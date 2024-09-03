"""
Cesar Cipher
--
Created by: Daniel Gómez
Email: dgomez.informatica@gmail.com
"""

def cesar_cipher(letra, mode = "cifrar"):
    dic = {
        'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
        'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
        'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r',
        'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
        'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b',
        'z': 'c'
    }

    # Dicionario inverso para descriptar
    dic_inv = {v: k for k, v in dic.items()}

    if mode == "cifrar":
        return dic.get(letra, letra)
    elif mode == "descifrar":
        return dic_inv.get(letra, letra)
    
    return "Modo no válido"


if __name__ == "__main__":
    texto = input("Ingrese un texto u frase cualquiera: ").lower()

    texto_cifrado = ""
    for letra in texto:
        texto_cifrado += cesar_cipher(letra, mode = "cifrar")

    texto_descifrado = ""
    for letra in texto_cifrado:
        texto_descifrado += cesar_cipher(letra, mode = "descifrar")

    print("Texto cifrado: ", texto_cifrado)
    print("Texto descifrado: ", texto_descifrado)
