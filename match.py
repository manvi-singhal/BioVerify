import numpy as np
import os

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def load_minutiae_from_file(file_path):
    minutiae_list = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())  # Adjust this based on your file format
            minutiae_list.append((x, y))
    return minutiae_list

def match_with_database(input_image, input_minutiae, database_folder):
    input_minutiae_set = set(tuple(m) for m in input_minutiae)

    match_scores = []

    for file_name in range(1, 33):  # Assuming images are named from 1.png to 32.png
        file_path = os.path.join(database_folder, f"{file_name}.png")

        # Load minutiae from the database file
        template_minutiae = load_minutiae_from_file(file_path)

        template_minutiae_set = set(tuple(m) for m in template_minutiae)

        # Jaccard similarity coefficient (intersection over union)
        match_score = len(input_minutiae_set.intersection(template_minutiae_set)) / len(
            input_minutiae_set.union(template_minutiae_set))

        # Sigmoid function to normalize the score between 0 and 1
        normalized_score = sigmoid(match_score)

        # Append the normalized score to the list of match scores
        match_scores.append(normalized_score)

    # Find the index of the best match
    best_match_index = np.argmax(match_scores)

    # Find the best match score
    best_match_score = match_scores[best_match_index]

    return best_match_index, best_match_score
