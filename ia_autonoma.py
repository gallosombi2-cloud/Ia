import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# Cargar configuración
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: No se encontró la GEMINI_API_KEY en el archivo .env")
    exit()

genai.configure(api_key=api_key)

# Usamos la versión estable más reciente
model = genai.GenerativeModel('gemini-1.5-flash')

def ejecutar_en_kali(comando):
    try:
        print(f"[*] Ejecutando en sistema: {comando}")
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        return resultado
    except Exception as e:
        return f"Error en ejecución: {str(e)}"

if __name__ == "__main__":
    print("\n--- IA AUTÓNOMA KALI (MODO TEXTO) ---")
    while True:
        try:
            orden = input("\n¿Qué orden quieres ejecutar?: ")
            if orden.lower() in ['salir', 'exit']: break

            # Generar respuesta
            response = model.generate_content(f"Eres un experto en Kali Linux. El usuario quiere: '{orden}'. Responde solo con el comando bash.")
            
            # Limpiar el comando de caracteres extraños
            comando_ia = response.text.strip().replace('```bash', '').replace('```', '').strip()

            print(f"[+] Comando generado: {comando_ia}")
            salida = ejecutar_en_kali(comando_ia)
            print(f"--- RESULTADO ---\n{salida}")
            
        except Exception as e:
            print(f"Hubo un error en el proceso: {e}")
