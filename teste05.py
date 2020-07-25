from time import sleep

resposta = 'SN'
while True:
    a = int(input('Entre com um número:'))

    b = int(input('Entre com um número:'))

    c = int(input('Entre com um número:'))
    print('-' * 40)
    print('-' * 40)
    print("Cal\n")
    sleep(1)
    print("cu\n")
    sleep(1)
    print("lando!!!\n")
    if a > b and a>c:
        print('O primeiro número é o maior')
    elif b>a and b > c:
        print('O segundo número é o maior')
    else:
        print('O terceiro é o maior número')



    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    while resposta not in "SN":
        resposta = str(input("ERRO! Responda apenas S ou N ")).strip().upper()[0]
    if resposta == "N":
     break
print('-' * 40)
print('-' * 40)
