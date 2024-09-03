# 📎Encriptador y Desencriptador Cesar

Este programa implementa un encriptador y desencriptador utilizando el cifrado Cesar. El cifrado Cesar es un tipo de cifrado por sustitución en el que una letra en el texto original es reemplazada por otra letra que se encuentra un número fijo de posiciones más adelante en el alfabeto. 

Por ejemplo, con un desplazamiento de 3 (Llamado llave u key en el programa) 'A' sería reemplazado por 'D', 'B' se convierte en 'E', y así sucesivamente.

Para encriptar un mensaje, cada letra del mensaje original se desplaza un número fijo de posiciones en el alfabeto. Para desencriptar un mensaje, se desplaza el mismo número de posiciones en el alfabeto, pero en la dirección opuesta.

## 📋 Requerimientos

- [Python 3.x](https://www.python.org/downloads/) - Lenguaje de programación

## 🚀 Instalación

1. Asegúrate de tener Python 3.x instalado en tu computadora.
2. Descargar el archivo cesar_cipher.py en tu computadora.

## 🔧 Implementacion

### 📌 Windows:

1. Abre la línea de comandos (CMD).
2. Navega hasta el directorio donde guardaste el archivo `cesar_cipher.py`.
3. Ejecuta el siguiente comando:

```bash
python cesar_cipher.py
```

### 📌 Linux/Mac:

1. Abre la terminal.
2. Navega hasta el directorio donde guardaste el archivo `cesar_cipher.py`.
3. Ejecuta el siguiente comando:

```bash
python3 cesar_cipher.py
```

## 📝 Notas adicionales

- El programa solo acepta letras del alfabeto inglés, tanto mayúsculas como minúsculas. Cualquier otro carácter (números, símbolos, espacios, etc.) no será encriptado y se mantendrá igual en el mensaje encriptado.