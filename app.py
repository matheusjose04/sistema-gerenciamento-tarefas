import os

os.system('cls')
from src.models.tarefa import Tarefa

print("===== TESTE 1 - Prioridade menor que 1 =====")
t1 = Tarefa("Teste", "Desc", -1)
print(t1._prioridade)  # esperado: 1


print("===== TESTE 2 - Prioridade maior que 5 =====")
t2 = Tarefa("Teste", "Desc", 6)
print(t2._prioridade)  # esperado: 5


print("===== TESTE 3 - Prioridade válida =====")
t3 = Tarefa("Teste", "Desc", 3)
print(t3._prioridade)  # esperado: 3


print("===== TESTE 4 - Estado inicial =====")
print(t3._concluida)  # esperado: False


print("===== TESTE 5 - Marcar concluída =====")
t3.marcar_concluida()
print(t3._concluida)  # esperado: True


print("===== TESTE 6 - Voltar para pendente =====")
t3.marcar_pendente()
print(t3._concluida)  # esperado: False