import cv2
from PIL import Image
import time
import os
from config import root_path


class Camera:
    capture = 0

    def __init__(self):
        print(root_path)
        self.capture = cv2.VideoCapture(0)

    def get_one_frame_from_camera(self):
        # get one from from camera
        ret, frame = self.capture.read()

        return frame

    def detect_face(self):
        frame = self.get_one_frame_from_camera()

        # detect face and cut frame
        face_cascade = cv2.CascadeClassifier(os.path.join(root_path, 'camera', 'haarcascade_frontalface_default.xml'))
        # face_cascade.load('./haarcascade_frontalface_default.xml')

        # convert to gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect face
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # test origin image from camera
        # frame_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        # frame_image.show()

        # get the 1st face of faces
        if len(faces) < 1:
            return None
        else:
            face = faces[0]

        face_frame = frame[face[1]:face[1] + face[3], face[0]:face[0] + face[2]]
        face_frame = Image.fromarray(cv2.cvtColor(face_frame, cv2.COLOR_BGR2RGB))

        return face_frame


if __name__ == '__main__':
    camera = Camera()

    while 1:
        time.sleep(1)
        face_frame = camera.detect_face()
        print(face_frame)

        # if face_frame:
        #     face_frame.show()
