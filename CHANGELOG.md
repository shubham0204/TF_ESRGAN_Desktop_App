- ESRGAN now runs on a worker thread to avoid app suspensions
- Added strict RGB conversion for PNG images
- Added `tf.clip_by_value` to avoid color changes in the 
output image.
- The output image is resized to the original dimensions 
of the input image, on saving.
- Window title changes to 'Processing' when an image is 
being processed
- Added window icon for the `App`