vendedores = []

for n in range (2):
    print(f'Vendedor {n + 1}')
    nome = input('Digite o nome: ')

    vendas = []
    for i in range(2):
        venda = float(input(f'Digite o valor{i + 1}: '))
        vendas.append(venda)

    media = sum(vendas) / len(vendas)
    total = sum(vendas)
    print(media)
    print(total)

    vendedor = {
        'Nome': nome,
        'Vendas': vendas,
        'Media': media

    }

    vendedores.append(vendedor)

for emp in vendedores:
    print(f'\nNome: {emp["Nome"]} \nVendas: {emp["Vendas"]} \nMedia: {emp["Media"]}')
    
