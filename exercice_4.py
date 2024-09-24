c = 6
P = 4 * c
A = c ** 2
b = A > 5 

print(f"Perimetre du carre: {P}")
print(f" Aire du carre: {A}")
print(f"L'aire est-elle superior a 5? {b}")

def perimetre(c):
    P = 4*c
    return P
def surface(c):
    A = c **2
    return A
print("le perimetre est:",perimetre(c))
print("L'air est:", surface(c))
