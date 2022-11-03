linha = open('arquivos2/arquivos.txt', 'w+')
linha.write('Davi\n')
linha.write('teste\n')
linha.write('HEHE\n')

linha.seek(0)
for i in linha.readlines() :
     print(i[:-1])