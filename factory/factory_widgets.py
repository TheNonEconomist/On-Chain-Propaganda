import cv2
import numpy as np

def concatenate_images_opencv(image_paths, horizontal=True):
    images = [cv2.imread(img_path) for img_path in image_paths]
    
    if horizontal:
        concatenated_image = np.hstack(images)
    else:
        concatenated_image = np.vstack(images)
    
    return concatenated_image


def add_text_alignment_check(
        image_path: list, text: str, 
        position: tuple, alignment: str,
        font, font_scale: int, font_color: tuple, font_thickness: int
        ):
    """
    add text as well as where it's aligned. By default it's left aligned from the position
    """
    if alignment == "right":
        (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        position = (position[0]-text_w, position[1]+text_h)
    elif alignment == "center":
        (text_w, text_h), _ = cv2.getTextSize(text, font, font_scale, font_thickness)
        position = (position[0]-text_w//2, position[1]+text_h//2)
    
    return __add_text_to_image(image_path, text, position, font, font_scale, font_color, font_thickness)


def __add_text_to_image(image_path, text, position, font=cv2.FONT_ITALIC, font_scale=1, font_color=(255, 0, 0), font_thickness=50):
    # Read the image
    image = cv2.imread(image_path)

    # Add text to the image
    cv2.putText(image, text, position, font, font_scale, font_color, font_thickness)

    return image


