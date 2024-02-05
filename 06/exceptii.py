my_var = input("Adauga un nr: ")
try:
    variabila
    my_int = int(my_var)
    print(my_int)
except ValueError:
    print("Ai introdus un string in locul intregului")
    variabila1 = 3
    print(variabila1)
except NameError:
    print("Nu ai declarat variabila")
    variabila1 = 5
except Exception as e:
    print('Exceptie generala', type(e).__name__)
# except ValueError:
#     print("Ai introdus un string in locul intregului")
else:
    print("A functionat")
finally:
    print('se executa oricand')
# print('oricum', variabila1)
print('oricum', my_int)