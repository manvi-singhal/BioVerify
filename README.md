# Fingerprint Recognition

## Key Features

## 1. Input Module

- Efficiently loads fingerprint images and templates using OpenCV.
- Adaptable to diverse fingerprint sensors.

## 2. Preprocessing Module

- Enhances image quality through histogram equalization, binarization, and morphological processing.
- Ensures high-quality images for accurate recognition.

## 3. Extracting Minutiae Module

- Identifies minutiae for effective feature extraction.
- Utilizes gradient calculation, ridge orientation, and frequency computation.

## 4. Matching Module

- Computes Jaccard similarity coefficients and normalizes scores with a sigmoid function.
- Identifies the best match for effective fingerprint matching.

## 5. Database Module

- Manages a collection of high-quality rolled fingerprint images as templates.

## 6. Output Module

- Presents results, including best match index, score, and visual representation.

## Execution Flow

- Database Module: Loads high-quality rolled fingerprint images.
- Input Module: Loads input image and templates.
- Preprocessing Module: Enhances image quality.
- Extracting Minutiae Module: Identifies minutiae for feature extraction.
- Matching Module: Computes similarity, normalizes scores, and identifies the best match.
- Output Module: Presents results.

