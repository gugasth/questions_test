def fibonacci(n):
    """
    Verifica se o número n esta na sequência de fibonacci
    Args:
        n (int)

    Returns:
        bool: true se o n estiver na sequencia de efibonacci, false caso não esteja.
    """
    if n < 0:
        return False

    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    
    return a == n

def main():
    try:
        num = int(input("Digite um número: "))
        if fibonacci(num):
            print(f"O número {num} pertence à sequência de fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de fibonacci.")
    except ValueError:
        print("Número inválido.")

if __name__ == "__main__":
    main()