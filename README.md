# Face Swap App

## Overview

The Face Swap App allows users to upload two images and swap the faces between them using deep learning techniques. Built with Streamlit, OpenCV, and the InsightFace library, this application provides a simple interface for face swapping.

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

- **Source Image**: The image from which the face will be extracted.
- **Target Image**: The image to which the face will be applied.

### Result

The application will display the original images and the resulting images with the swapped faces.

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

