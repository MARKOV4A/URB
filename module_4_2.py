def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()

inner_function()
#Выдает ошибку тк функция 'inner_function' определенная только в 'test_function'