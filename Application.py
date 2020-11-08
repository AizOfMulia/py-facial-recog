import cv2
import os
import PySimpleGUI as GUI
import pickle

path                =   os.path.dirname(os.path.abspath(__file__))
labels              =   {}

with open(path + "/data/saves/labels.pkl", 'rb') as f:
    labels      =   pickle.load(f)
    labels      =   {v:k for k,v in labels.items()}

def main():
    layout              =   [[GUI.Text("Please Login")], [GUI.Button("Login")], [GUI.Button("Close")]]
    window              =   GUI.Window("The Next Gen App", layout, margins=(100, 50))

    while True:
        event, values   =   window.read()

        if event == "Login":
            #GUI.Popup("Login Clicked", keep_on_top=True)
            user = facial_recongition()
            #if authenticated then popup "User: Akmal has logged in"
            GUI.Popup(user + " has logged in", keep_on_top=True)

        if event == "Close" or event == GUI.WIN_CLOSED:
            break

    window.close()

#def authenticate():


def facial_recongition():
    camera              =   cv2.VideoCapture(0)

    face_profile    =   cv2.CascadeClassifier(path + '/data/haarcascade_frontalface_default.xml')
    eye_profile     =   cv2.CascadeClassifier(path + '/data/haarcascade_eye.xml')
    recognizer      =   cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(path + "/data/saves/cache.xml")

    name            =   ""

    if not camera.isOpened():
        print("Camera is not active")
        exit()

    while True:
        ret, frame  =   camera.read()

        if not ret:
            print("frame can't be retrieved")
            break

        gray    =   cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        facial  =   face_profile.detectMultiScale(gray, 1.5, 5)

        for (x, y, w, h) in facial:
            region_of_interest_gray    =   gray[y:y+h, x:x+w]
            region_of_interest_color   =   frame[y:y+h, x:x+w]

            id_, confidence   =   recognizer.predict(region_of_interest_gray)

            if confidence >= 75 and confidence <= 100:
                font    =   cv2.FONT_HERSHEY_SIMPLEX
                name    =   labels[id_]

                color   =   (255, 255, 255)
                stroke  =   1

                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

            border_color               =   (0, 255, 0)
            border_stroke_size         =   1

            end_coord_x                =   x + w
            end_coord_y                =   y + h

            cv2.rectangle(frame, (x,y), (end_coord_x, end_coord_y), border_color, border_stroke_size)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if name:
            break

    camera.release()
    cv2.destroyAllWindows()

    return name

if __name__ == "__main__":
    main()
