A = int(input("Digite um lado: "))
B = int(input("Digite um lado: "))
C = int(input("Digite um lado: "))

if (A + B > C) and (A + C > B) and (B + C > A):

 if A == B and A == C:
  print("Equilátero")

elif (A == B) or (B == C) or (A == C):
    print("Isósceles")

else:
   print("Escaleno")


