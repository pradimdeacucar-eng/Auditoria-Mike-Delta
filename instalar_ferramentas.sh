#!/bin/bash

# Script de instalação de ferramentas para auditoria
# Data: 2026-06-03

echo "======================================"
echo "Instalando ferramentas necessárias..."
echo "======================================"

# Atualizar repositórios
echo "1. Atualizando repositórios..."
sudo apt update

# Instalar Python e ferramentas
echo "2. Instalando Python e dependências..."
sudo apt install -y python3 python3-pip python3-venv python3-dev

# Instalar ferramentas de desenvolvimento
echo "3. Instalando ferramentas de desenvolvimento..."
sudo apt install -y build-essential git curl wget nano vim

# Instalar PowerShell (opcional)
echo "4. Instalando PowerShell..."
sudo apt install -y powershell

# Instalar ferramentas adicionais úteis
echo "5. Instalando ferramentas adicionais..."
sudo apt install -y jq unzip zip htop tree

# Upgrade do pip
echo "6. Atualizando pip..."
python3 -m pip install --upgrade pip setuptools wheel

# Instalar bibliotecas Python úteis
echo "7. Instalando bibliotecas Python..."
pip3 install requests beautifulsoup4 pandas openpyxl json5 pyyaml

# Criar diretório PREFEITURA_PRADO_BA
echo "8. Criando diretório de trabalho..."
sudo mkdir -p /mnt/d/PREFEITURA_PRADO_BA
cd /mnt/d/PREFEITURA_PRADO_BA

echo "======================================"
echo "Instalação concluída com sucesso!"
echo "======================================"
echo ""
echo "Versões instaladas:"
python3 --version
pip3 --version
bash --version | head -1
git --version
curl --version | head -1
echo ""
echo "Para verificar PowerShell: pwsh --version"
echo ""
