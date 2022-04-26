def palindromo(text):
	text_back = text[::-1]
	if text == text_back:
		print(f"La palabra {text} es palindroma\n")
	else:
		print(f"La palabra {text} no es palindromo (T_T)\n")

def letter_count(text):
	text = text.lower()
	letters = {}
	for x in range(len(text)):
		letters[text[x]] = letters.get(text[x],0) + 1
	print(letters)
	print('\n')

def entrada():
    a = input('Digita la palabra:')
    return a 

def eliminar_espacios(palabra,x):
    i = 0
    for letra in palabra:
        if letra == " ":
            palabra=palabra[:i]+palabra[i+1:]
            i -= 1
        i += 1            
    return palabra

def caracter_especial(palabra):
    for letra in palabra:
        c = ord(letra)
        if (c<97 or c>122) and c!= 241:
            return False
    return True

def main():
    palabra = entrada()
    palabra = eliminar_espacios(palabra,len(palabra))
    palabra1= palabra.lower()
    if caracter_especial(palabra1):
        palindromo(palabra)
        letter_count(palabra)
    else:
        print('El texto contiene  caracteres espciales (T_T)')

if __name__ == "__main__":
    main()