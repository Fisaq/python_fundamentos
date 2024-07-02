# Programa que implementa uma Calculadora

def soma(num1,num2):
    resultado =  num1 + num2
    print(f'\n{num1} + {num2} = {resultado}')

def sub(num1,num2):
    resultado =  num1 - num2
    print(f'\n{num1} - {num2} = {resultado}')

def div(num1,num2):
    resultado =  num1 / num2
    print(f'\n{num1} / {num2} = {resultado}')

def mult(num1,num2):
    resultado =  num1 * num2
    print(f'\n{num1} * {num2} = {resultado}')

def potencia(num1,num2):
    resultado = num1 ** num2
    print(f'\n{num1} ^ {num2} = {resultado}')

def menu():
    
    print('\n-------------------- PYCALC --------------------\n')

    while True:

        print('\nSelecione a operação que deseja realizar:\n')
        print('[1] Somar\n[2] Subtrair\n[3] Dividir\n[4] Multiplicar\n[5] Potenciação')
        op = int(input('\nR: '))

        lista_op = [1, 2, 3, 4, 5]

        if op not in lista_op:
            print('\nOpção inválida, favor selecionar uma opção do menu!')
        else:
            num1 = float(input('\nInforme o primeiro valor: '))
            num2 = float(input('\nInforme o segundo valor: '))
            if op == 1:
                soma(num1,num2)
                break
            elif op == 2:
                sub(num1,num2)
                break
            elif op == 3:
                div(num1,num2)
                break
            elif op == 4:
                mult(num1,num2)
                break
            elif op == 5:
                potencia(num1,num2)
                break

if __name__ == '__main__':
    menu()
