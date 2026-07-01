"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""
import os
os.system("cls")

symbols = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

def main():
    while True:
        try:
            roman_number = str(input("Ingrese un numero romano que quiera convertir a numeros enteros: ")).upper()
            break
        except ValueError:
            print("Por favor ingrese numeros romanos (En letras): ")
         
    print(f"Numero romano ingresado: {roman_number}")
    roman_to_integer(roman_number)
        
def roman_to_integer(roman_number):
    valores_lista = []
    for i, s in enumerate(roman_number):
        if s in symbols:
            valores_lista.append(symbols[s])
    print (f"Numeros pasados a Integer: {valores_lista}")
    
    calcular(valores_lista) 

def calcular(valores_lista):
    last_roman_number = valores_lista[-1]
    print(f"Ultimo numero: {last_roman_number}")
    resultado = 0
    for i in range(len(valores_lista) - 1):
        print(f"#{i}: {resultado}")
        if valores_lista[i] < valores_lista[i+1]:
            resultado -= valores_lista[i]
        else:
            resultado += valores_lista[i]
    
    print(f"Numero antes de sumar el ultimo numero: {resultado}")
    resultado += last_roman_number        
    print(f"Resultado final: {resultado}")

main()
    
        