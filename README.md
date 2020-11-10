# py-facial-recog

Cryptography facial authentication assignment.
using OpenCV and TKinter as GUI interface.

## Requirements
1. Python >= 3.8
2. pip
3. Virtualenv (Optional)

## Installation
Go to directory and run:

`pip install -r requirements.txt`

Create a user folder in data and fill it with user's name and facial profile

```
data/
|
|_ user/
    |_ example_guy/
    |   |_ picture.png
    |   |_ face.png
    |   |_ another_face.jpg
    |_ another_guy/
        |_ face.png
        |_ smile.jpg
```

Run `Authenticator.py` to cache the user information

`python Authenticator.py`

To compile an executable run - pyInstaller:

`pyinstaller --onefile Application.py`

Then copy and paste the data folder into the `/dist` folder


## Known Errors
Based on the known errors reported by Numpy, there is a runtime error within Windows 10 machines that have been patched to 2004.
This will prompt and error as below

```
RuntimeError: The current Numpy installation ('xxx\\Python38\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the window runtime. See this issue for more information: https://tinyurl.com/y3dm3h86
ImportError: numpy.core.multiarray failed to import
```
