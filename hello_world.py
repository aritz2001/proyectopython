print("Hello world!")
texto = "Hello"
texto2 = "world!"
print(texto + " " + texto2)

numero1 = int(2)
numero2 = int(4)
print(numero1 * numero2)
print(texto + " " + texto2 + " " + str(numero2 / numero1))
#print(int(numero2 / numero1))

frutas = ["platanos", "manzanas","kiwis","peras"]
for x in frutas:
    print(x)

numeroprueba = 4
numeroprueba2 = "3"
resultado = str(numeroprueba) * numeroprueba2
print(resultado)
def function():

    i = 1
    frutas = ["platanos", "manzanas","kiwis","peras", "melocoton"]
    while i < 6:
        for x in frutas:
                print(str(i) + " " + x)
        i += 1	
    numero5 = int(input("Elige un numero5 del 1 al 10: "))
    while numero5 >= 10:
        numero5 = int(input("Elige un numero5 del 1 al 10: "))
    else:
            numero3 = int(input("Elige un numero3 del 1 al 10: " ))
            numero4 = int(input("Elige un numero4 del 1 al 10:" ))
            if numero3 > 10 and numero4 > 10:
                print("Uno de los numeros no es inferior a 10")
            else:
                if numero3 > numero4:
                        print("el tercer numero es mas grande")
                else:
                        print("el cuarto numero es mas grande")   

function()

