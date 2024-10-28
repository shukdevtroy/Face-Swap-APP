import streamlit as st
import numpy as np
import cv2
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model
import tempfile

# Initialize face analysis app
app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(640, 640))

# Load the face swapper model
swapper = get_model('inswapper_128.onnx', download=False, download_zip=False)

def swap_faces(img1, img2):
    face1 = app.get(img1)[0]
    face2 = app.get(img2)[0]
    
    img1_swapped = img1.copy()
    img2_swapped = img2.copy()

    img1_swapped = swapper.get(img1_swapped, face1, face2, paste_back=True)
    img2_swapped = swapper.get(img2_swapped, face2, face1, paste_back=True)
    
    return img1_swapped, img2_swapped

def main():
    st.title("Face Swap App")
    
    # Upload source image
    source_image = st.file_uploader("Upload Source Image", type=["jpg", "jpeg", "png"])
    # Upload target image
    target_image = st.file_uploader("Upload Target Image", type=["jpg", "jpeg", "png"])
    
    if source_image is not None and target_image is not None:
        # Read images
        img1 = cv2.imdecode(np.frombuffer(source_image.read(), np.uint8), 1)
        img2 = cv2.imdecode(np.frombuffer(target_image.read(), np.uint8), 1)
        
        # Swap faces
        img1_swapped, img2_swapped = swap_faces(img1, img2)

        # Display original and swapped images
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Source Image")
            st.image(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB), channels="RGB")

        with col2:
            st.subheader("Target Image")
            st.image(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB), channels="RGB")

        st.subheader("Swapped Images")
        col3, col4 = st.columns(2)
        
        with col3:
            st.image(cv2.cvtColor(img1_swapped, cv2.COLOR_BGR2RGB), channels="RGB", caption="Source with Target Face")
            # Save button for Source with Target Face
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                cv2.imwrite(tmp_file.name, img1_swapped)
                st.download_button(
                    label="Download Source with Target Face",
                    data=open(tmp_file.name, "rb").read(),
                    file_name="source_with_target_face.jpg",
                    mime="image/jpeg"
                )

        with col4:
            st.image(cv2.cvtColor(img2_swapped, cv2.COLOR_BGR2RGB), channels="RGB", caption="Target with Source Face")
            # Save button for Target with Source Face
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                cv2.imwrite(tmp_file.name, img2_swapped)
                st.download_button(
                    label="Download Target with Source Face",
                    data=open(tmp_file.name, "rb").read(),
                    file_name="target_with_source_face.jpg",
                    mime="image/jpeg"
                )

if __name__ == "__main__":
    main()
