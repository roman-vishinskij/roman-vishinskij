immutable_var = 1, 2, 'a', 'b'
print("Immutable tuple: " , immutable_var)
#immutable_var[0]= 6
#print(immutable_var) # Изменить НЕЛЬЗЯ -потому что  элементы кортежа не могут быть изменены после того, как они были назначены

mutable_list=[1, 2, 'a', 'b', 'Modified']
print('Mutable: ', mutable_list)
mutable_list [0]= 9
print('Mutable: ', mutable_list)
