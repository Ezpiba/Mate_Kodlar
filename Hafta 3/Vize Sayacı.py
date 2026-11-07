from datetime import datetime
a= datetime.now()
tara=int (input("Vizenin ayını (sayıyla) yazın: "))
targ= int (input("Vizenin gününü yazın: "))
saat= int (input("Vizenin saatini yazın: "))
c = datetime.now().year
b= datetime(c,tara,targ,saat,0,0)
c= b-a
print("Kalan gün ve saat: ",c)