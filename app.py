import streamlit as st
import requests

# FastAPI backend URL
FASTAPI_URL = "http://127.0.0.1:8000/translate/"

# Language mapping for full names
LANGUAGE_MAP = {
    "Auto Detect": "auto",
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Russian": "ru",
    "Dutch": "nl",
    "Polish": "pl"
}

# Streamlit UI setup
st.set_page_config(page_title="Language Translator", page_icon="🌍", layout="wide")

# Custom CSS for better contrast & styling
st.markdown(
    """
    <style>
    .stTextArea textarea { font-size: 16px; }
    .stButton button { background-color: #4CAF50; color: white; font-size: 16px; }
    .output-box {
        background-color: #222;
        color: #fff;
        padding: 15px;
        border-radius: 5px;
        font-size: 20px;
        min-height: 200px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.title("🌍 Language Translator")

# Create two columns (side-by-side layout)
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📝 Input Text")
    source_lang_name = st.selectbox("🌐 Source Language", LANGUAGE_MAP.keys(), index=1)
    text_to_translate = st.text_area("✍️ Enter text here", "", height=200)

with col2:
    st.markdown("### 🔍 Translated Text")
    target_lang_name = st.selectbox("🎯 Target Language", list(LANGUAGE_MAP.keys())[1:], index=1)
    translated_text_placeholder = st.empty()  # Placeholder for translated text

# Translate button (spanning both columns)
if st.button("🔄 Translate", use_container_width=True):
    if text_to_translate.strip():
        # Convert language names to codes
        source_lang = LANGUAGE_MAP[source_lang_name]
        target_lang = LANGUAGE_MAP[target_lang_name]

        # Auto-detect fallback (default to English if not supported)
        if source_lang == "auto":
            source_lang = "en"

        request_data = {
            "source_lang": source_lang,
            "target_lang": target_lang,
            "text": text_to_translate
        }

        try:
            response = requests.post(FASTAPI_URL, json=request_data)
            result = response.json()
            if "translated_text" in result:
                translated_text_placeholder.markdown(
                    f'<div class="output-box">{result["translated_text"]}</div>', unsafe_allow_html=True
                )
            else:
                translated_text_placeholder.markdown(
                    '<div class="output-box">❌ Error: Translation failed</div>', unsafe_allow_html=True
                )
        except Exception as e:
            translated_text_placeholder.markdown(
                f'<div class="output-box">⚠️ API request failed: {str(e)}</div>', unsafe_allow_html=True
            )
    else:
        st.warning("⚠️ Please enter some text to translate.")
