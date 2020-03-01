import sys
import os
import face_recognition
from PIL import Image
from pathlib import Path

originalCatImage = Image.open('resources\\cat.png').convert('RGBA')
sourceFolder = 'insta_sources\\'
resultFolder = 'catified\\'
ratio = 1.4

def resize_cat_image(height):
    factor = height / originalCatImage.height * ratio
    height = (int)(originalCatImage.height*factor)
    width = (int)(originalCatImage.width*factor)
    return originalCatImage.resize((width, height))


def add_cats(userName):
    sourceUserFolder = sourceFolder + userName + '\\'
    resultUserFolder = resultFolder + userName + '\\'
    Path(resultUserFolder).mkdir(parents=True, exist_ok=True) # Create a folder for results if it doesn't exist

    for filename in os.listdir(sourceUserFolder):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            break

        filePath = sourceUserFolder + filename
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
            background.save(resultUserFolder + filename, format='JPEG')

def main():
    userName = sys.argv[1]
    
    add_cats(userName)

if __name__ == '__main__':
    main()