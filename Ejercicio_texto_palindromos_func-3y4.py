def palindromo(text):
	text_back = text[::-1]
	if text == text_back:
		print("El texto es palindromo\n")
	else:
		print("El texto no es palindromo\n")

def letter_count(text):
	text = text.lower()
	letters = {}
	for x in range(len(text)):
		letters[text[x]] = letters.get(text[x],0) + 1
	print(letters)
	print('\n')




if __name__ == "__main__":
    while True:
    	text = input('Ingrese el texto:\n')
    	palindromo(text)
    	letter_count(text)