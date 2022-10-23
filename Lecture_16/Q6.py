# What will the following code print?
origins = ['Amelia', 'Bill', 'Chris', 'Dina']
for (index, value) in enumerate(origins):
    if(value == 'Bill'):
        print(index, end=' ')
    else:
        print(value, end=' ')

