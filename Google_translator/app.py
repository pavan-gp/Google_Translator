from deep_translator import GoogleTranslator
import streamlit as st


st.title("Google Language Translator Application")
user_input=st.text_input("Enter the text to convert into other languages")
diff_lang=['Kannada','Hindi','Tamil','urdu','Telugu','Marathi','Punjabi','Russian','Ukrainian']
sel_l = st.selectbox("choose language to translate",diff_lang)
d={'Kannada': 'kn' ,'Hindi':'hi','Tamil': 'ta','urdu': 'ur','Telugu': 'te','Marathi':'mr','Punjabi': 'pa',
   'Russian': 'ru','Ukrainian': 'uk'}
target_lang=d[sel_l]
if st.button("Translate"):
    if user_input:
        res = GoogleTranslator(source='en', target=target_lang).translate(user_input)
        st.write(res)
    else:
        st.write("Please provide a text to translate")
