# criando a class tarefa
class Tarefa:
    def __init__(self, titulo, descricao, prioridade, ):
        self._titulo = titulo
        self._descricao = descricao
        self._prioridade = max(1, min(prioridade, 5))
        self._concluida = False

    def marcar_concluida(self):
        self._concluida = True
    def marcar_pendente(self):
        self._concluida = False

    @property
    def status(self):
        return "Concluida" if self._concluida else "Pendente"