def write_surname(data):
    with open ('file.csv', 'a') as file:
        file.write(f'Surname: {data}\n')

def write_name(data):
    with open ('file.csv', 'a') as file:
        file.write(f'Name: {data}\n')

def write_namber(data):
    with open ('file.csv', 'a') as file:
        file.write(f'Namber: {data}\n')

def write_description(data):
    with open ('file.csv', 'a') as file:
        file.write(f'Description: {data}\n')
