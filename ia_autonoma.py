import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("[-] Error: No hay clave en el archivo .env")
    exit()

genai.configure(api_key=api_key)
# Usamos gemini-1.5-flash para máxima compatibilidad
model = genai.GenerativeModel('gemini-1.5-flash')

def ejecutar_comando(cmd):
    try:
        print(f"[*] IA ejecutando: {cmd}")
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("\n--- IA KALI ONLINE (TEXTO) ---")
    while True:
        try:
            orden = input("\nOrden: ")
            if orden.lower() in ['exit', 'salir']: break
            
            res = model.generate_content(f"Eres experto en Kali Linux. El usuario quiere: {orden}. Responde SOLO el comando bash.")
            comando = res.text.strip().replace('```bash', '').replace('```', '').strip()
            
            print(ejecutar_comando(comando))
        except Exception as e:
            print(f"Error en proceso: {e}")
