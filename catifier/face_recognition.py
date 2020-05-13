import cv2
from pkg_resources import resource_filename

def recognize_faces(filePath):
    image = cv2.imread(filePath)
    # Load the cascade
    cascadeSource = resource_filename(__name__, 'resources/haarcascade_frontalface_default.xml')
    face_cascade = cv2.CascadeClassifier(cascadeSource)
    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    return face_cascade.detectMultiScale(gray, 1.1, 4)