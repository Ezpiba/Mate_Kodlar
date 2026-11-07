while True:
    try:
        n=input("Bir sayı girin: ")
        say=float(n)
        
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
    else: 
        break
 
    