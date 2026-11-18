#!/usr/bin/env python3
"""Simple web interface for extracting text from screenshots."""

import hashlib
import shutil
from pathlib import Path

import pytesseract
import streamlit as st
from PIL import Image, UnidentifiedImageError


if not shutil.which("tesseract"):
    tesseract_path = Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe")
    if tesseract_path.is_file():
        pytesseract.pytesseract.tesseract_cmd = str(tesseract_path)


st.set_page_config(page_title="Screenshot OCR", page_icon=":mag:")
st.title("Screenshot OCR")
st.write("Upload a screenshot and extract its visible text.")
st.caption(
    "Screenshots are uploaded to this app for processing. Avoid uploading sensitive images."
)

uploaded_file = st.file_uploader(
    "Choose a screenshot",
    type=["png", "jpg", "jpeg", "bmp", "tif", "tiff", "webp"],
)
language = st.text_input("OCR language", value="eng", help="For example: eng or eng+fra")

if uploaded_file is not None:
    image_bytes = uploaded_file.getvalue()
    result_key = hashlib.sha256(image_bytes + language.encode("utf-8")).hexdigest()

    try:
        image = Image.open(uploaded_file)
        image.load()
        st.image(image, caption=uploaded_file.name, use_container_width=True)
    except (UnidentifiedImageError, OSError) as error:
        st.error("Could not read the uploaded image: {}".format(error))
    else:
        if st.button("Extract text", type="primary"):
            try:
                text = pytesseract.image_to_string(image, lang=language)
            except pytesseract.TesseractNotFoundError:
                st.error(
                    "Tesseract OCR was not found. Install it and ensure it is available on PATH."
                )
            except pytesseract.TesseractError as error:
                st.error("OCR failed: {}".format(error))
            else:
                st.session_state["ocr_result"] = (result_key, text)

        result = st.session_state.get("ocr_result")
        if result is not None and result[0] == result_key:
            st.subheader("Extracted text")
            st.text_area(
                "OCR result",
                value=result[1],
                height=240,
                label_visibility="collapsed",
            )
            st.download_button(
                "Download text",
                data=result[1],
                file_name="extracted_text.txt",
                mime="text/plain",
            )
