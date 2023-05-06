#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит
#число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8

def exponentiation (number, degree):
  if degree == 1:
    return number
  if degree == 0:
    return 1
  return number*exponentiation (number, degree-1)

use_number = int(input("Enter your number, please: "))
use_degree = int(input("Enter degree of the number, please: "))
print(exponentiation(use_number, use_degree))