import cv2
import numpy as np

def concatenate_images_opencv(image_paths, horizontal=True):
    images = [cv2.imread(img_path) for img_path in image_paths]
    
    if horizontal:
        concatenated_image = np.hstack(images)
    else:
        concatenated_image = np.vstack(images)
    
    return concatenated_image

def add_text_to_image(image_path, text, position, font=cv2.FONT_ITALIC, font_scale=1, font_color=(255, 0, 0), font_thickness=50):
    # Read the image
    image = cv2.imread(image_path)

    # Add text to the image
    cv2.putText(image, text, position, font, font_scale, font_color, font_thickness)

    return image

def propaganda_template(picture, )