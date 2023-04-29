import os 
from PIL import Image


PATH = 'downloaded'
NEW_PATH = 'downloaded_rotated'

dirs = os.listdir(PATH)
for img_file in dirs :  
    img = Image.open(os.path.join(PATH,img_file))
    img = img.rotate(270) 
    img_name = img_file.split("/")[-1]
    img.save(os.path.join(NEW_PATH,img_name))
    print(f"image {img_name} saved to {NEW_PATH}/{img_name}")
