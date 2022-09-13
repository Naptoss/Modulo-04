A = type(
    'A',
    (),
    {
        'attr': 'Ola Mundo'
    }

)

a = A()
print(a.attr)
