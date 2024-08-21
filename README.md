# Project 3: Galaxy Zoo
**Contributors:** Rob Pavlik, Mitchell Terry, Tony Montgomery, Trenton Parker

## Overview
This project aims to assist in the manual classification of galaxy images by developing a robust image classification model. The goal is to streamline and enhance the process of analyzing galaxy images, galaxies as belonging to one of six categories, reducing the reliance on manual classification methods. It is not intended to 100% replace human classifiers, instead we hope to quickly weed out images that have artifacts preventing classification and allow humans to focus on those images that need human interpretation.

![Galaxy Image Classification](https://github.com/user-attachments/assets/9320ff63-ac79-4d57-b925-0d63cff25e56)

## Data
The dataset utilized for this project is sourced from [Galaxy Zoo](https://data.galaxyzoo.org/) 2, a large-scale citizen science project that provides extensive galaxy images for classification purposes.

## Installation and Setup
To get started with the project, ensure you have the necessary resources by following these steps:

1. Install the required package:
    ```sh
    pip install galaxy-datasets
    ```

2. Run the dataset utility script to download the necessary data:
    ```sh
    python datasets_util.py
    ```

## Acknowledgements
The images used in this project are intended to complement the data tables available at [Galaxy Zoo](https://data.galaxyzoo.org/). These images are part of the original sample of subject images in Galaxy Zoo 2 (Willett et al. 2013, MNRAS, 435, 2835, DOI: [10.1093/mnras/stt1458](https://doi.org/10.1093/mnras/stt1458)), as identified in Table 1 of Willett et al., and also referenced in Hart et al. (2016, MNRAS, 461, 3663, DOI: [10.1093/mnras/stw1588](https://doi.org/10.1093/mnras/stw1588)). Please note that while the original GZ2 subjects provided an option to view an inverted version of the subject image, these inverted images are not included but can be easily recreated from the provided images.
