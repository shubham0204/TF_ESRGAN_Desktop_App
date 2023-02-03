# Super Resolution with ESRGANs in Desktop Apps
> Building the UI with Qt (Qt Creator) and writing the
> logic in Python, getting the best of both worlds 💪

A desktop app built with Qt (PySide6) for super resolution with ESRGANs in TensorFlow

### Building executables with GitHub Actions

A GitHub workflow defined by `build_apps.yml` in `.build/workflows` is
used to build portable executables for Windows and Linux. It contains two jobs, that are 
identical but run on `windows-latest` and `ubuntu-latest` respectively using 
the `main.spec` file to build the executables.

The workflow is initiated manually and the artifacts (executables) are uploaded 
as a release with an increment in the version.

### Frameworks/Packages

- [`PySide6`](https://doc.qt.io/qtforpython/) 
- [`PyInstaller`](https://pyinstaller.org/en/stable/index.html)
- [`TensorFlow`](https://www.tensorflow.org) and [`TensorFlow Hub`](https://www.tensorflow.org/hub)
- [`Qt Creator`](https://www.qt.io/product/development-tools) (Open-source version)

## Contribution

If you wish to extend the functionality of the project or add new ML-app examples,
open a new PR or a new issue mentioning the details of example required.

See [🚀 Future Scope](https://github.com/shubham0204/TF_ESRGAN_Desktop_App/discussions/1) 
for more ideas and possible contributions