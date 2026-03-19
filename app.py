import os
from src.models.tarefa import Tarefa
from src.models.gerenciador import GerenciadorDeTarefas

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def ler_inteiro(mensagem, minimo=None, maximo=None):
    """Lê um número inteiro e garante que ele seja válido e esteja no intervalo."""
    while True:
        try:
            entrada = input(mensagem).strip()
            if not entrada:
                print("❌ Erro: O campo não pode ser vazio.")
                continue
            
            numero = int(entrada)
            
            if minimo is not None and numero < minimo:
                print(f"❌ Erro: O número deve ser no mínimo {minimo}.")
            elif maximo is not None and numero > maximo:
                print(f"❌ Erro: O número deve ser no máximo {maximo}.")
            else:
                return numero
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido.")

def menu():
    print("""
==================================================
        📋 SISTEMA DE GERENCIAMENTO DE TAREFAS
==================================================
[1] Adicionar tarefa
[2] Listar tarefas
[3] Listar pendentes
[4] Listar concluídas
[5] Marcar / Desmarcar tarefa
[6] Remover tarefa
[7] Mostrar totais

[0] Sair
==================================================
""")
    return ler_inteiro('Digite a sua opção: ', 0, 7)

def adicionar_tarefa(ger):
    limpar_tela()

    while True:
        titulo = input('Título: ').strip()
        if titulo: break
        print("❌ Título obrigatório!")
        
    descricao = input('Descrição: ').strip()
    

    prioridade = ler_inteiro('Prioridade (1-5): ', 1, 5)
    
    nova = Tarefa(titulo=titulo, descricao=descricao, prioridade=prioridade)
    ger.adicionar_tarefa(nova)
    print("\n✅ Tarefa adicionada!")
    input("ENTER para voltar...")

def main():
    ger = GerenciadorDeTarefas()

    while True:
        limpar_tela()
        opcao = menu()

        match opcao:
            case 0:
                limpar_tela()
                print("Saindo...")
                break

            case 1:
                adicionar_tarefa(ger)

            case 2:
                limpar_tela()
                ger.listar_tarefas()
                input("\nENTER para voltar...")

            case 3:
                limpar_tela()
                ger.listar_pendentes()
                input("\nENTER para voltar...")

            case 4:
                limpar_tela()
                ger.listar_concluidas()
                input("\nENTER para voltar...")

            case 5:
                limpar_tela()
                escolha = input("Marcar como concluído? (S/N): ").upper().strip()

                if escolha == 'S':
                    pendentes = [t for t in ger._tarefas if not t._concluida]
                    if not pendentes:
                        print("Nenhuma tarefa pendente.")
                    else:
                        for i, t in enumerate(pendentes, start=1):
                            print(f"{i} - {t._titulo}")
                        
                        indice = ler_inteiro("Escolha a tarefa: ", 1, len(pendentes))
                        pendentes[indice - 1].marcar_concluida()
                        ger.salvar()
                        print("✅ Tarefa concluída!")

                else:
                    escolha = input("Voltar para pendente? (S/N): ").upper().strip()
                    if escolha == 'S':
                        concluidas = [t for t in ger._tarefas if t._concluida]
                        if not concluidas:
                            print("Nenhuma tarefa concluída.")
                        else:
                            for i, t in enumerate(concluidas, start=1):
                                print(f"{i} - {t._titulo}")
                            
                            indice = ler_inteiro("Escolha a tarefa: ", 1, len(concluidas))
                            concluidas[indice - 1].marcar_pendente()
                            ger.salvar()
                            print("✅ Tarefa voltou para pendente!")

                input("\nENTER para voltar...")

            case 6:
                limpar_tela()
                if not ger._tarefas:
                    print("Lista vazia.")
                else:
                    for i, t in enumerate(ger._tarefas, start=1):
                        print(f"{i} - {t._titulo}")

                    indice = ler_inteiro("Qual tarefa remover: ", 1, len(ger._tarefas))
                    ger.remover_tarefa(ger._tarefas[indice - 1])
                    ger.salvar()
                    print("🗑️ Tarefa removida!")

                input("\nENTER para voltar...")

            case 7:
                limpar_tela()
                print(f"Total de tarefas: {ger.total_tarefas}")
                print(f"Concluídas: {ger.total_concluidas}")
                input("\nENTER para voltar...")

if __name__ == "__main__":
    main()