import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


# Tesseract yo'li (agar Windows bo'lsa kerak)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# Fon rasmi
def set_bg_hack_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://cdn.pixabay.com/photo/2020/06/19/22/33/wormhole-5319067_960_720.jpg");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# Sahifa sozlamasi
st.set_page_config(
    page_title="Risk Management Product - OCR",
    page_icon="🔍",
    layout="wide"
)

# Fonni o'rnatish
set_bg_hack_url()

# Header
st.markdown(
    """
    <div style="
        text-align:center;
        color:white;
        font-size:50px;
        font-weight:bold;
        padding:20px;
        background: rgba(0, 0, 0, 0.6);
        border-radius:15px;
        margin-bottom:20px;">
        🔍 Risk Management Product - OCR
    </div>
    """,
    unsafe_allow_html=True
)

# Fayl yuklash
st.subheader("📥 Upload an Image:")
uploaded_file = st.file_uploader("Upload image file", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    # OCR
    try:
        text = pytesseract.image_to_string(image_np, lang='rus+eng+uzb_cyrl')
    except pytesseract.TesseractError as e:
        st.error(f"OCR Error: {e}")
        text = ""

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🖼️ Uploaded Image:")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("📄 Extracted Text:")

        # Text box
        st.markdown(
            f"""
            <div style="
                background-color: white;
                padding: 10px;
                border-radius: 10px;
                color: black;
                max-height: 1000px;
                overflow-y: auto;
                ">
                {text.replace('\n', '<br>')}
            </div>
            """,
            unsafe_allow_html=True
        )

    # Download tugmasi
    st.download_button(
        label="📥 Download Text as .txt",
        data=text,
        file_name="ocr_result.txt",
        mime="text/plain"
    )
