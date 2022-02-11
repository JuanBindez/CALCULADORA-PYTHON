from colors import Color
import time
import os


try:

    def cal():
        print(Color.AMARELO + "calculadora Python!")

    def divide():
        try:
            d1 = float(input(Color.AMARELO + "digite o numero para ser  dividido:\n"))
            d2 = float(input("digite o outro numero:\n" + Color.RESET))
            os.system("clear")
            time.sleep(1)
            cal()
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
        cal()
        print(Color.VERDE + "o resultado é =", m1 * m2)


    def sub():
        s1 = float(input(Color.AMARELO + "digite o numero para ser subtraido:\n"))
        s2 = float(input("digite o outro numero:\n" + Color.RESET))
        os.system("clear")
        time.sleep(1)
        cal()
        print(Color.VERDE + "o resultado é =", s1 - s2)


    def adiciona():
        a1 = float(input(Color.AMARELO + "digite o numero para ser adicionado:\n"))
        a2 = float(input("digite o outro numero:\n" + Color.RESET))
        os.system("clear")
        time.sleep(1)
        cal()
        print(Color.VERDE + "o resultado é =", a1 + a2)

    os.system("clear")
    cal()
    print(Color.CYANO + "para dividir digite 1")
    print("para multiplicar digite 2")
    print("para subtrair digite 3")
    print("para adição digite 4" + Color.RESET)

    y = int(input(":"))
    os.system("clear")

    if y == 1:
        divide()

    if y == 2:
        multi()


    if y == 3:
        sub()


    if y == 4:
        adiciona()
        
except KeyboardInterrupt:
    os.system("clear")
    print(Color.VERDE + "obrigado por usar a Calculadora Python!")



