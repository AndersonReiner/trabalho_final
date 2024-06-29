#!/bin/bash

# Nome do ambiente virtual
VENV_DIR="venv"

# Nome do script Python
SCRIPT_NAME="hamiltonian_cycle_with_visualization.py"

# Nome do executável de saída
OUTPUT_NAME="hamiltonian_cycle_with_visualization"

# Criar o ambiente virtual
echo "Criando ambiente virtual..."
python3 -m venv $VENV_DIR

# Ativar o ambiente virtual
echo "Ativando ambiente virtual..."
source $VENV_DIR/bin/activate

# Atualizar pip
echo "Atualizando pip..."
pip install --upgrade pip

# Instalar as bibliotecas necessárias
echo "Instalando bibliotecas necessárias..."
pip install networkx matplotlib

# Testar o script
echo "Testando o script..."
python $SCRIPT_NAME

if [ $? -ne 0 ]; then
    echo "Erro ao executar o script. Verifique o código e tente novamente."
    deactivate
    exit 1
fi

# Instalar PyInstaller
echo "Instalando PyInstaller..."
pip install pyinstaller

# Criar o executável
echo "Criando executável..."
pyinstaller --onefile --windowed $SCRIPT_NAME

# Verificar se a criação do executável foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Erro ao criar o executável. Verifique o PyInstaller e tente novamente."
    deactivate
    exit 1
fi

# Desativar o ambiente virtual
echo "Desativando o ambiente virtual..."
deactivate

# Instruções finais
echo "O executável foi criado com sucesso!"
echo "Você pode encontrá-lo na pasta 'dist' com o nome '$OUTPUT_NAME'."
echo "Para executar o arquivo, use o seguinte comando:"
echo "cd dist"
echo "./$OUTPUT_NAME"

# Script finalizado
echo "Script concluído com sucesso!"
