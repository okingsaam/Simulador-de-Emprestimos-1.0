def calcular_emprestimo(valor_emprestimo, taxa_juros, prazo_anual) :
    taxa_juros_mensal = taxa_juros / 100 / 12
    numero_parcelas = prazo_anual * 12

    if taxa_juros_mensal > 0 :
        parcela_mensal = valor_emprestimo *( taxa_juros_mensal *(1 + taxa_juros_mensal) ** numero_parcelas) / ((1 + taxa_juros_mensal) ** numero_parcelas - 1)
    else:
        parcela_mensal = valor_emprestimo / numero_parcelas

    total_pago = parcela_mensal * numero_parcelas
    total_juros = total_pago - valor_emprestimo

    return parcela_mensal, total_pago, total_juros
def main():
    print("simulador de emprestimo")

while True:
    valor = float(input("digite o valor do emprestimo (R$): "))
    juros = float(input("digite o valor de juros anual(%): "))
    prazo = int(input("digite o valor do emprestimo em anos: "))

    parcela, total, juros_total = calcular_emprestimo(valor, juros, prazo)

    print("\n---resultado---")
    print(f"parcela mensal: R${parcela:2f}")
    print(f"total pago: R${total:.2f}")
    print(f"total de juros: R${juros_total:.2f}")

    repetir = input("\n deseja fazer outra simulação ? (s/n):").strip().lower()
    if repetir != "s":
        print("encerrando o simulador. até mais !")
        break

if __name__ == "__main__":
    main()