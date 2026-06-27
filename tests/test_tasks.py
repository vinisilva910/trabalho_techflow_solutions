from src.tasks import TaskManager


def test_criar_tarefa():
    manager = TaskManager()
    manager.criar_tarefa("Estudar Python")

    assert len(manager.tasks) == 1
    assert manager.tasks[0].titulo == "Estudar Python"


def test_concluir_tarefa():
    manager = TaskManager()
    manager.criar_tarefa("Estudar")

    manager.concluir_tarefa(1)

    assert manager.tasks[0].concluida is True


def test_remover_tarefa():
    manager = TaskManager()

    manager.criar_tarefa("A")
    manager.criar_tarefa("B")

    manager.remover_tarefa(1)

    assert len(manager.tasks) == 1
