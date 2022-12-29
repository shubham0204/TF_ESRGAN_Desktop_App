from mainwindow_qt import Ui_MainWindow
from PIL import Image
from PIL import ImageOps
from PIL import ImageQt
import PySide6.QtWidgets as widgets
import PySide6.QtGui as gui
import numpy as np
import os
import sys

import tensorflow_hub as hub
import tensorflow as tf

class App( widgets.QMainWindow ):

    def __init__(self):
        super( App , self).__init__()
        self.current_secs = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Super Resolution with ESRGANs")

        self.ui.save_image.clicked.connect(self.on_save_image_click)
        self.ui.select_image.clicked.connect(self.on_select_image_click)
        self.ui.super_resolve.clicked.connect(self.on_super_resolve_click)

        self.model = hub.load( "https://tfhub.dev/captain-pool/esrgan-tf2/1" )

        self.selected_image = None
        self.converted_image = None

    def on_select_image_click(self):
        selected_file_path = widgets.QFileDialog.getOpenFileName( self )
        if selected_file_path[0] is not None:
            image_file = open( selected_file_path[0] , 'rb' )
            image = Image.open( image_file )
            self.set_image( image , self.ui.input_img )
            self.selected_image = np.asarray( image , dtype='float32' )

    def on_save_image_click(self):
        selected_file_path = widgets.QFileDialog.getExistingDirectory(self)
        if selected_file_path is not None:
            self.converted_image.save( os.path.join( selected_file_path , 'img.png' ) )

    def on_super_resolve_click(self):
        low_resolution_image = np.expand_dims( self.selected_image , axis=0 )
        low_resolution_image = tf.cast( low_resolution_image , tf.float32 )
        self.ui.super_resolve.setText("Processing...")
        output = self.model( low_resolution_image ).numpy()[0]
        output = ( output - output.min() ) / ( output.max() - output.min() )
        output *= 255
        self.converted_image = Image.fromarray( output.astype( np.uint8 ) )
        self.set_image( self.converted_image , self.ui.output_img )
        self.ui.super_resolve.setText( "Super Resolve" )

    def set_image( self , image , label ):
        resized_image = ImageOps.contain( image , ( 500 , 500 ) )
        image = ImageQt.ImageQt( resized_image )
        label.setPixmap(gui.QPixmap.fromImage(image))

    def display_message( self , title , icon , message , button ):
        warning = widgets.QMessageBox()
        warning.setIcon( icon )
        warning.setWindowTitle( title )
        warning.setText( message )
        warning.setStandardButtons( button )
        warning.exec()


def resolve_path(path):
    if getattr(sys, "frozen", False):
        resolved_path = os.path.abspath(os.path.join(sys._MEIPASS, path))
    else:
        resolved_path = os.path.abspath(os.path.join(os.getcwd(), path))
    return resolved_path


app = widgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(app.exec())
