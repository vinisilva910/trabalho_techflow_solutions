
from tasks import TaskManager

manager = TaskManager()

while True:
    print("\n===== TaskFlow =====")
    print("1 - Criar tarefa")
    print("2 - Listar tarefas")
    print("3 - Concluir tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")
    print("=====================")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o nome da tarefa: ")
        manager.criar_tarefa(titulo)
        print("Tarefa criada!")

    elif opcao == "2":
        tarefas = manager.listar_tarefas()
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in tarefas:
                print(tarefa)

    elif opcao == "3":
        id = int(input("Digite o ID da tarefa: "))
        manager.concluir_tarefa(id)
        print("Tarefa concluída!")

    elif opcao == "4":
        id = int(input("Digite o ID da tarefa: "))
        manager.remover_tarefa(id)
        print("Tarefa removida!")

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
