def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
bilangan = 4
hasil_fibonacci = fibonacci(bilangan)
print(f"Deret Fibonacci ke-{bilangan} adalah {hasil_fibonacci}")
