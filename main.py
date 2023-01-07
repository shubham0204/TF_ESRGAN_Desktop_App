from mainwindow_qt import Ui_MainWindow
from PIL import Image
from PIL import ImageOps
from PIL import ImageQt
import PySide6.QtWidgets as widgets
import PySide6.QtGui as gui
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
import os
import sys
import threading


class App( widgets.QMainWindow ):

    def __init__(self):
        super( App , self).__init__()
        self.current_secs = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Super Resolution with ESRGANs")
        self.statusBar().setSizeGripEnabled(False)
        self.setMaximumWidth( self.geometry().width())
        self.setMaximumHeight( self.geometry().height())

        self.ui.save_image.clicked.connect(self.on_save_image_click)
        self.ui.select_image.clicked.connect(self.on_select_image_click)
        self.ui.super_resolve.clicked.connect(self.on_super_resolve_click)

        self.loading_thread = None
        self.start_tf_model_loading()

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
        if self.loading_thread.is_alive():
            return

        low_resolution_image = np.expand_dims( self.selected_image , axis=0 )
        low_resolution_image = tf.cast( low_resolution_image , tf.float32 )

        self.ui.super_resolve.setText("Processing...")
        self.ui.super_resolve.repaint()

        output = self.model( low_resolution_image ).numpy()[0]
        output = ( output - output.min() ) / ( output.max() - output.min() )
        output *= 255
        self.converted_image = Image.fromarray( output.astype( np.uint8 ) )
        self.set_image( self.converted_image , self.ui.output_img )

        self.ui.super_resolve.setText( "Super Resolve" )
        self.ui.super_resolve.repaint()


    def set_image( self , image , label ):
        resized_image = ImageOps.contain( image , ( 500 , 500 ) )
        image = ImageQt.ImageQt( resized_image )
        label.setPixmap(gui.QPixmap.fromImage(image))


    def start_tf_model_loading(self):
        self.loading_thread = threading.Thread( target=self.load_tf_model , name="TF Model Loading" )
        self.loading_thread.start()

    def load_tf_model( self ):
        self.model = hub.load( "https://tfhub.dev/captain-pool/esrgan-tf2/1" )


app = widgets.QApplication(sys.argv)
window = App()

window.show()
sys.exit(app.exec())
