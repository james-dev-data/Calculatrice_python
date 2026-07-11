def addition(a,b):      # fonction d'addition
    return a + b
def soustraction(a,b):  # fonction de soustraction
    return a - b
def multiplication(a,b):    # fonction de multiplication 
    return a * b
def division(a,b):      # fonction de division
    if b == 0: # cette condition survient si la valeur du denumerateur est egal à 0
        return "Erreur ! 0 ne peut être diviseur "
    else:
        return a / b
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxieme nombre : "))
operateur = input("choississez le signe (+, -, *, /) : ")

# condition de calcul selon le signe 
if operateur == '+':
    print('resultat : ',addition(a,b))
elif operateur == '-':
    print('resultat : ', soustraction(a,b))
elif operateur == '*':
    print('resultata : ', multiplication(a,b))
elif operateur == '/':
    print('resultat : ', division(a,b))
else:
    print("entrée invalide.")