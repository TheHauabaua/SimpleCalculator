
# Dodawanie
def Dodawanie(n1, n2):
    return n1 + n2

# Odejmowanie
def Odejmowanie(n1, n2):
    return n1 - n2

# Mnożenie
def Mnożenie(n1, n2):
    return n1 * n2

# Dzielenie
def Dzielenie(n1, n2):
    return n1 / n2


print("Wybierz Opcję")
print(
    "1. Dodawanie\n"
    "2. Odejmowanie\n"
    "3. Mnożenie\n"
    "4. Dzielenie\n")


operation = int(input("Wybieram: "))

n1 = float(input("Wprowadź pierwszą liczbę: "))
n2 = float(input("Wprowadź drugą liczbę: "))

if operation == 1:
    print (n1, "+", n2, "=", Dodawanie(n1, n2))

elif operation == 2:
    print (n1, "-", n2, "=", Odejmowanie(n1, n2)) 

elif operation == 3:
    print (n1, "*", n2, "=", Mnożenie(n1, n2)) 
    
elif operation == 4:
    print (n1, "/", n2, "=", Dzielenie(n1, n2)) 
    
else:
    print("Wprowadzono błędne dane!")