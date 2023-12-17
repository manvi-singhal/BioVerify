import cv2
import numpy as np


def extract_minutiae(image, image_name, display_minutiae=False):
    gradient_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    ridge_orientation = np.arctan2(gradient_y, gradient_x)
    ridge_frequency = np.sqrt(gradient_x ** 2 + gradient_y ** 2)

    gradient_magnitude = np.sqrt(gradient_x ** 2 + gradient_y ** 2)
    _, ridge_mask = cv2.threshold(gradient_magnitude, 70, 255, cv2.THRESH_BINARY)

    if image_name:
        print(f"Extracting minutiae for image: {image_name}")

    minutiae_mask = np.zeros_like(image)

    threshold_percentile = np.percentile(ridge_frequency, 80)  # 80th percentile

    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            # Checking if the pixel is part of a ridge and has a sufficient ridge frequency
            if ridge_mask[i, j] == 255 and ridge_frequency[i, j] > threshold_percentile:
                neighborhood = ridge_orientation[i - 1:i + 2, j - 1:j + 2]
                # Checking the neighborhood for ridge conditions
                if np.sum(neighborhood == ridge_orientation[i, j]) == 1:
                    minutiae_mask[i, j] = 255

    if display_minutiae:
        minutiae_image = cv2.bitwise_and(image, image, mask=minutiae_mask)
        cv2.imshow("Minutiae Image", minutiae_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    minutiae_coords = np.column_stack(np.where(minutiae_mask > 0))

    return minutiae_coords
