#In this script i check all my files are not corrupted before training

from PIL import Image
import os

def check_images(directory):
    invalid_images = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".jpeg"):
                file_path = os.path.join(root, file)
                try:
                    img = Image.open(file_path)
                    img.verify()  # Check if the file can be opened
                except (IOError, SyntaxError) as e:
                    invalid_images.append(file_path)
    return invalid_images

directory = 'path_to_your_dataset'  
corrupted_files = check_images(directory)

if corrupted_files:
    print("Corrupted files:")
    for file in corrupted_files:
        print(file)
else:
    print("No corrupted files found.")
