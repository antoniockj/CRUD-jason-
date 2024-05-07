import json

# Função para ler um arquivo JSON
def ler_arquivo(nome_do_arquivo):
    try:
        with open(nome_do_arquivo + ".json", 'r', encoding='utf-8') as f:
            lista = json.load(f)
            return lista
    except:
        return []

# Função para salvar uma lista em um arquivo JSON
def salvar_arquivo(lista, nome_do_arquivo):
    with open(nome_do_arquivo + ".json", "w", encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False)

def menu_principal():
    menu_principal = ['---Menu principal---',
              '(1)Gerenciar estudantes',
              '(2)Gerenciar disciplinas',
              '(3)Gerenciar professores',
              '(4)Gerenciar turmas',
              '(5)Gerenciar matriculas',
              '(0)Sair']
    for i in menu_principal:
        print(i)

def menu_secundario():
    menu_secundario = ['---Menu de operações---',
              '(1)Incluir',
              '(2)Listar',
              '(3)Editar',
              '(4)Excluir',
              '(0)Voltar para o menu principal']
    for i in menu_secundario:
        print(i)

def menu_edit(arquivo_sem_ext):
    if arquivo_sem_ext == "estudante" or "professor":
        menu_edit = ['---Menu de edição---',
                    '(1)Editar codigo',
                    '(2)Editar nome',
                    '(3)Editar CPF']
    elif arquivo_sem_ext == "disciplina":
        menu_edit = ['---Menu de edição---',
                    '(1)Editar codigo',
                    '(2)Editar nome']
    elif arquivo_sem_ext == "turma":
        menu_edit = ['---Menu de edição---',
                    '(1)Editar código da turma',
                    '(2)Editar código professor ',
                    '(2)Editar código disciplina ']
    elif arquivo_sem_ext == "matricula":
        menu_edit = ['---Menu de edição---',
                    '(1)Editar codigo da turma',
                    '(2)Editar código do estudante']
    for i in menu_edit:
        print(i)

# Função para exibir a tabela
def mostrar_tabela(opcao):
    print(opcao)

# Função para incluir uma pessoa
def incluir_pessoa(codigo, nome, cpf, file):
    info = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
        }
    lista = ler_arquivo(file)
    lista.append(info)
    salvar_arquivo(lista, file)

# Função para incluir outros itens
def incluir_outros(arquivo_sem_ext):
    if arquivo_sem_ext == "disciplina":
        codigo = int(input('Digite o código da {}: '.format(arquivo_sem_ext)))
        nome = input('Digite o nome da {}: '.format(arquivo_sem_ext))
        info = {
            "codigo": codigo,
            "nome": nome
            }

    if arquivo_sem_ext == "turma":
        codigo_turma = int(input('Digite o código da turma: '))
        codigo_professor = int(input('Digite o código do professor: '))
        codigo_disciplina = int(input('Digite o código da disciplina: '))
        info = {
            "codigo_turma": codigo_turma,
            "codigo_professor": codigo_professor,
            "codigo_disciplina": codigo_disciplina
        }

    if arquivo_sem_ext == "matricula":
        codigo_turma = int(input('Digite o código da turma: '))
        codigo_estudante = int(input('Digite o código do estudante: '))
        info = {
            "codigo_turma": codigo_turma,
            "codigo_estudante": codigo_estudante
            }
    lista = ler_arquivo(arquivo_sem_ext)
    lista.append(info)
    salvar_arquivo(lista, arquivo_sem_ext)

# Função para editar informações
def editar(arquivo_sem_ext):
    if arquivo_sem_ext == "estudante" or "professor":
        cod = int(input('Qual o código da pessoa que você deseja editar: '))
        menu_edit(arquivo_sem_ext)
        edit = int(input('Digite o que você quer editar: '))
        lista = ler_arquivo(arquivo_sem_ext)
        encontrado = False
        for pessoa in lista:
            if pessoa.get('codigo') == cod:
                encontrado = True
                if edit == 1:
                    modf = int(input('Qual o novo código: '))
                    pessoa.update({'codigo': modf})
                    salvar_arquivo(lista, arquivo_sem_ext)
                    break
                elif edit == 2:
                    modf = str(input('Digite o novo nome: '))
                    pessoa.update({'nome': modf})
                    salvar_arquivo(lista, arquivo_sem_ext)
                    break
                elif edit == 3:
                    modf = str(input('Digite o novo CPF: '))
                    pessoa.update({'cpf': modf})
                    salvar_arquivo(lista, arquivo_sem_ext)
                    break
        if not encontrado:
            print('Código não encontrado!')

# Função para remover um elemento
def remover(arquivo_semext):
    remover = int(input(f'Digite o código do/da {arquivo_semext} que deseja remover: '))
    lista = ler_arquivo(arquivo_semext)
    for i in lista:
        if i.get('codigo') == remover:
            lista.remove(i)
            print(f'{arquivo_semext} com código {remover} removido com sucesso.')
            salvar_arquivo(lista, arquivo_semext)
            break
        else:
            print('Estudante não encontrado.')

# estudantes ou professores
def pessoas(arquivo_sem_ext):
    loop = True
    while loop:
        menu_secundario()
        opcao = int(input('Digite uma opcao:'))
        if opcao == 1:
            codigo = int(input(f'Digite o código do {arquivo_sem_ext}:'))
            nome = input(f'Digite o nome do {arquivo_sem_ext}:')
            cpf = input(f'Digite o CPF do {arquivo_sem_ext}:')
            incluir_pessoa(codigo, nome, cpf, arquivo_sem_ext)
        elif opcao == 2:
            mostrar_tabela(ler_arquivo(arquivo_sem_ext))
        elif opcao == 3:
            editar(arquivo_sem_ext)
        elif opcao == 4:
            remover(arquivo_sem_ext)
        elif opcao == 0:
            break
        else:
            print('Opção inválida, escolha uma opção disponível no menu abaixo:')

# disciplinas, turmas e matrículas
def outros(arquivo_sem_ext):
    loop = True
    while loop:
        menu_secundario()
        opcao = int(input('Digite uma opção: '))
        if opcao == 1:
            incluir_outros(arquivo_sem_ext)
        elif opcao == 2:
            mostrar_tabela(ler_arquivo(arquivo_sem_ext))
        elif opcao == 3:
            editar(arquivo_sem_ext)
        elif opcao == 4:
            remover(arquivo_sem_ext)
        elif opcao == 0:
            break
        else:
            print('Opção inválida, escolha uma opção disponivel no menu abaixo: ')

# Loop principal
loop = True
while loop:
    menu_principal()
    opcao1 = int(input("Digite a sua opção: "))

    if opcao1 == 0:
        loop = False
    elif opcao1 == 1:
        pessoas("estudante")
    elif opcao1 == 2:
        outros("disciplina")
        pass
    elif opcao1 == 3:
        pessoas("professor")
        pass
    elif opcao1 == 4:
        outros("turma")
        pass
    elif opcao1 == 5:
        outros("matricula")
        pass
    else:
        print('Opção inválida, escolha uma opção disponível no menu abaixo: ')