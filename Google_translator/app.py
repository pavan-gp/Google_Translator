from deep_translator import GoogleTranslator
import gradio as gr

# ✅ List of supported languages
diff_lang = [
    'Kannada', 'Hindi', 'Tamil', 'Urdu', 'Telugu', 'Marathi', 'Punjabi', 'Russian', 'Ukrainian',
    'Spanish', 'French', 'German', 'Italian', 'Japanese', 'Chinese (Simplified)', 'Chinese (Traditional)',
    'Arabic', 'Portuguese', 'Bengali', 'Malayalam', 'Gujarati', 'Indonesian', 'Korean', 'Turkish', 'Vietnamese'
]

# ✅ Language code dictionary
d = {
    'Kannada': 'kn', 'Hindi': 'hi', 'Tamil': 'ta', 'Urdu': 'ur',
    'Telugu': 'te', 'Marathi': 'mr', 'Punjabi': 'pa',
    'Russian': 'ru', 'Ukrainian': 'uk',
    'Spanish': 'es', 'French': 'fr', 'German': 'de', 'Italian': 'it',
    'Japanese': 'ja', 'Chinese (Simplified)': 'zh-CN', 'Chinese (Traditional)': 'zh-TW',
    'Arabic': 'ar', 'Portuguese': 'pt', 'Bengali': 'bn', 'Malayalam': 'ml',
    'Gujarati': 'gu', 'Indonesian': 'id', 'Korean': 'ko', 'Turkish': 'tr', 'Vietnamese': 'vi'
}

# ✅ Translation function
def translate_text(text, lang):
    if text:
        target_lang = d[lang]
        translated = GoogleTranslator(source='en', target=target_lang).translate(text)
        return translated
    else:
        return "⚠️ Please provide text to translate."

# ✅ Gradio Interface
iface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(
            label="Enter text to translate",
            lines=6,
            placeholder="Type or paste your English text here"
        ),
        gr.Dropdown(
            choices=diff_lang,
            label="Choose language to translate"
        )
    ],
    outputs=gr.Textbox(
        label="Output",
        lines=8,
        interactive=True,
        placeholder="Translation will appear here"
    ),
    title="🌍 Multilingual Translator — Powered by Deep Translator (Google Translate)",
    description="Translate English text into 25 global languages instantly using the Deep Translator library."
)

if __name__ == "__main__":
    iface.launch()

