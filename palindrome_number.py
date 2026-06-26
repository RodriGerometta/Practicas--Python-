import os

os.system("cls")


def main():
    while True:
        try:
            x = int(input("Ingrese un valor: "))
            break
        except ValueError:
            print("Por favor ingrese un valor valido")
    resultado = isPalindrome(x)
    mostrar(resultado)


def isPalindrome(x):
    if x >= 0:
        y = int(str(x)[::-1])
        if x == y:
            return True
        else:
            return False
    else:
        return False


def mostrar(resultado):
    if resultado == True:
        print("El numero ingresado es un palindromo(Capicua)")
    else:
        print("El numero ingresado no es un palindromo")


if __name__ == "__main__":
    main()
