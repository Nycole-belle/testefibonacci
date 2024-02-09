def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def is_in_fibonacci(n):
    fib_sequence = fibonacci_sequence(n)
    if n in fib_sequence:
        return True
    else:
        return False

numero = int(input("Digite um número: "))

if is_in_fibonacci(numero):
    print(f"{numero} pertence à sequência Fibonacci.")
else:
    print(f"{numero} não pertence à sequência Fibonacci.")