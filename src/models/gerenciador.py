
from src.models.tarefa import Tarefa


class GerenciadorDeTarefas:
    def __init__(self):
        self._tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        if isinstance(tarefa, Tarefa):
            self._tarefas.append(tarefa)
    
    def remover_tarefa(self, tarefa):
        if tarefa in self._tarefas:
            self._tarefas.remove(tarefa)

    @property
    def total_tarefas(self):
        return len(self._tarefas)
    
    @property
    def total_concluidas(self):
        contador = 0
        for t in self._tarefas:
            if t._concluida:
                contador += 1
        return contador

    def listar_tarefas(self):
        self.ondem_de_prioridade()

        print(f'{"Titulo".ljust(25)} | {"Prioridade".ljust(25)} | {"Status".ljust(25)}')
        for t in self._tarefas:
            print(f'{t._titulo.ljust(25)} | {str(t._prioridade).ljust(25)} | {t.status.ljust(25)}')
    
    def listar_concluidas(self):
        concluidas = [t for t in self._tarefas if t._concluida]
        
        if not concluidas:
            print("Nenhuma tarefa concluída.")
            return
        
        print(f'{"Titulo".ljust(25)} | {"Prioridade".ljust(25)} | {"Status".ljust(25)}')


        for t in concluidas:
            print(f'{t._titulo.ljust(25)} | {str(t._prioridade).ljust(25)} | {t.status.ljust(25)}')


    def listar_pendentes(self):
        pendentes = [t for t in self._tarefas if t._concluida == False]

        if not pendentes:
            print("Nenhuma em pendencias tarefa concluída.")
            return
        print(f'{"Titulo".ljust(25)} | {"Prioridade".ljust(25)} | {"Status".ljust(25)}')
        for t in pendentes:
            print(f'{t._titulo.ljust(25)} | {str(t._prioridade).ljust(25)} | {t.status.ljust(25)}')
        
    def ondem_de_prioridade(self):
        for i in range(len(self._tarefas)):
            for y in range(len(self._tarefas) - 1):
                if self._tarefas[y + 1].prioridade < self._tarefas[y].prioridade:
                     self._tarefas[y], self._tarefas[y + 1] = self._tarefas[y + 1], self._tarefas[y]
                            

        