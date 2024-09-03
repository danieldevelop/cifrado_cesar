"""
Cesar Cipher
--
Created by: Daniel Gómez
Email: dgomez.informatica@gmail.com
"""

def cesar_cipher(texto, llave):
    """
    Cifra o descrifra un texto usando el algoritmo de Cifrado Cesar
    :param texto: str
    :param llave: int
    :return: str
    """
    resultado = ""
    for i in range(len(texto)):
        char = texto[i]
        if char.isupper():
            resultado += chr((ord(char) + llave - 65) % 26 + 65)
        elif char.islower():
            resultado += chr((ord(char) + llave - 97) % 26 + 97)
        else:
            resultado += char
    return resultado



if __name__ == "__main__":
    texto = input("Ingrese un texto u frase cualquiera: ")
    llave = 3 # Clave de cifrado de desplazamiento

    
    print(f"Texto cifrado: {cesar_cipher(texto, llave)}")
    print(f"Texto descifrado: {cesar_cipher(cesar_cipher(texto, llave), -llave)}")
