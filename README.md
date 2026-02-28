# Sistema de Gerenciamento de Tarefas

Este projeto está sendo desenvolvido como prática de Programação Orientada a Objetos em Python.

O objetivo é criar um sistema modular de gerenciamento de tarefas, aplicando boas práticas como organização em pastas, separação de responsabilidades e regras de negócio dentro das classes.

Neste projeto estou praticando:

- Criação de classes
- Encapsulamento (atributos privados)
- Uso de @property
- Validação de dados
- Separação da lógica principal (app.py) das regras de negócio (models)
- Organização de projeto em estrutura modular
- Uso do uv para gerenciamento de ambiente
- Versionamento com Git e GitHub

A estrutura principal do projeto é:

- models/tarefa.py → Classe que representa uma tarefa.
- models/gerenciador.py → Classe que gerencia várias tarefas.
- app.py → Arquivo principal para testar o sistema.

## Como executar o projeto

1. Clone o repositório:

git clone https://github.com/seuusuario/sistema-tarefas.git  
cd sistema-tarefas  

2. Instale as dependências usando uv:

uv sync  

Esse comando cria automaticamente o ambiente virtual e instala tudo que o projeto precisa.

3. Execute o projeto:

uv run python app.py  

Não é necessário ativar o ambiente virtual manualmente.

## Objetivo de aprendizado

Estou desenvolvendo este sistema para melhorar minha lógica de programação, organização de código e entendimento de arquitetura básica de software em Python.