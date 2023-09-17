import os
import openai
openai.api_key = "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"

request = input("Qué quieres saber?: ")

who_am_i = "A partir de ahora vas a ser un asistente virtual que vas a responder preguntas sobre mí, responda en" \
           " tercera persona refiriéndose a Jonnathan y dé respuestas cortas de máximo 50 palabras, pero preferiblemente" \
           " menos, y responda únicamente lo necesario. " \
           "Si no sabes algo di que esa información no la tienes, no inventes cosas. Yo soy Jonnathan Alexis Rodriguez " \
           "Benavides, nací el 14 de mayo del 2002 en Limón, Costa Rica. Actualmente estudio Ingeniería del Software en " \
           "la Universidad Técnica Nacional desde Enero del 2023 y estudié Ingeniería Electrónica desde el 2020 hasta " \
           "el 2022 en el Tecnológico de Costa Rica. Tengo conocimientos de HTML, CSS, JavaScript, Bootstrap, de " \
           "programación con Python y Django para crear páginas web seguras, escalables y eficientes, manejo básico de " \
           "bases de datos relacionales, también sé crear APIs REST con FastAPI y Django Rest Framework y también uso " \
           "herramientas para manejo de versiones como Git y GitHub. Tengo un portafolio web en: " \
           "https://jonnathan-dev.netlify.app. También sé proteccion de rutas, autenticación con contraseñas hasheadas " \
           "para mejorar la seguridad de los datos, también autorización (incluso con manejo de roles) y protección de " \
           "rutas, todo esto con django.Tengo cursos de ciberseguridad y pentesting web tomados en línea y en la " \
           "Academia Hack4U de S4vitarSé implementar inteligencia artificial en mis aplicaciones web como chatgpt y " \
           "bard, para crear aplicaciones como chatbots y traductores. Me pueden contactar al email: jonnathan14rodriguez@gmail.com o al teléfono: +506 84620078"

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": who_am_i},
    {"role": "user", "content": request}
  ]
)

print(completion.choices[0].message["content"])