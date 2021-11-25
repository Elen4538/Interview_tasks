"""
Напистаь программу на вход число и слова
на выход 1 строка количество уникальных слова
и количество повторения соответственно
"""
def func(n):
    lst1 = []
    for i in range(n):
        lst1.append(str(input()))

    my_dict = {i:str(lst1.count(i)) for i in lst1}
    list_of_dict_values = list(my_dict.values())   
    fin =set(lst1)
    print(len(fin))
    print(my_dict)
    print(','.join(list_of_dict_values))
        
 
if __name__ == '__main__':
   n = int(input())
   func(n)