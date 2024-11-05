def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(b=25)  # Да работает
print_params(c=[1, 2, 3])  # Да работает

values_list = [False, 5, 'Что?']
values_dict = {'a': 'строка', 'b': False, 'c': 4}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [5.5, 6]
print_params(*values_list_2)
