# Vamos declarar uma lista
from typing import overload


nomes = [
    'Edson',
    'Renata',
    'Eric',
    'Henrique'
]

dados = ['Edson', 50, 12.67, True]

#Mostrando o conteúdo de uma lista
print(nomes)
print(dados)

#As listas possuem índices , iniciando em zero (0)
#      0     1     2    3
dados = ['Edson', 50, 12.67, True]
print(dados[0])
print(dados[1])
print(dados[2])
print(dados[3])

#Percorrendo (Laço) uma lista
#Primeira forma

for nome in nomes: #in = dentro ou pertence ou contido
    print(nome)

# Ex com Números
numeros = [1, 2, 3, 4, 5, 6]
for numero in numeros:
    print(numero)

dados = ['Edson', 50, 12.67, True]
   
for item in dados:
    print(item, type(item))

    # Somar os valores de uma lista
dados = ['Edson', 50, 12.67, True]

soma = 0
for valor in dados:
    if type(valor) == int or type(valor) == float:
        soma += float(valor)
print(soma)

#Percorrer é a mesma coisa que "iterar"
#vamis ver como sabemos qual é o índice eo valor de item em uma lista 

for indice, valor in enumerate(dados):
    print(indice, valor)

#Desafio 
#Utilizando a lista abaixo, mostre apenas os valores nos índices ímpares
#            0                 1            2               3            4             5
lista = ['Tio Patinhas', 'Zé colméia', 'Zeca Urubú', 'Pato Donalds', 'Gaguinho', 'Zé Carioca']
for indice, item in enumerate(lista):
    if indice % 2 != 0:
     print(indice, item)

     #Operações com Listas
     #* Adição: 'Append(value)'
     #* Adição localizada: 'Insert(index, value)'
     #*Remoção: 'remove(value)
     #*contagem de itens: 'conunt(value)
     

unidades = ['Vergueiro', 'Vila Maria', 'Memorial']
#adicionando um elemnto na lista com append() - insere no final da lista
unidades.append('Santo Amaro')
print(unidades)

#adicionando com insert()
unidades.insert(1, 'Vila Prudente')
print(unidades)

#remover um elemento da lista
unidades.remove('Santo Amaro')
print(unidades)

#remover com pop() - remove pelo índice
unidades.pop(2)
print(unidades)

#contando itens de uma lista - conunt()
#Verifica a recorrência de determinado item
unidades.count('Vila Maria')

#tamanho de uma lista 
len(unidades)

#ordenar - crescente 
unidades.sort()
unidades

#ordenar decrescente
unidades.reverse()
unidades 

#cuidado...
valores = [-1, 29, 19, 48, -12]

# Z-A
valores.reverse()
print(valores)

#Os valores foram apenas invertidos e não ordenados 

#Dada a lista abaixo, remover "todos" os valores iguais a 38

valores = [38, 38, 25, 27, 38, 25, 26, -12, -3]
valores = [38, 38, 25, 27, 38, 25, 26, -12, -3]
while True:
  for i in valores:
    if i == 38:
      valores.remove(i)
  if valores.count(38) == 0:
     break
print(valores)


# Resolvendo com comandando set() - remove todos, mantendo apenas um
valores = [38, 38, 25, 27, 38, 25, 26, -12, -3]
print(set(valores))

#tentem implementar depois com o set()

#Vamos resolver de maneira inteligente e sem esforço

valores = [38, 38, 25, 27, 38, 25, 26, -12, -3]
valores_novos = []
for valor in valores:
    if valor != 38:
        valores_novos.append(valor)

        print(valores_novos)

# Pertencimento (está contido)
unidades = ['Vergueiro', 'Vila Maria', 'Memorial']
print('Vergueiro' in unidades)
print('Tatuapé' not in unidades)
print('Tatuapé' in unidades)

#Fatiamento de listas
# Cuidado: o intervalo não é inclusivo

#           0              1          2             3
aves = ['Andorinha', 'Pica-Pau', 'Beija-Flor', 'Canário']

print(aves[1:3])
print(aves[0:2])

# Manipular o deslocamento dos ":"
aves[::3]

aves[2:len(aves)-1]
