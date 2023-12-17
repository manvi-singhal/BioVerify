import os
import cv2
from preprocess import preprocess_image
from minutiae import extract_minutiae
from match import match_with_database

if __name__ == "__main__":
    # Path to the input image
    input_image_path = "db/1.png"

    # Path to the fingerprint database folder
    database_folder = "db"

    # List all files in the database folder
    database_files = os.listdir(database_folder)
    # Load images from the database folder
    database = [cv2.imread(os.path.join(database_folder, file), cv2.IMREAD_GRAYSCALE) for file in database_files]

    # Preprocess the input image
    processed_image = preprocess_image(input_image_path)

    # Extract minutiae from the processed image and display minutiae for the input image only
    minutiae = extract_minutiae(processed_image, image_name=input_image_path, display_minutiae=True)
    # Extract minutiae from each database image (without displaying minutiae)
    database_minutiae = [extract_minutiae(template, display_minutiae=False) for template in database]

    # Match the processed image with the database using minutiae information
    best_match_index, best_match_score = match_with_database(processed_image, minutiae, database_minutiae)

    # Print the result
    print(f"Best match index: {best_match_index}")
    print(f"Best match score: {best_match_score}")

    # Display the matched image
    matched_image = cv2.imread(os.path.join(database_folder, database_files[best_match_index]), cv2.IMREAD_GRAYSCALE)
    cv2.imshow(f"Matched Image at Index {best_match_index}", matched_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
