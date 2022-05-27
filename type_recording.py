recording_file = 'file.csv'

def table_format():
    with open (recording_file) as file:
        for num_line, line in enumerate(file):
            num_line = 1 + num_line
            with open('method_table.csv','a') as file:
                if num_line % 4 != 0:
                    file.write(line)
                else:
                    file.write(line)
                    file.write('\n')

def row_format():
    with open (recording_file) as file:
        for num_line, line in enumerate(file):
            num_line = 1 + num_line
            with open('method_line.csv','a') as file:
                if num_line % 4 != 0:
                    a = line.replace('\n',', ')
                    file.write(a)
                else:
                    a = line.strip()
                    file.write(a)
                    file.write('\n')
