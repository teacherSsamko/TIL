def file_read():
    with open('unit40.words.txt') as file:
        while True:
            line = file.readline()
            if line == '':
                break

            yield line.rstrip('\n')


for i in file_read():
    print(i)
