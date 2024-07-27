import streamlit as st
from gtts import gTTS
import tempfile

st.title("Conversor de Texto para Áudio")

# Área de texto para entrada do usuário
texto = st.text_input("Digite o texto que você deseja converter para áudio:", placeholder='Digite o texto aqui!')

if texto:
    # Converter texto em áudio usando gTTS
    tts = gTTS(text=texto, lang='pt-br')
    
    # Criar um arquivo temporário para armazenar o áudio
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    tts.save(temp_file.name)
    
    # Reproduzir o áudio no Streamlit
    audio_file = open(temp_file.name, "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/wav', autoplay=True)
    st.success("Áudio gerado com sucesso!")