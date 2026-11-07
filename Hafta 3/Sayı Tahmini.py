import random
say= random.randint(1,100)
n=int(input("Lütfen bir tahmin sayı yazın: "))
while(n!=say):
    if(say<n):
        print("Aşağı in")
        n=int(input("Lütfen bir tahmin sayı yazın: "))
    else:
        print("Yukarı çık")
        n=int(input("Lütfen bir tahmin sayı yazın: "))
print("Tebrikler, Sayıyı buldunuz!")