import os
from src.models.tarefa import Tarefa
from src.models.gerenciador import GerenciadorDeTarefas


def menu():
        print("""
        ==================================================
                📋 SISTEMA DE GERENCIAMENTO DE TAREFAS
        ==================================================

        [1] Adicionar tarefa
        [2] Listar tarefas
        [3] Listar pendentes
        [4] Listar concluídas
        [5] Marcar como concluída
        [6] Remover tarefa
        [7] Mostrar totais

        [0] Sair

        ==================================================
        """)

        try:
            valor_permitidos = range(0, 8)
            opcao = int(input('Digite a sua opção: '))

            if opcao in valor_permitidos:
                return opcao
            else:
                print('Opção inválida. Escolha um número do menu.')

        except ValueError:
            print('Digite apenas números.')
def adicionar_tarefa(ger):
     nova_tarefa = Tarefa(titulo = input('Digite o titulo da tarefa: '),
                        descricao = input('escreva a descricao da tarefa: '),
                        prioridade = int(input('qual prioridade de 1 a 5: ')),
                        )
     ger.adicionar_tarefa(nova_tarefa)
     print(f'tarefa adicionada com susesso')
     

                
def main():
    ger = GerenciadorDeTarefas() 
    while True:
        opcao = menu()
        match opcao:
             case 0:
                  os.system('cls')
                  break
             case 1:
                  os.system('cls')
                  adicionar_tarefa(ger)
             case 2:
                  os.system('cls')
                  ger.listar_tarefas()
                  input("Pressione ENTER para voltar ao menu...")
                  os.system("cls")
             case 3:
                  os.system('cls')
                  ger.listar_pendentes()
                  input("Pressione ENTER para voltar ao menu...")
                  os.system("cls")                  
             case 4:
                  os.system('cls')
                  ger.listar_concluidas()
                  input("Pressione ENTER para voltar ao menu...")
                  os.system("cls")
             case 5:
                  concluido = input('')
if __name__ == "__main__":
     main()