def palindromo(text):
	text_back = text[::-1]
	if text == text_back:
		return True
	else:
		return False

def letter_count(text):
	text = text.lower()
	letters = {}
	for x in range(len(text)):
		letters[text[x]] = letters.get(text[x],0) + 1
	return letters
    

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
        if (c>=97 and c<=122) or (c>=48 and c<=57) or c==241:
            pass
        else:
            return False
    return True

def back(palabra):
    palabra = eliminar_espacios(palabra,len(palabra))
    palabra1= palabra.lower()
    if len(palabra1) >= 10 and len(palabra1) <= 20 : 
        if caracter_especial(palabra1):
            if palindromo(palabra1):
                return letter_count(palabra)
            else:
                return 3
        else:
            return 2
    else :
        return 1
