tarefa = []

// função para listar tarefas 
def listar_tarefas(tarefa):
    if not tarefa:
        print("Nenhum regitro encontrado!")
    else:
        for i, t in enumerate(tarefa, start=1):
            print(f"{i}. {t}")

def pesquisar_tarefa(tarefa, search):
    i=0
    for i, t in enumerate (tarefa, start=1):
        if search == t:
            print(i,tarefa[i-1])
    

    
def criar_tarefa(tarefa, tarefa_nova):
    tarefa.append(tarefa_nova)
    print("Tarefa adicionada com sucesso!")

def excluir_tarefa(tarefa):
    delete = input("Digite a tarefa a ser apagada: ").strip()
    if delete.lower() in tarefa:
        tarefa.remove(delete)
        print("tarefa removida")
    else:
        print("Tarefa não encontrada!")


def editar_tarefa(tarefa, valor):
    i=0
    for i, t in enumerate(tarefa, start=1):
        if valor == i:
            alterar = input("Como deseja renomear essa tarefa? ")
            tarefa[i-1] = alterar
            print(i,tarefa[i-1])
            break
    
        
def main():
    while True:
        print("Bem-vindo a sua lista de tarefas!")
        print("Selecione uma opção para prosseguir:")
        print("(1) Listar Tarefas")
        print("(2) Pesquisar Tarefa")
        print("(3) Criar Tarefa")
        print("(4) Excluir Tarefa")
        print("(5) Editar tarefa")
        print("(6) Sair do Programa")
        
        resposta = input("Digite o número da opção desejada: ")
        
        if resposta == "6":
            print("Obrigado por usar a sua lista de tarefas!")
            exit()
        elif resposta == "1":
            print("Listando tarefas...")
            listar_tarefas(tarefa)
        elif resposta == "2":
            search = input("Pesquisar tarefa: ")
            print("Pesquisando tarefas...")
            pesquisar_tarefa(tarefa, search)       
        elif resposta == "3":
            print("Criando tarefas...")
            tarefa_nova = input("Digite uma nova tarefa: ")
            criar_tarefa(tarefa, tarefa_nova)
        elif resposta == "4":
            print("Excluindo tarefas...")
            excluir_tarefa(tarefa)
        elif resposta == "5":
            print("Editando tarefas...")
            valor = int(input("Qual tarefa deseja alterar? "))
            editar_tarefa(tarefa, valor)
        else:
            print("Opção inválida. Tente novamente.")
            main()

if __name__ == '__main__':
    main()
