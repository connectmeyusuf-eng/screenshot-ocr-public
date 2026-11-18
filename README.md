# Screenshot OCR

A small Streamlit app for extracting visible text from screenshots with
[Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

## Requirements

- Python 3.10 or later
- The Tesseract OCR executable installed and available on `PATH`

On Windows, install Tesseract OCR from the
[UB Mannheim installer page](https://github.com/UB-Mannheim/tesseract/wiki).

## Run locally

```powershell
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL printed by Streamlit, upload a screenshot, and select
**Extract text**. The extracted text can be copied or downloaded as a `.txt`
file.

The OCR language defaults to `eng`; use installed Tesseract language codes,
such as `eng+fra`, for other languages.

## Deploy to Streamlit Community Cloud

The `packages.txt` file installs Tesseract OCR in the Linux deployment
environment. In Streamlit Community Cloud, create an app from this repository's
`main` branch and select `app.py` as the entry point.

The deployed app has a shareable URL. Screenshots are uploaded to the hosted app
for processing, so users should not upload sensitive images.
