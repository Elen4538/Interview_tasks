"""
на вход - ввод положительного числа от 1 до 9 включительно
выводит построчно треугольник высотой n-1
4444
333
22
1
"""

def triangle(n):
    ar = [0]

    for j in range(n,0,-1):
        print(str(j)*j)
    

if __name__ == '__main__':
   n = int(input())

   triangle(n)