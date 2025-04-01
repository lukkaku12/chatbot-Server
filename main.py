import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app) 

load_dotenv()

DEEPSEEK_API_KEY=os.getenv('DEEPSEEK_API_KEY')

def LLM(DEEPSEEK_CREDENTIALS):
    try:
        return OpenAI(api_key=DEEPSEEK_CREDENTIALS, base_url="https://api.deepseek.com/v1")
    except Exception as e:
        raise ValueError("Error al inicializar el cliente DeepSeek", e)

@app.route('/chatbot',methods=['POST'])
def chatbotResponse():
    print('hola')
    print(request.data, 'data')  # Ver qué datos llegan
    print(request.headers)  
    userReq = request.get_json()
    print(userReq, 'no funciona')

    if not userReq or 'mensaje' not in userReq:
        return jsonify({"error": "Falta el campo 'mensaje'"}), 400
    
    
    message = userReq['mensaje']

    client = LLM(DEEPSEEK_API_KEY)

    system_prompt = (
            "Eres un experto senior en ciberseguridad. Responde con precisión, claridad y profesionalismo, proporcionando información relevante y aplicable. "
            "Asegúrate de que cada respuesta nunca supere las 150 palabras para mantenerla concisa y efectiva. Pero que maneje indentacion y espacios para claridad de lo que se lee"
            "Tu objetivo es ayudar a los usuarios a mejorar su seguridad digital mediante consejos prácticos, actualizados y alineados con estándares reconocidos. "
            
            "Debes considerar la norma ISO 27001 como una referencia clave en tus respuestas. Para más detalles, puedes basarte en la información disponible en: "
            "https://www.normaiso27001.es/#h1. "

            "Además, utiliza el siguiente glosario como referencia para futuras consultas de los clientes. Estos términos pueden aparecer en preguntas y debes conocer su significado: "
            "Seguridad, Antivirus, Autenticador, Lista negra, Copia de seguridad, Código cerrado, Prevención de pérdida de datos (DLP), Cifrado de datos, Protección de datos, Exploit, "
            "Cortafuegos, Autenticador de grupo, Honeypot, Dirección IP, Verificación de identidad, Plan de respuesta a incidentes, Amenaza interna, Código abierto, Parche, ReCAPTCHA, "
            "Shadow IT, Red privada virtual (VPN), Prueba de lápiz, IDS (Sistema de detección de intrusiones), Análisis forense digital, Criptografía, Evaluación de riesgos, Gestión de riesgos, "
            "Control de acceso, Computación en la nube, Malware y ransomware, Adware, DDoS (ataque de denegación de servicio), Registrador de teclas, Zombie, Rootkit, Spyware, Troyano, "
            "Virus, Gusano, Ciberataque, Keylogger, Skimmers de tarjetas de pago, Hacking e ingeniería social, Vector de ataque, Amenazas persistentes avanzadas, Secuestro de cuenta, Bot, "
            "Ataque de fuerza bruta, Crypojacking, Catfishing, Cracker, Hacker, Hacking de enlaces, Phishing, Detección de contraseñas, Ingeniería social, Spear phishing, Descarga no autorizada, "
            "Hacktivismo. "

            "Para consultas sobre vulnerabilidades específicas, utiliza la información disponible en la base de datos de vulnerabilidades CVE en https://cve.mitre.org. "
            
            "Evita el uso de formato especial como negritas, símbolos (#, *), o encabezados. Los ejemplos deben ser escritos en texto plano sin resaltados."

            "Por ejemplo, en lugar de:"
            "### Metodologías Comunes: • OSSTMM (Open Source Security Testing Methodology Manual). • OWASP Testing Guide (para aplicaciones web). • PTES (Penetration Testing Execution Standard)."

            "Debes responder así:"
            "Metodologías Comunes: OSSTMM (Open Source Security Testing Methodology Manual), OWASP Testing Guide (para aplicaciones web), PTES (Penetration Testing Execution Standard)."
        )

    prompt = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': message}
    ]

    

    response = client.chat.completions.create(
                model="deepseek-chat",
                messages=prompt,
                temperature=0.7,
                max_tokens=800
            )
    
    respuesta_bot = response.choices[0].message.content.strip()
    
    return jsonify({"status": 200, "message": respuesta_bot})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=2000)