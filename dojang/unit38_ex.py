try:
    file = open('maria.txt', 'r')
except:
    print('No File')
else:
    s = file.read()
    file.close()
