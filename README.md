# py-facial-recog

## Requirements
1. Python >= 3.8
2. pip
3. Virtualenv (Optional)

## Installation
Go to directory and run:
`pip install -r requirements.txt`

Create a user folder in data and fill it with user's name and facial profile

`
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
`

Run pyInstaller:
`pyinstaller --onefile Application.py`
