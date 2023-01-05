# Meu primeiro projeto em python.3.0 :)
# Discord: Jhon Markheze#5879
# Instagram: 
import time

while True:
    try:
        c1 = input('Crie um usuario: ')
        c2 = input('Crie uma senha: ')

        c3 = input('Digite seu usuario: ')
        c4 = input('Digite sua senha: ')

        if c3 == c1 and c4 == c2:
            print('Login efetuado com sucesso!!')
            time.sleep(5)
            exit()
        else:
            print('[X] Usuario ou senha incorretos! ')
            time.sleep(5)
    except:
        break
