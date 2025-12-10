alunos = []

for n in range(2):
    print(f'\n----- Aluno {n + 1} -----')
    nome = input('Informe o nome do aluno: ')

    notas = []
    for i in range(2):
        nota = float(input(f'Informe a nota{i + 1}: '))
        notas.append(nota)

    media = sum(notas) / len(notas)    
    print(media)

    aluno = {
        'Nome': nome,
        'Notas': notas,
        'Media': media
    }

    alunos.append(aluno)

                                       #exibindo dados

for estudante in alunos:
    print(f'\nNome: {estudante["Nome"]} \nNota: {estudante["Notas"]} \nMedia: {estudante["Media"]}')

