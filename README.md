# Face Swap App

## Overview

The Face Swap App allows users to upload two images and swap the faces between them using deep learning techniques. Built with Streamlit, OpenCV, and the InsightFace library, this application provides a simple interface for face swapping.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Model](#model)
- [Usage](#usage)
- [Example](#example)
- [Result](#result)
- [License](#license)

## Features

- Upload two images (source and target).
- Swap faces between the two images.
- Preview original and swapped images.
- Download the swapped images in JPEG format.

## Requirements

- Python 3.7 or later
- Streamlit
- NumPy
- OpenCV
- Matplotlib
- InsightFace

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/shukdevtroy/Face-Swap-APP.git
   cd Face-Swap-APP
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Ensure that you have the InsightFace model files. If you don't have them, the app will automatically download them the first time you run it.

## Model

**InsightFace Model**: [Click to here to download the model file](https://drive.google.com/file/d/190gxPPj8yQX6qL-NAava3XqD4MWT0av_/view?usp=sharing)

## Usage

1. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501`.

3. Upload your source and target images using the file upload buttons.

4. View the original images and the swapped images side by side.

5. Click the download buttons to save the swapped images to your local machine.

## Example

### Uploading Images

- **Source Image**:

  ![Example Image](https://github.com/shukdevtroy/Face-Swap-APP/blob/main/images/source.jpg)
  
- **Target Image**:

  ![Example Image](https://github.com/shukdevtroy/Face-Swap-APP/blob/main/images/target.jpg)

### Result

The application will display the original images and the resulting images with the swapped faces.

- **Swapped Face 1**:

![Example Image](https://github.com/shukdevtroy/Face-Swap-APP/blob/main/images/swapsource.jpg)

- **Swapped Face 2**:

![Example Image](https://github.com/shukdevtroy/Face-Swap-APP/blob/main/images/swaptarget.jpg)


## Notes

- Make sure the images you upload are clear and well-lit for the best results.
- The app utilizes GPU processing if available; ensure that your environment is set up correctly to leverage this.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please contact:

- **Email**: shukdevdatta@gmail.com
- **GitHub**: [Click to here to access the Github Profile](https://github.com/shukdevtroy)
- **WhatsApp**: [Click here to chat](https://wa.me/+8801719296601)

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenCV](https://opencv.org/)
- [InsightFace](https://github.com/deepinsight/insightface)

