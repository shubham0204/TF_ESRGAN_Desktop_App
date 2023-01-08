import torch
from PIL import Image
import numpy as np
from RealESRGAN import RealESRGAN

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = RealESRGAN( device, scale=4 )
model.load_weights( 'RealESRGAN_x4.pth' )

image = Image.open( 'input_image.jpg' ).convert( 'RGB' )
output = model.predict( image )
output.save( 'output_image.jpg' )

