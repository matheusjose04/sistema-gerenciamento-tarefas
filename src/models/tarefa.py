
class Tarefa:
    def __init__(self, titulo, descricao, prioridade, ):
        self._titulo = titulo.strip( )
        self._descricao = descricao
        self._prioridade = max(1, min(prioridade, 5))
        self._concluida = False

        if len(self._titulo) == 0:
            self._titulo = "Sem titulo"

    def marcar_concluida(self):
        self._concluida = True
    def marcar_pendente(self):
        self._concluida = False

    @property
    def status(self):
        return "Concluida" if self._concluida else "Pendente"
    
    def alterar_prioridade(self, nova_prioridade):
        self._prioridade = max(1, min(nova_prioridade, 5))
    
    @property
    def prioridade(self):
        return(self._prioridade)