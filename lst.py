def my_list(ls):
    ls1 = [el * (-1) if 3 <= el <= 8 else el for el in ls]
    return ls1
     
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list(ls))