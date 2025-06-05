# Função que calcula o valor da parcela mensal, o total pago e o total de juros pagos
def calcular_emprestimo(valor_emprestimo, taxa_juros, prazo_anos):
    # Convertendo a taxa de juros anual para mensal:
    # A taxa de juros mensal é a taxa anual dividida por 100 para transformá-la em valor decimal e depois por 12 (para obter a taxa mensal)
    taxa_juros_mensal = taxa_juros / 100 / 12

    # Calculando o número total de parcelas (em meses)
    # Se o prazo for em anos, multiplicamos por 12 para converter para meses
    numero_parcelas = prazo_anos * 12
    
    # Fórmula de amortização fixa (tabela Price) para calcular o valor da parcela mensal
    # Fórmula: P = V * i * (1 + i)^n / [(1 + i)^n - 1]
    # P = valor da parcela mensal
    # V = valor do empréstimo
    # i = taxa de juros mensal
    # n = número total de parcelas (meses)
    if taxa_juros_mensal > 0:
        # Se a taxa de juros mensal for maior que 0, usamos a fórmula para calcular a parcela mensal
        parcela_mensal = valor_emprestimo * (taxa_juros_mensal * (1 + taxa_juros_mensal)**numero_parcelas) / ((1 + taxa_juros_mensal)**numero_parcelas - 1)
    else:
        # Se a taxa de juros for 0%, a parcela mensal é simplesmente o valor do empréstimo dividido pelo número de parcelas
        parcela_mensal = valor_emprestimo / numero_parcelas
    
    # Calculando o valor total pago durante o empréstimo
    # O valor total pago é o valor da parcela mensal multiplicado pelo número de parcelas
    total_pago = parcela_mensal * numero_parcelas

    # Calculando o total de juros pagos
    # O total de juros pagos é a diferença entre o total pago e o valor original do empréstimo
    total_juros = total_pago - valor_emprestimo
    
    # Retorna os valores calculados: parcela mensal, total pago e total de juros
    return parcela_mensal, total_pago, total_juros

# Função principal que interage com o usuário
def main():
    print("Simulador de Empréstimo")
    
    # Coleta de informações do usuário
    # O valor do empréstimo é solicitado ao usuário e convertido para float para permitir valores decimais
    valor_emprestimo = float(input("Digite o valor do empréstimo (R$): "))
    
    # A taxa de juros anual também é solicitada ao usuário e convertida para float
    taxa_juros = float(input("Digite a taxa de juros anual (%): "))
    
    # O prazo do empréstimo em anos é solicitado ao usuário e convertido para inteiro
    prazo_anos = int(input("Digite o prazo do empréstimo em anos: "))
    
    # Calculando os valores do empréstimo chamando a função que fizemos anteriormente
    parcela_mensal, total_pago, total_juros = calcular_emprestimo(valor_emprestimo, taxa_juros, prazo_anos)
    
    # Exibindo os resultados ao usuário
    # Usamos o formato {:.2f} para mostrar os valores com duas casas decimais
    print(f"\nResultados do empréstimo:")
    print(f"Valor da parcela mensal: R${parcela_mensal:.2f}")
    print(f"Valor total pago após {prazo_anos} anos: R${total_pago:.2f}")
    print(f"Total de juros pagos: R${total_juros:.2f}")

# Este bloco garante que a função main seja chamada quando o programa for executado
if __name__ == "__main__":
    main()
