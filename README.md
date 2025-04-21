# Documentación del Chatbot de Ciberseguridad

Este documento explica de manera sencilla cómo funciona un chatbot de ciberseguridad desarrollado en Python con Flask, OpenAI y DeepSeek. Está diseñado para que cualquier persona, incluso sin conocimientos técnicos, pueda entenderlo.

---

## Herramientas utilizadas

- **Python**: El lenguaje de programación con el que está construido el bot.
- **Flask**: Un framework para crear la API, que es como la puerta de entrada del chatbot.
- **dotenv**: Sirve para manejar claves secretas de forma segura en un archivo llamado `.env`.
- **CORS**: Permite que el chatbot funcione desde diferentes sitios web o aplicaciones sin problemas.
- **OpenAI / DeepSeek**: Son los motores de inteligencia artificial que generan las respuestas del bot.
- **Twilio (opcional)**: Si se quiere conectar el chatbot con WhatsApp o mensajes SMS.

---

## ¿Para qué sirve este bot?

Este chatbot funciona como un asesor virtual en temas de ciberseguridad. Cuando alguien le hace una pregunta (ya sea desde una página web, una app o WhatsApp), el bot responde de manera clara, precisa y profesional, dando información útil y confiable.

---

## ¿Cómo funciona internamente?

1. El bot está atento a las preguntas que lleguen a la ruta `/chatbot`.
2. Cuando recibe un mensaje, verifica que tenga el campo `mensaje`.
3. Prepara una instrucción especial (llamada `system_prompt`) para que la IA sepa cómo responder.
4. Envía la pregunta del usuario junto con esa instrucción a DeepSeek.
5. Recibe la respuesta de la IA y se la devuelve al usuario.

---

## Partes importantes del código

### `LLM(DEEPSEEK_CREDENTIALS)`

- Configura la conexión con DeepSeek.
- Usa una clave secreta (`DEEPSEEK_API_KEY`) para acceder al servicio.

### `chatbotResponse()`

- Es la función principal que procesa las preguntas.
- Valida los datos, genera la respuesta y la devuelve.
- Tiene instrucciones detalladas para que la IA responda de manera adecuada.

---

## ¿Cómo conectarlo a WhatsApp? (Opcional)

Si se quiere que el chatbot funcione por WhatsApp, se puede usar Twilio. Los pasos son:

1. Crear una cuenta en Twilio ([https://www.twilio.com/](https://www.twilio.com/)).
2. Configurar un número de prueba para WhatsApp.
3. Agregar una función especial en el código para manejar mensajes de WhatsApp:

```python
@app.route('/whatsapp', methods=['POST'])
def whatsappBot():
    mensaje = request.form.get('Body')  # Mensaje que llega por WhatsApp
    respuesta = chatbotResponse(mensaje)
    # Luego, se usa Twilio para enviar la respuesta

```

4.	Configurar el webhook en Twilio para que apunte al servidor del bot (ejemplo: https://tu-servidor.ngrok.io/whatsapp).

### ✉️ ¿Cómo se conecta con Twilio? (Opcional)

Twilio permite recibir mensajes por **WhatsApp o SMS**. Si deseas que este chatbot funcione por WhatsApp, sigue estos pasos:

1. Crea una cuenta en [Twilio](https://www.twilio.com/).
2. Configura un número de prueba para WhatsApp.
3. Crea una función extra como esta:

```python
@app.route('/whatsapp', methods=['POST'])
def whatsappBot():
    incoming_msg = request.form.get('Body')  # Mensaje recibido por WhatsApp
    respuesta = chatbotResponse(incoming_msg)
    # Luego usas Twilio para enviar la respuesta de vuelta
```

4. Configura el **webhook** en Twilio para que apunte a tu servidor Flask:

```
https://tu-servidor.ngrok.io/whatsapp
```

---

### 📊 Ejemplo de uso en la vida real

**Pregunta enviada:**

```json
{
  "mensaje": "¿Qué es un cortafuegos y para qué sirve?"
}
```

**Respuesta esperada:**

```json
{
  "status": 200,
  "message": "Un cortafuegos es un sistema que controla el tráfico de red para permitir o bloquear conexiones según reglas de seguridad. Protege los dispositivos y redes frente a accesos no autorizados."
}
```

---

### ▶️ ¿Cómo lo ejecuto en mi computadora?

1. Tener **Python instalado**.
2. Crear un archivo `.env` con tu clave de DeepSeek:

```
DEEPSEEK_API_KEY=tu_clave_aqui
```

3. Instalar las dependencias necesarias:

```bash
pip install flask python-dotenv flask-cors openai
```

4. Ejecutar el archivo Python:

```bash
python nombre_del_archivo.py
```

5. Probar el chatbot accediendo a:

```
http://localhost:2000/chatbot
```

Puedes usar herramientas como **Postman** o conectar una interfaz de chat.

---

### ✅ Consejos para principiantes

- Revisa bien los nombres de los campos, como `mensaje`.
- Siempre guarda tu clave de API en `.env` y **nunca la publiques**.
- Si algo falla, usa `print()` en el código para depurar.
- Puedes personalizar el comportamiento del bot modificando el `system_prompt`.
- Si conectas Twilio, asegúrate de que tu servidor sea accesible desde internet (puedes usar [ngrok](https://ngrok.com/)).

