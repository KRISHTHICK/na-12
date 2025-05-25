import cv2
import numpy as np

def virtual_try_on(user_image_path, clothing_image_path):
    user_image = cv2.imread(user_image_path)
    clothing_image = cv2.imread(clothing_image_path)

    # Resize clothing image to fit the user image
    clothing_image = cv2.resize(clothing_image, (user_image.shape[1], user_image.shape[0]))

    # Create a mask for the clothing image
    clothing_mask = clothing_image[:, :, 3]  # Assuming the clothing image has an alpha channel
    clothing_mask = cv2.cvtColor(clothing_mask, cv2.COLOR_GRAY2BGR)

    # Combine images
    combined_image = np.where(clothing_mask == 0, user_image, clothing_image)

    return combined_image
