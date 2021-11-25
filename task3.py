"""
напишите программу, проводящую вычисление n-го числа ряда Фибоначчи.
"""

def fib(n):
    prev, curr = 0, 1

    for i in range(n+1):
        curr = prev + curr
        prev, curr = curr, prev

    return curr

    
    
if __name__ == '__main__':
   n = int(input())

   print(fib(n))