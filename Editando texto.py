# Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase na tela.
frase = 'As rosas são vermelhas.'
print(frase)

# Crie um código que solicite uma frase e depois imprima a frase na tela.
frase = input('Informe uma frase: ')
print(frase)

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras maiúsculas.
frase = input('Informe uma frase: ').upper()
print(frase)

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase digitada mas com todas as letras minúsculas.
frase = input('Informe uma frase: ').lower()
print(frase)

# Crie uma variável chamada “frase” e atribua a ela uma string de sua escolha. Em seguida, imprima a frase sem espaços em branco no início e no fim.
frase = ' Essa época do ano, as flores estão desabroxando. '.strip()
print(frase)

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim.
frase = input('Informe uma frase: ').strip()
print(frase)

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase sem espaços em branco no início e no fim e em letras minúsculas.
frase = input('Informe uma frase: ').strip()
print(frase.lower())

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “e” trocadas pela letra “f”.
frase = input('Informe uma frase: ').strip()
print(frase.replace('e', 'f'))


# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as vogais “a” trocadas pela caractere “@”.
frase = input('Informe uma frase: ')
print(frase.lower().replace('a',chr(64)))

# Crie um código que solicite uma frase à pessoa usuária e imprima a mesma frase com todas as consoantes “s” trocadas pelo caractere “$”.
frase = input('Informe uma frase: ')
print(frase.lower().replace('s',chr(36)))