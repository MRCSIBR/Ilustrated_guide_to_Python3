def check_object(obj):
    print('Propiedades Objeto')
    print('-----------------')
    print('ID:', id(obj))
    print('Type:', type(obj))
    print('Value:', obj, '\n')

num = 12
check_object(num)

num += 20
check_object(num)
