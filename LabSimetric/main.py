def c_cesar(message,displacement):
    result = ''
    for letter in message:
        if letter.isalpha():
            displacement_ascii = 65 if letter.isupper() else 97
            c_letter = chr((ord(letter) - displacement_ascii + displacement) % 26 + displacement_ascii)
            result += c_letter
        else:
            result += letter
    return result

def d_cesar(message,displacement):
    return c_cesar(message,-displacement)

word = input("\nPALABRA A CIFRAR: ")
displacement = int(input("NUMERO DE DESPLAZAMIENTO: "))
print("Cifrado Cesar: " + c_cesar(word,displacement))
print("Descifrado Cesar: " + d_cesar(c_cesar(word,displacement),displacement))

def c_atbash(message):
    result = ''
    for letter in message.upper():
        if letter.isalpha():
            result += chr(90 - ord(letter) + 65)
    return result

word = input("\nPALABRA A CIFRAR: ")
print("Cifrado Atbash: " + c_atbash(word))
print("Descifrado Atbash: " + c_atbash(c_atbash(word)))

def create_matrix(dkey):
    dkey = "".join(sorted(set(dkey.upper()),key=dkey.index))
    abc = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    for letter in dkey + abc:
        if letter not in matrix:
            matrix.append(letter)
    return [matrix[i:i+5] for i in range(0,25,5)]

def find_pos(matrix, letter):
    for i, j in enumerate(matrix):
        if letter in j:
            return i, j.index(letter)
    return None

def prepare_message(message):
    message = message.upper().replace("J", "I").replace(" ", "")
    prepared = ""
    i = 0
    while i < len(message):
        prepared += message[i]
        if i + 1 < len(message) and message[i] == message[i + 1]:
            prepared += 'X'
        elif i + 1 < len(message):
            prepared += message[i + 1]
            i += 1
        i += 1
    if len(prepared) % 2 != 0:
        prepared += 'X'
    return prepared

def c_playfair(message, dkey):
    matrix = create_matrix(dkey)
    message = prepare_message(message)
    result = ""
    for i in range(0, len(message), 2):
        letter1, letter2 = message[i], message[i + 1]
        i1, j1 = find_pos(matrix, letter1)
        i2, j2 = find_pos(matrix, letter2)
        if i1 == i2:
            result += matrix[i1][(j1 + 1) % 5]
            result += matrix[i2][(j2 + 1) % 5]
        elif j1 == j2:
            result += matrix[(i1 + 1) % 5][j1]
            result += matrix[(i2 + 1) % 5][j2]
        else:
            result += matrix[i1][j2]
            result += matrix[i2][j1]
    return result

word = input("\nPALABRA A CIFRAR: ")
key = input("PALABRA CLAVE: ")
print("Cifrado Playfair: " + c_playfair(word,key))

def c_polybios(message):
    abc ='ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix = {abc [i]: (i // 5 + 1, i % 5 + 1) for i in range(len(abc))}
    result = ''
    for letter in message.upper():
        if letter in matrix:
            i, j = matrix[letter]
            result += str(i) + str(j)
        else:
            result += letter
    return result

def d_polybios(message):
    abc = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    matrix_inverse = {(i // 5 + 1, i % 5 + 1): abc[i] for i in range(len(abc))}
    result = ''
    i = 0
    while i < len(message):
        if message[i].isdigit() and message[i + 1].isdigit():
            j = int(message[i])
            k = int(message[i + 1])
            letra = matrix_inverse.get((j, k), '')
            result += letra
            i += 2
        else:
            result += message[i]
            i += 1
    return result

word = input("\nPALABRA A CIFRAR: ")
print("Cifrado Polybios: " + c_polybios(word))
print("Descifrado Polybios: " + d_polybios(c_polybios(word)))

def c_amsco(message, key):
    blocks = []
    altern = True
    i = 0
    while i < len(message):
        tamanio = 1 if altern else 2
        blocks.append(message[i:i+tamanio])
        i += tamanio
        altern = not altern
    reorganizeds = [''] * len(blocks)
    for index, char in enumerate(key):
        if index < len(blocks):
            reorganizeds[char] = blocks[index]
    return ''.join(reorganizeds)

word = input("\nPALABRA A CIFRAR: ")
key = input("PALABRA CLAVE: ")
print("Cifrado Amsco: " + c_amsco(word,key))
