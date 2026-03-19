import json
import os
from src.models.tarefa import Tarefa


class GerenciadorDeTarefas:
    def __init__(self):
        self._tarefas = []
        self._arquivo = os.path.join("src", "database", "tarefas.json")
        self.carregar()

    def salvar(self):
        dados = []

        for t in self._tarefas:
            dados.append({
                "titulo": t._titulo,
                "descricao": t._descricao,
                "prioridade": t._prioridade,
                "concluida": t._concluida
            })

        with open(self._arquivo, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4)

    def carregar(self):
        if not os.path.exists(self._arquivo):
            return

        with open(self._arquivo, "r", encoding="utf-8") as f:
            try:
                dados = json.load(f)
            except json.JSONDecodeError:
                dados = []

        for item in dados:
            tarefa = Tarefa(
                titulo=item["titulo"],
                descricao=item["descricao"],
                prioridade=item["prioridade"]
            )

            if item["concluida"]:
                tarefa.marcar_concluida()

            self._tarefas.append(tarefa)

    def adicionar_tarefa(self, tarefa):
        if isinstance(tarefa, Tarefa):
            self._tarefas.append(tarefa)
            self.salvar()

    def remover_tarefa(self, tarefa):
        if tarefa in self._tarefas:
            self._tarefas.remove(tarefa)
            self.salvar()

    @property
    def total_tarefas(self):
        return len(self._tarefas)

    @property
    def total_concluidas(self):
        return sum(1 for t in self._tarefas if t._concluida)

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
        self.ondem_de_prioridade()
        pendentes = [t for t in self._tarefas if not t._concluida]

        if not pendentes:
            print("Nenhuma tarefa pendente.")
            return

        print(f'{"Titulo".ljust(25)} | {"Prioridade".ljust(25)} | {"Status".ljust(25)}')

        for t in pendentes:
            print(f'{t._titulo.ljust(25)} | {str(t._prioridade).ljust(25)} | {t.status.ljust(25)}')

    def ondem_de_prioridade(self):
        for i in range(len(self._tarefas)):
            for y in range(len(self._tarefas) - 1):
                if self._tarefas[y + 1].prioridade < self._tarefas[y].prioridade:
                    self._tarefas[y], self._tarefas[y + 1] = self._tarefas[y + 1], self._tarefas[y]