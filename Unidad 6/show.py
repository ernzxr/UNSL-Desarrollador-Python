# //////// Ejercicio 16 ////////
print("\nEjercicio 16")

def gen_div(n):
    return (i for i in range(1,n+1) if n%i)

def divisores(n):
    return (i for i in range(1,n+1) if not n%i)

h = gen_div(10)
x = divisores(10)

print(h, x)
print(next(h), next(x))
print(next(h), next(x))
print(next(h), next(x))
print(next(h), next(x))
print(next(h), next(x))
print(next(h), next(x))
