import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# Forzamos la carga del archivo .env local
load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

# Configuración con la versión de API correcta
genai.configure(api_key=api_key)

# Usamos el modelo flash que es el más estable actualmente
model = genai.GenerativeModel('gemini-1.5-flash')

def ejecutar_comando(cmd):
    try:
        print(f"[*] Ejecutando: {cmd}")
        # Captura la salida del sistema Kali
        return subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
    except Exception as e:
        return f"Error de sistema: {str(e)}"

if __name__ == "__main__":
    print("\n--- IA KALI: SISTEMA LISTO ---")
    if not api_key or api_key == "Tu_Nueva_Clave_Aqui":
        print("[!] ERROR: No has puesto tu clave real en el archivo .env")
    else:
        while True:
            try:
                orden = input("\n¿Qué quieres hacer?: ")
                if orden.lower() in ['salir', 'exit']: break
                
                # Generamos el comando
                response = model.generate_content(f"Eres experto en Kali Linux. El usuario quiere: {orden}. Responde SOLO el comando bash, sin explicaciones ni comillas.")
                comando = response.text.strip().replace('```bash', '').replace('```', '').strip()
                
                print(f"[+] Comando generado: {comando}")
                print(ejecutar_comando(comando))
            except Exception as e:
                print(f"[-] Error de conexión o API: {e}")
