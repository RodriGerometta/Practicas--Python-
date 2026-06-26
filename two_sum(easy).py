'''
Dado un array de enteros nums y un entero target, devuelve los índices de los dos números de tal manera que sumentarget .

Puede suponer que cada entrada tendrá exactamente una solución y que no puede utilizar el mismo elemento dos veces.

Puedes devolver la respuesta en cualquier orden.

Ejemplo 1:
Entrada: nums = [2,7,11,15], objetivo = 9
 Salida: [0,1]
 Explicación: Como nums[0] + nums[1] == 9, devolvemos [0, 1].
 
Ejemplo 2:
Entrada: nums = [3,2,4], objetivo = 6
 Salida: [1,2]
Ejemplo 3:

Entrada: nums = [3,3], objetivo = 6
 Salida: [0,1]
''' 

from typing import List
import os
os.system("cls")

nums = [2,7,11,15]
target = 30

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Escribe tu código aquí
        vistos = {}
        
        for i, num in enumerate(nums):
            numero = target - num
            
            if numero in vistos:
                 # Devolvemos el índice guardado y el índice actual en una list
                return [vistos[numero], i]
            
            # Si no está, guardamos el número actual con su índice
            vistos[num] = i
    
sol = Solution()    
resultado = sol.twoSum(nums, target)
print(resultado)