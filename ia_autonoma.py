import os
import subprocess
import speech_recognition as sr
import google.generativeai as genai
from dotenv import load_dotenv

# Carga la clave desde el archivo .env
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def ejecutar_en_kali(comando):
    try:
        print(f"[*] Ejecutando: {comando}")
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        return resultado
    except Exception as e:
        return f"Error: {str(e)}"

def cerebro_ia():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n>>> IA Activa. Di tu orden...")
        audio = r.listen(source)
    try:
        orden = r.recognize_google(audio, language="es-ES")
        print(f"Comando de voz: {orden}")

        # La IA decide qué hacer
        prompt = f"Eres un agente de Kali Linux. El usuario quiere: '{orden}'. Responde SOLAMENTE con el comando de bash necesario. Sin explicaciones."
        response = model.generate_content(prompt)
        comando_decidido = response.text.strip()

        # Acción en el sistema
        salida = ejecutar_en_kali(comando_decidido)
        print(f"Salida del sistema:\n{salida}")
    except Exception as e:
        print(f"Error en proceso: {e}")

if __name__ == "__main__":
    while True:
        cerebro_ia()
