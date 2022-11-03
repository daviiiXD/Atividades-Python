letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
quantidade = 0
for i in letras :
    if i not in "a,e,i,o,u" :
        print(i)
        quantidade += 1

print(quantidade)