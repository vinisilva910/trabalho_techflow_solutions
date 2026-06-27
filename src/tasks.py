class Task:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo
        self.concluida = False

    def concluir(self):
        self.concluida = True

    def __str__(self):
        status = "✔" if self.concluida else "✘"
        return f"{self.id} - {self.titulo} [{status}]"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def criar_tarefa(self, titulo):
        task = Task(len(self.tasks) + 1, titulo)
        self.tasks.append(task)

    def listar_tarefas(self):
        return self.tasks

    def concluir_tarefa(self, id):
        for task in self.tasks:
            if task.id == id:
                task.concluir()

    def remover_tarefa(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]
