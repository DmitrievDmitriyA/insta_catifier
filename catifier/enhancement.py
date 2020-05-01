import os
import catifier.face_recognition as face_recognition
from PIL import Image, ImageDraw2
from pathlib import Path
from pkg_resources import resource_filename


catImage = resource_filename(__name__, 'resources\\cat.png')
originalCatImage = Image.open(catImage).convert('RGBA')
ratio = 1.4


def _resize_cat_image(height):
    factor = height / originalCatImage.height * ratio
    height = (int)(originalCatImage.height*factor)
    width = (int)(originalCatImage.width*factor)
    return originalCatImage.resize((width, height))


def _create_folder(sourceUserFolder, resultUserFolder):
    # Create a folder for results if it doesn't exist
    Path(resultUserFolder).mkdir(parents=True, exist_ok=True)

    # And return total amount of files in sources folder
    return len(os.listdir(sourceUserFolder))


def _modify_source(sourceUserFolder, filename, resultUserFolder):
        filePath = sourceUserFolder + filename

        # Find faces
        faces = face_recognition.recognize_faces(filePath)

        background = Image.open(filePath)

        if len(faces):
            # Draw cats
            for (x, y, w, h) in faces:
                # Prepare cat image
                foreground = _resize_cat_image(h)
                # Center the coordinates for insertion
                cor_x = x - (foreground.height - h) // 2
                cor_y = y - (foreground.width - w) // 2
                # Prepare background
                background.paste(foreground, (cor_x, cor_y), foreground)

                # if debugMode:
                #     draw = ImageDraw2.Draw(background)
                #     draw.rectangle([x, y, x+w, y+h], ImageDraw2.Pen('red', width=4))

        resultPath = resultUserFolder + filename
        background.save(resultPath, format='JPEG')
        return {'resultPath': resultPath, 'hasFaces': bool(len(faces)) }


def add_cats_and_return_paths(sourceUserFolder, resultUserFolder, resultsNumber):
    totalAmountOfFiles = _create_folder(sourceUserFolder, resultUserFolder)

    filesCount = 0
    facedPhotos = 0
    results = []

    for filename in os.listdir(sourceUserFolder):
        filesCount += 1
        print(f"In progress: {filesCount} of {totalAmountOfFiles}")
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        result = _modify_source(sourceUserFolder, filename, resultUserFolder)

        # If photo contains no faces then check if result is not full yet
        # and append result in the end
        if not result['hasFaces']:
            if(len(results) < resultsNumber):
                results.append(result)
        else:
            for photo in results:
                if not photo['hasFaces']:
                    results.remove(photo)
                    break
            facedPhotos += 1
            results.append(result)

        # If we alredy has found enough faced photes then it's time to stop
        if facedPhotos == resultsNumber:
            break
    
    return results




def add_cats(sourceUserFolder, resultUserFolder):
    totalAmountOfFiles = _create_folder(sourceUserFolder, resultUserFolder)

    filesCount = 0

    for filename in os.listdir(sourceUserFolder):
        filesCount += 1
        print(f"In progress: {filesCount} of {totalAmountOfFiles}")
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        _modify_source(sourceUserFolder, filename, resultUserFolder)
