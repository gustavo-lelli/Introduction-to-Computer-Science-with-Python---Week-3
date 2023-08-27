n=int(input("Digite o valor de n: "))

if n==0:
    print("1")
else:
    i=n-1
    
    while i>0:
        n*=i
        i-=1

    print(n)
