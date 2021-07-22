#Usar a função open
#variavel = open (nome, modo)
'''
modo    função
  r     somente leitura
  w     escrita(caso exista, será apagado eoutro criado)
  a     leitura e escrita(add novo cont ao fim do  arq)
  r+    leitura e escrita
  w+    escrita(caso exista, será apagado eoutro criado)
  a+    leitura e escrita(abre arq para atualização
'''
#LENDO ARQUIVOS usamos 3 funções
'''
read() lê arq inteiros
readline() lê uma linha
readlines() lê arquivos e armazena em uma lista'''

#Criar variável para receber o arquivo
arquivo = open ('exemploParaArquivos.txt')
print(arquivo)#imprime o modo e o nome
print('\n')

#lê arquivos e armazena em uma lista
arquivo = open ('exemploParaArquivos.txt')
lista = arquivo.readlines()
print(lista)
print('\n')
#para imprimir linhas por linha fazer um for
for linha in lista:
     print(linha)
print('\n')

#imprimir tudo de uma vez função read
arquivo = open ('exemploParaArquivos.txt')
texto_completo = arquivo.read()
print(texto_completo)
print('\n')

#função readline
arquivo = open ('exemploParaArquivos.txt')
linha = arquivo.readline()
print(linha)
print('\n')

#Criando arquivo
w = open ('arquivo2','a')
#colocar inf dendro de arquivo2. função write
'''nome do  arq / função /conteúdo '''
w.write('Esse é o meu arquivo\n')
w.close()

