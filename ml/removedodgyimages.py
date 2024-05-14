# Data preprocessing - removing dodgy images
import os
import cv2
import imghdr

data_dir = 'data' 
image_exts = ['jpeg','jpg', 'png']

for image_class in os.listdir(data_dir): 
    for image in os.listdir(os.path.join(data_dir, image_class)):
        image_path = os.path.join(data_dir, image_class, image)
        try: 
            img = cv2.imread(image_path)
            tip = imghdr.what(image_path)
            if tip not in image_exts: 
                print(f'Image not in ext list {format(image_path)}')
                os.remove(image_path)
        except Exception as e: 
            print(f'Issue with image {format(image_path)}')

# Code for listing the number of images in each subdirectory in the data folder
# (to see how many images of each character there are)
for image_class in os.listdir(data_dir):
    class_dir = os.path.join(data_dir, image_class)
    if os.path.isdir(class_dir):
        num_images = len(os.listdir(class_dir))
        print(f"{image_class}: {num_images} images")