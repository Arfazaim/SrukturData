def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
bilangan = 4
hasil_faktorial = faktorial(bilangan)
print(f"Faktorial dari {bilangan} adalah {hasil_faktorial}")
