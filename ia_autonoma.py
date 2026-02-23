import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def ejecutar_en_kali(comando):
    try:
        print(f"[*] IA ejecutando: {comando}")
        # Ejecuta el comando en el sistema y captura la salida
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        return resultado
    except Exception as e:
        return f"Error en la ejecución: {str(e)}"

if __name__ == "__main__":
    print("--- IA AUTÓNOMA KALI (MODO TEXTO ACTIVO) ---")
    while True:
        try:
            # Entrada por teclado para evitar errores de audio (ALSA/JACK)
            orden = input("\n¿Qué orden quieres ejecutar en Kali?: ")
            
            if orden.lower() in ['salir', 'exit', 'quit']:
                break

            # La IA traduce tu texto a un comando de Linux
            prompt = f"Eres un experto en Kali Linux. El usuario quiere: '{orden}'. Responde ÚNICAMENTE con el comando de bash necesario."
            response = model.generate_content(prompt)
            comando_ia = response.text.strip()

            print(f"[+] Comando generado por IA: {comando_ia}")
            
            # Ejecución automática
            salida = ejecutar_en_kali(comando_ia)
            print(f"--- RESULTADO DEL SISTEMA ---\n{salida}")
            
        except Exception as e:
            print(f"Hubo un error en el proceso: {e}")
