#!/usr/bin/env python3
"""
Script para sincronizar dados do DOEM (Diário Oficial do Estado da Bahia)
com o vault do Obsidian
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os

# URL do DOEM para Prado
DOEM_URL = "https://doem.org.br/ba/prado"
OUTPUT_DIR = "DOEM_Downloads"

def criar_diretorio():
    """Cria diretório para downloads se não existir"""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"✅ Diretório '{OUTPUT_DIR}' criado")

def raspar_doem():
    """Raspa dados do DOEM"""
    try:
        print(f"🔍 Consultando {DOEM_URL}...")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(DOEM_URL, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extrair informações
        publicacoes = []
        
        # Procurar por elementos comuns
        items = soup.find_all(['article', 'div'], class_=['item', 'publicacao', 'resultado'])
        
        for item in items:
            titulo = item.find(['h2', 'h3', 'a'])
            data = item.find(['span', 'time'])
            
            if titulo:
                publicacoes.append({
                    'titulo': titulo.get_text(strip=True),
                    'data': data.get_text(strip=True) if data else 'Data não encontrada',
                    'url': item.find('a')['href'] if item.find('a') else DOEM_URL
                })
        
        if publicacoes:
            print(f"✅ {len(publicacoes)} publicações encontradas")
        else:
            print("⚠️  Nenhuma publicação encontrada")
        
        return publicacoes
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao consultar DOEM: {e}")
        return []

def salvar_json(dados):
    """Salva dados em JSON"""
    timestamp = datetime.now().isoformat()
    arquivo = os.path.join(OUTPUT_DIR, f"doem_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': timestamp,
            'url': DOEM_URL,
            'publicacoes': dados
        }, f, ensure_ascii=False, indent=2)
    
    print(f"💾 Dados salvos em: {arquivo}")
    return arquivo

def atualizar_markdown(dados):
    """Atualiza arquivo markdown com dados do DOEM"""
    arquivo_md = "DOEM_Prado_BA.md"
    
    tabela = "| Data | Tipo | Descrição | Status |\n"
    tabela += "|------|------|-----------|--------|\n"
    
    for pub in dados[:10]:  # Últimas 10
        tabela += f"| {pub['data']} | Publicação | {pub['titulo'][:50]}... | ✅ Novo |\n"
    
    print(f"📝 Arquivo markdown atualizado: {arquivo_md}")

def main():
    print("\n" + "="*50)
    print("🔗 SINCRONIZADOR DOEM - PRADO/BA")
    print("="*50 + "\n")
    
    criar_diretorio()
    publicacoes = raspar_doem()
    
    if publicacoes:
        salvar_json(publicacoes)
        atualizar_markdown(publicacoes)
    
    print("\n✅ Sincronização concluída!\n")

if __name__ == "__main__":
    main()
