def calcular_emprestimo(valor_emprestimo, taxa_juros, Prazo_anos):
    pass
def main():
    pass
if __name__=="main_":
    main()
def calcular_emprestimo(valor_emprestimo, taxa_juros, prazo_anos):
    taxa_juros_mensal = taxa_juros / 100 / 12
    numero_parcelas = prazo_anos * 12
    if  taxa_juros_mensal > 0 :
        taxa_juros_mensal = valor_emprestimo * (
            taxa_juros_mensal * (1 + taxa_juros_mensal)** numero_parcelas  / (1 + taxa_juros_mensal)**numero_parcelas -1)
    else: 
        parcelas_mensais = valor_emprestimo / numero_parcelas

    total_pago = parcelas_mensais * numero_parcelas
    total_juros = total_pago - valor_emprestimo
    
    return parcelas_mensais, total_pago, total_juros

def calcular_emprestimo(valor_emprestimo, taxa_juros, Prazo_anos):
    taxa_juros_mensal = taxa_juros / 100 / 12
    numero_parcelas = Prazo_anos * 12

    def calcular_emprestimo(valor_emprestimo, taxa_juros, prazo_anos):
        taxa_juros_mensal = taxa_juros / 100 / 12
    numero_parcelas = Prazo_anos * 12
    
    if taxa_juros_mensal > 0:
        parcela_mensal = valor_emprestimo * (
            taxa_juros_mensal * (1 + taxa_juros_mensal)**numero_parcelas
        ) / (
            (1 + taxa_juros_mensal)**numero_parcelas - 1
        )
    else:
        parcela_mensal = valor_emprestimo / numero_parcelas
    total_pago = parcela_mensal * numero_parcelas
    total_juros = total_pago - valor_emprestimo

    return parcela_mensal, total_pago, total_juros

def main():
    print("Simulador de Empréstimo")
    valor = float(input("Digite o valor do empréstimo (R$): "))
    juros = float(input("Digite a taxa de juros anual (%): "))
    prazo = int(input("Digite o prazo do empréstimo em anos: "))

    parcela, total, juros_total = calcular_emprestimo(valor, juros, prazo)

    print("\n--- Resultado ---")
    print(f"Parcela mensal: R${parcela:.2f}")
    print(f"Total pago: R${total:.2f}")
    print(f"Total de juros: R${juros_total:.2f}")


if __name__ == "__main__":
    main()