numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

par = []
impar = []

for i in range(0, 10) :
    if numeros[i] % 2 == 0 :
        par.insert(i , numeros[i])
    else :
        impar.insert(i , numeros[i])

print("Numeros pares: " + str(par))
print("Numeros impares: " + str(impar))