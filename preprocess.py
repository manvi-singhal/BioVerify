import cv2
import numpy as np


def preprocess_image(image_path):
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    cv2.imshow("Original Image", original_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    enhanced_image = cv2.equalizeHist(original_image)  # Image Enhancement
    cv2.imshow("Enhanced Image", enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    _, binary_image = cv2.threshold(enhanced_image, 128, 255, cv2.THRESH_BINARY)  # Binarisation
    cv2.imshow("Binary Image", binary_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    kernel = np.ones((3, 3), np.uint8)  # Structuring Element
    morph_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)  # Morphological Operations
    cv2.imshow("Morphological Processed Image", morph_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return morph_image
