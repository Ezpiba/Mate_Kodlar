dogum_yil= int(input("Doğum yılınızı yazın."))
a=2026-dogum_yil
if(a<18):
    b=18-a
    print(a,"yaşındasınız.Ehliyet alamazsınız.",b,"yıl bekleyin")
elif(a>=18):
     print(a,"yaşındasınız.Ehliyet alabilirsiniz.")
