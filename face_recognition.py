import cv2

def recognize_faces(filePath):
    image = cv2.imread(filePath)
    # Load the cascade
    face_cascade = cv2.CascadeClassifier('resources\haarcascade_frontalface_default.xml')
    # Convert into grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces
    return face_cascade.detectMultiScale(gray, 1.1, 4)