a = '97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx'
files = a.split()

result = list(map(lambda x: '%03d' %
                  int(x.split('.')[0]) + '.' + x.split('.')[1], files))
print(result)

result = list(
    map(lambda x: f'{int(x.split(".")[0]):03d}.{x.split(".")[1]}', files))
