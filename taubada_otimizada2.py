def tracejado():
    """Imprime uma linha tracejada."""
    print("-" * 50)

def saudacao():
    """Imprime uma mensagem de boas-vindas."""
    print('\n\tOla seja bem vindo a Tabuada Inteligente.')

def obter_nome_usuario():
    """Coleta o nome do usuário."""
    user = input('\n\tQual seu nome? ').title().strip()
    return user

def exibir_mensagem_boas_vindas(user):
    """Exibe uma mensagem de boas-vindas personalizada."""
    print(f'\n\tLegal, {user}.')

def calcular_tabuada():
    """Coleta o número e executa a tabuada."""
    number = int(input("\n\tQual número você gostaria de consultar? "))
    for i in range(1, 11):
        resultado = i * number
        print(f"\n {i} x {number}: {resultado}")

def main():
    """Função principal que organiza a execução do programa."""
    while True:
        tracejado()
        saudacao()

        user = obter_nome_usuario()
        exibir_mensagem_boas_vindas(user)

        calcular_tabuada()

        tracejado()

        continuar = input("\nDeseja consultar outra tabuada? (S/N): ").strip().lower()
        if continuar != 's':
            break

if __name__ == "__main__":
    main()
