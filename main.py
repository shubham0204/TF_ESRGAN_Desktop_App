from mainwindow_qt import Ui_MainWindow
from PIL import Image
from PIL import ImageOps
from PIL import ImageQt
from RealESRGAN import RealESRGAN
import PySide6.QtWidgets as widgets
import PySide6.QtGui as gui
import os
import sys
import threading
import torch


class App( widgets.QMainWindow ):

    def __init__(self):
        super( App , self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("Super Resolution with ESRGANs")
        self.setWindowIcon( gui.QIcon( 'app_icon.ico' ) )
        self.statusBar().setSizeGripEnabled(False)
        self.setMaximumWidth( self.geometry().width())
        self.setMaximumHeight( self.geometry().height())

        self.ui.save_image.clicked.connect(self.on_save_image_click)
        self.ui.select_image.clicked.connect(self.on_select_image_click)
        self.ui.super_resolve.clicked.connect(self.on_super_resolve_click)

        self.loading_thread = None
        self.inference_thread = None
        self.start_tf_model_loading()

        self.selected_image = None
        self.selected_image_size = None
        self.selected_image_name = None
        self.converted_image = None
        self.model = None


    def on_select_image_click(self):
        selected_file_path = widgets.QFileDialog.getOpenFileName( self )
        path = selected_file_path[0]
        if path is not None:
            image_file = open( path , 'rb' )
            image = Image.open( image_file ).convert( 'RGB' )
            self.set_image( image , self.ui.input_img )
            self.selected_image_size = image.size
            self.selected_image_name = os.path.basename( path )
            self.selected_image = image


    def on_save_image_click(self):
        selected_file_path = widgets.QFileDialog.getExistingDirectory(self)
        if selected_file_path is not None:
            self.converted_image\
                .resize( self.selected_image_size )\
                .save( os.path.join( selected_file_path , f'sr_{self.selected_image_name}.jpg' ) )


    def on_super_resolve_click(self):
        if self.loading_thread.is_alive():
            return

        self.ui.super_resolve.setText("Processing...")
        self.setWindowTitle("Processing...")
        self.ui.super_resolve.repaint()

        self.inference_thread = threading.Thread( target=self.perform_inference , name='Inference' )
        self.inference_thread.start()


    def perform_inference( self ):
        self.converted_image = self.model.predict( self.selected_image )
        self.set_image( self.converted_image , self.ui.output_img )

        self.ui.super_resolve.setText( "Super Resolve" )
        self.setWindowTitle("Super Resolution with ESRGANs")
        self.ui.super_resolve.repaint()


    def set_image( self , image , label ):
        resized_image = ImageOps.contain( image , ( 500 , 500 ) )
        image = ImageQt.ImageQt( resized_image )
        label.setPixmap(gui.QPixmap.fromImage(image))


    def start_tf_model_loading(self):
        self.loading_thread = threading.Thread( target=self.load_tf_model , name="PyTorch Model Loading" )
        self.loading_thread.start()

    def load_tf_model( self ):
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model = RealESRGAN(device, scale=2)
        self.model.load_weights('torch_models/RealESRGAN_x2.pth')


app = widgets.QApplication(sys.argv)
window = App()

window.show()
sys.exit(app.exec())
