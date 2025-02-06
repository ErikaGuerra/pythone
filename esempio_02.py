numero = int (input( "inserisci un numero: "))
lettera= input ( " inserisci una lettera: ")
for i in range(0,numero):
    print(" " * (numero-i-1)+ lettera * (i*2 + 1 )) 

  