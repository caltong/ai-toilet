from camera.camera import Camera


if __name__ == '__main__':
    camera = Camera()
    while 1:
        face = camera.detect_face()
        if face:
            print('face detected!')
        else:
            print('face not detected!')
