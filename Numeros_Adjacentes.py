n=int(input("Digite um número inteiro: "))
adj=0

while n:
    first=n%10
    n//=10
    second=n%10
    if first==second:
        adj=1

if adj:
    print("sim")
else:
    print("não")
