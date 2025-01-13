import os
import pyaes

## Abrir o arquivo criptografado
file_name = "teste.txt.ransomwaretroll" 
file = open(file_name, "rb") ## Abrr o arquivo
file_data = file.read() ## Ler o arquivo
file.close() ## Fechar o arquivo

## Chave para descriptografia

key = b"testeransomwares" ## Chave com 16 caracteres
aes = pyaes.AESModeOfOperationCTR(key) ## Funcao para descriptografar usando a chave
decrypt_data = aes.decrypt(file_data)

## Remover o arquivo criptografado

os.remove(file_name)

## Criar o arquivo descriptografado

new_file = "teste.txt" ## Criar um novo arquivo
new_file = open(f'{new_file}', "wb") ## Abrir o arquivo
new_file.write(decrypt_data) ## Descriptografa o arquivo
new_file.close() ## Fechar o arquivo
