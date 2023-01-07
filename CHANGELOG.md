- Moved the loading of TF Hub model from main thread to a 
worker thread in `main.py` using `threading`
- Fixed size of `QMainWindow`/`App` in `main.py`
- *Super Resolve* button now shows `Processing...` when the 
image is being processed.