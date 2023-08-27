n=int(input("Digite um número inteiro: "))
i=2
primo=0

while i<=n:
    if n%i == 0:
        primo+=1
    i+=1

if primo==1:
    print("primo")
else:
    print("não primo")
