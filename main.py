#Captura y validacion de dia
dia = int(input("Ingresa tu dia de nacimiento: "))
while (dia < 1 or dia > 31) :
    print("Error: Ingresa un dia valido")
    dia = int(input("Ingresa tu dia de nacimiento: "))
#Captura y validacion de mes
mes = int(input("Ingresa el numero de tu mes de nacimiento: "))
while (mes < 1 or mes > 12):
    print("Error: Ingresa un mes valido")
    mes = int(input("Ingresa tu mes de nacimiento: "))
#Validacion para meses especificos
while (mes == 2 and (dia > 29 or dia < 1)):
    print("Error: Ingrese un dia valido para el mes dado")
    dia = int(input("Ingresa tu dia de nacimiento: "))
while(mes != 2 and ((mes%2 == 0 and (mes < 8)) or (mes % 2 == 1 and (mes > 8))) and (dia > 30 or dia < 1)):
    print("Erro: Ingresa un dia valido para el mes dado")
    dia = int(input("Ingresa tu dia de nacimiento: "))
#Obtencion del signo zodiacal
if (mes == 1):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Capricornio")
    else:
        print("Tu signo zodiacal es:\n Acuario")
elif (mes == 2):
    if (dia <= 19):
        print("Tu signo zodiacal es:\n Acuario")
    else:
        print("Tu signo zodiacal es:\n Piscis")
elif (mes == 3):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Piscis")
    else:
        print("Tu signo zodiacal es:\n Aries")
elif (mes == 4):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Aries")
    else:
        print("Tu signo zodiacal es:\n Tauro")
elif (mes == 5):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Tauro")
    else:
        print("Tu signo zodiacal es:\n Geminis")
elif (mes == 6):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Geminis")
    else:
        print("Tu signo zodiacal es:\n Cancer")
elif (mes == 7):
    if (dia <= 22):
        print("Tu signo zodiacal es:\n Cancer")
    else:
        print("Tu signo zodiacal es:\n Leo")
elif (mes == 8):
    if (dia <= 22):
        print("Tu signo zodiacal es:\n Leo")
    else:
        print("Tu signo zodiacal es:\n Virgo")
elif (mes == 9):
    if (dia <= 22):
        print("Tu signo zodiacal es:\n Virgo")
    else:
        print("Tu signo zodiacal es:\n Libra")
elif (mes == 10):
    if (dia <= 20):
        print("Tu signo zodiacal es:\n Libra")
    else:
        print("Tu signo zodiacal es:\n Escorpion")
elif (mes == 11):
    if (dia <= 21):
        print("Tu signo zodiacal es:\n Escorpion")
    else:
        print("Tu signo zodiacal es:\n Sagitario")
elif (mes == 12):
    if (dia <= 21):
        print("Tu signo zodiacal es:\n Sagitario")
    else:
        print("Tu signo zodiacal es:\n Capricornio")