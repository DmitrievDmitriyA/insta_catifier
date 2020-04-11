import os
import backend.face_recognition as face_recognition
from PIL import Image, ImageDraw2
from pathlib import Path

originalCatImage = Image.open('resources\\cat.png').convert('RGBA')
ratio = 1.4

def resize_cat_image(height):
    factor = height / originalCatImage.height * ratio
    height = (int)(originalCatImage.height*factor)
    width = (int)(originalCatImage.width*factor)
    return originalCatImage.resize((width, height))


def add_cats(debugMode, userName, sourceUserFolder, resultUserFolder):
    Path(resultUserFolder).mkdir(parents=True, exist_ok=True) # Create a folder for results if it doesn't exist

    totalAmountOfFiles = len(os.listdir(sourceUserFolder))
    filesCount = 0

    for filename in os.listdir(sourceUserFolder):
        filesCount += 1
        print(f"In progress: {filesCount} of {totalAmountOfFiles}")
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        filePath = sourceUserFolder + filename
        if debugMode:
            print(filename)

        # Find faces
        faces = face_recognition.recognize_faces(filePath)

        if len(faces):
            background = Image.open(filePath)
            # Draw cats 
            for (x, y, w, h) in faces:
                # Prepare cat image
                foreground = resize_cat_image(h)
                # Center the coordinates for insertion
                cor_x = x - (foreground.height - h) // 2
                cor_y = y - (foreground.width - w) // 2
                # Prepare background
                background.paste(foreground, (cor_x, cor_y), foreground)

                if debugMode:
                    draw = ImageDraw2.Draw(background)
                    draw.rectangle([x, y, x+w, y+h], ImageDraw2.Pen('red', width=4))

            background.save(resultUserFolder + filename, format='JPEG')