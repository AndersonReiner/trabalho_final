# Hamiltonian Cycle Project

Este projeto implementa um algoritmo para encontrar e visualizar um ciclo Hamiltoniano em um grafo que representa cidades e suas conexões. O objetivo é identificar um caminho que visita cada cidade exatamente uma vez e retorna à cidade de origem.

## Arquivos do Projeto

- **`hamiltonian_cycle_with_visualization.py`**: O script Python principal que implementa o algoritmo de ciclo Hamiltoniano e a visualização do grafo.
- **`setup_and_build.sh`**: Um script `bash` que automatiza a criação de um ambiente virtual, a instalação das dependências e a geração de um executável.
- **`README.md`**: Este arquivo de instruções.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes ferramentas instaladas em seu sistema:

- **Python 3.x**: Inclui o comando `python3` e o gerenciador de pacotes `pip`.
- **pip**: O gerenciador de pacotes Python, usado para instalar dependências.
- **Bash**: O shell Unix, necessário para executar o script `setup_and_build.sh`.

## Passos para Configuração e Execução

Siga os passos abaixo para configurar o ambiente e criar o executável:

### 1. Tornar o Script Executável

Primeiro, torne o script `setup_and_build.sh` executável. Abra um terminal e navegue até o diretório do projeto, então execute:

```bash
chmod +x setup_and_build.sh
```

por fim

```bash
./setup_and_build.sh