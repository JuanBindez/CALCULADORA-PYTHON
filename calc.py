'''
Author: www.github.com/JuanBindez
Description:
Python Version: 3.10
year: 2022
Local: Brazil
'''

from colors import Color
import time
import os


try:

    def divide():
        try:
            d1 = float(input(Color.AMARELO + "digite o numero para ser  dividido:\n"))
            d2 = float(input("digite o outro numero:\n" + Color.RESET))
            os.system("clear")
            time.sleep(1)
            credits_author()
            print(Color.VERDE + "o resultado é =", d1 / d2)
        except ZeroDivisionError:
            print(Color.VERMELHO + "erro de divisão por 0" + Color.RESET)
        except ValueError:
            os.system("clear")
            print(Color.VERMELHO + "erro, digite apenas numeros, o Python não converte string em float!" + Color.RESET)


    def multi():
        m1 = float(input(Color.AMARELO + "digite o numero para ser multiplicado:\n"))
        m2 = float(input("digite o outro numero:\n" + Color.RESET))
        os.system("clear")
        time.sleep(1)
        credits_author()
        print(Color.VERDE + "o resultado é =", m1 * m2)


    def sub():
        s1 = float(input(Color.AMARELO + "digite o numero para ser subtraido:\n"))
        s2 = float(input("digite o outro numero:\n" + Color.RESET))
        os.system("clear")
        time.sleep(1)
        credits_author()
        print(Color.VERDE + "o resultado é =", s1 - s2)


    def adiciona():
        a1 = float(input(Color.AMARELO + "digite o numero para ser adicionado:\n"))
        a2 = float(input("digite o outro numero:\n" + Color.RESET))
        os.system("clear")
        time.sleep(1)
        credits_author()
        print(Color.VERDE + "o resultado é =", a1 + a2)

    def credits_author():
        print(
                            '''
                            Author: www.github.com/JuanBindez
                            Description:
                            Python Version: 3.10
                            year: 2022
                            Local: Brazil
                            '''
        )

    os.system("clear")
    credits_author()
    print(Color.CYANO + "[1]  dividir digite ")
    print("[2]  multiplicar digite ")
    print("[3]  subtrair digite 3")
    print("[4]  adição digite 4" + Color.RESET)

    numero = int(input(">"))
    os.system("clear")

    match numero:

        case 1:
            divide()
        
        case 2:
            multi()

        case 3:
            sub()

        case 4:
            adiciona()


except KeyboardInterrupt:
    os.system("clear")
    print(Color.VERDE + "obrigado por usar a Calculadora Python!")


