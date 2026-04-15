def gerar_relatorio(nome, cpf, email, endereco, valor_material, mao, forma_pagamento, quantidades):
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:

        # TÍTULO
        arquivo.write("RELATÓRIO DE ORÇAMENTO\n\n")

        # DADOS DO CLIENTE
        arquivo.write(f"Nome: {nome}\n")
        arquivo.write(f"CPF: {cpf}\n")
        arquivo.write(f"Email: {email}\n")
        arquivo.write(f"Endereço: {endereco}\n\n")

        # PRODUTOS
        arquivo.write("PRODUTOS:\n")
        for item, quantidade in quantidades.items():
            arquivo.write(f"{item}: {quantidade}\n")

        arquivo.write("\n")

        # VALORES
        arquivo.write(f"Valor material: R$ {valor_material:.2f}\n")
        arquivo.write(f"Mão de obra: R$ {mao:.2f}\n")
        arquivo.write(f"Total: R$ {valor_material + mao:.2f}\n")

        # PAGAMENTO
        arquivo.write(f"Pagamento: {forma_pagamento}\n")


# 👇 AQUI VOCÊ CRIA OS DADOS (isso que faltava)

quantidades = {
    'piso': 10,
    'rodape': 15,
    'cola_piso': 2,
    'cola_rodape': 1,
    'nivela': 3,
    'prime': 1,
    'selante': 2
}


#  CHAMADA DA FUNÇÃO

gerar_relatorio(
    "João",
    "12345678900",
    "joao@email.com",
    "Rua A, 123",
    3000.00,
    1200.00,
    "À vista",
    quantidades
)

print("Relatório criado com sucesso.")