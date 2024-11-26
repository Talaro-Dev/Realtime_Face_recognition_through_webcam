#I used this script in order to resize my images to 250x250 in order the model to be trained, also my images wanted to be rotated 90 degress clockwise in order not to be
#horizontal

import os 
from PIL import Image

source_folder = r'C:\Users\georg\Desktop\me' 
destination_folder = r'C:\Users\georg\Desktop\me\new' 


if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)


target_size = (250, 250) #new size of images


def resize_and_rotate_images(source_folder, destination_folder, target_size):
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):  
            try:
                img_path = os.path.join(source_folder, filename)
                img = Image.open(img_path)  
                
                # Rotate the image 90 degrees clockwise
                img = img.rotate(-90, expand=True)  
                
                # Resize image to the target size
                img = img.resize(target_size, Image.LANCZOS)  
                
                # Save the resized image to the destination folder
                img.save(os.path.join(destination_folder, filename))
                print(f"Resized and rotated: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")
        else:
            print(f"Skipped non-image file: {filename}") 


resize_and_rotate_images(source_folder, destination_folder, target_size)
