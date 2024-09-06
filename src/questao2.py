def conta_a(s):
    """
    Conta a quantidade de vezes que o caracter 'a' ou 'A' esta na string s

    Args:
        s (str): a string a ser verificada

    Returns:
        bool, int: true/false se teve a, a quantidade de a.
    """
    s = s.lower()
    qnt = s.count('a')
    exists = qnt > 0
    return exists, qnt

def main():
    s = input("Digite uma string: ")
    exists, qnt = conta_a(s)
    
    if exists:
        print(f"A letra 'a' (maiúscula ou minúscula) ocorre {qnt} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

if __name__ == "__main__":
    main()