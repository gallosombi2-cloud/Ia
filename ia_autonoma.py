import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

# Configuración inicial
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Usamos gemini-1.5-flash para evitar el error 404 de modelos antiguos
model = genai.GenerativeModel('gemini-1.5-flash')

def ejecutar_en_kali(comando):
    try:
        print(f"[*] IA ejecutando: {comando}")
        resultado = subprocess.check_output(comando, shell=True, stderr=subprocess.STDOUT, text=True)
        return resultado
    except Exception as e:
        return f"Error en la ejecución: {str(e)}"

if __name__ == "__main__":
    print("\n--- IA AUTÓNOMA KALI (MODO TEXTO ACTIVO) ---")
    while True:
        try:
            orden = input("\n¿Qué orden quieres ejecutar en Kali?: ")
            
            if orden.lower() in ['salir', 'exit', 'quit']:
                break

            prompt = f"Eres un experto en Kali Linux. El usuario quiere: '{orden}'. Responde ÚNICAMENTE con el comando de bash necesario."
            response = model.generate_content(prompt)
            comando_ia = response.text.strip()

            # Limpiamos el comando de posibles comillas de Markdown
            comando_ia = comando_ia.replace('```bash', '').replace('```', '').strip()

            print(f"[+] Comando generado: {comando_ia}")
            salida = ejecutar_en_kali(comando_ia)
            print(f"--- RESULTADO ---\n{salida}")
            
        except Exception as e:
            print(f"Hubo un error en el proceso: {e}")
