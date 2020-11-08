import os
import cv2

import numpy
from PIL import Image
import pickle

base_dir    =   os.path.dirname(os.path.abspath(__file__))
user_dir    =   os.path.join(base_dir, "data/user")

face_profile    =   cv2.CascadeClassifier(base_dir + "/data/haarcascade_frontalface_default.xml")
face_recognizer =   cv2.face.LBPHFaceRecognizer_create()

current_id  =   0
label_id    =   {}

y_labels    =   []
x_train     =   []

for root, dirs, files in os.walk(user_dir):
    for file in files:
        if file.endswith('.png') or file.endswith('.jpg'):
            path    =   os.path.join(root, file)
            label   =   os.path.basename(os.path.dirname(path)).replace(' ', '_').lower()

            if label in label_id:
                pass
            else:
                label_id[label]     =   current_id
                current_id         +=   1

            id_ =   label_id[label]

            pil_image   =   Image.open(path).convert("L")
            size        =   (1080, 1920)
            rescale_img =   pil_image.resize(size, Image.ANTIALIAS)
            image_array =   numpy.array(rescale_img, "uint8")

            facial      =   face_profile.detectMultiScale(image_array, 1.5, 5)

            for (x, y, w, h) in facial:
                region_of_interest  =   image_array[y:y+h, x:x+w]
                x_train.append(region_of_interest)
                y_labels.append(id_)

with open(base_dir + "/data/saves/labels.pkl", 'wb') as f:
    pickle.dump(label_id, f)

face_recognizer.train(x_train, numpy.array(y_labels))
face_recognizer.save(base_dir + "/data/saves/cache.xml")
