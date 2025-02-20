from fastapi import FastAPI
from pydantic import BaseModel
from transformers import MarianMTModel, MarianTokenizer

app = FastAPI()

# Define request format
class TranslationRequest(BaseModel):
    source_lang: str
    target_lang: str
    text: str

# Load model dynamically based on source and target languages
def load_translation_model(source_lang, target_lang):
    model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"
    try:
        tokenizer = MarianTokenizer.from_pretrained(model_name)
        model = MarianMTModel.from_pretrained(model_name)
        return tokenizer, model
    except Exception as e:
        raise ValueError(f"Translation model for {source_lang} to {target_lang} not found. Error: {e}")

# Translation function
def translate_text(source_lang, target_lang, text):
    tokenizer, model = load_translation_model(source_lang, target_lang)
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated_tokens = model.generate(**inputs)
    translated_text = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
    return translated_text

# Define API endpoint
@app.post("/translate/")
async def translate(request: TranslationRequest):
    try:
        translated_text = translate_text(request.source_lang, request.target_lang, request.text)
        return {"translated_text": translated_text}
    except Exception as e:
        return {"error": str(e)}

