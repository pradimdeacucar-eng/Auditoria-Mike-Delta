#!/bin/bash

# Script de Auditoria Automática Completa
# Executar: bash auditoria_completa.sh

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  🔍 AUDITORIA AUTOMÁTICA DE CONFORMIDADE LEGAL             ║"
echo "║     Prefeitura Municipal de Prado - BA                     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 não encontrado. Instale para continuar.${NC}"
    exit 1
fi

echo -e "${BLUE}✅ Python 3 encontrado$(python3 --version)${NC}"
echo ""

# Etapa 1: Verificar dependências
echo -e "${YELLOW}[1/4] Verificando dependências...${NC}"
python3 -c "import requests" 2>/dev/null
if [ $? -ne 0 ]; then
    echo -e "${YELLOW}  📦 Instalando requests...${NC}"
    pip3 install requests beautifulsoup4 -q
fi
echo -e "${GREEN}  ✅ Dependências OK${NC}"
echo ""

# Etapa 2: Executar auditoria de conformidade
echo -e "${YELLOW}[2/4] Executando análise de conformidade...${NC}"
python3 auditoria_conformidade.py
AUDIT_STATUS=$?

if [ $AUDIT_STATUS -eq 0 ]; then
    echo -e "${GREEN}  ✅ Auditoria concluída${NC}"
else
    echo -e "${RED}  ❌ Erro na auditoria${NC}"
    exit 1
fi
echo ""

# Etapa 3: Gerar propostas de correção
echo -e "${YELLOW}[3/4] Gerando propostas de correção...${NC}"
python3 gerar_propostas_obsidian.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}  ✅ Propostas geradas${NC}"
else
    echo -e "${YELLOW}  ⚠️  Propostas não puderam ser geradas${NC}"
fi
echo ""

# Etapa 4: Resumo Final
echo -e "${YELLOW}[4/4] Gerando resumo...${NC}"
echo ""
echo -e "${BLUE}╔════════════════════════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║  📊 RESUMO DA AUDITORIA                                    ║${NC}"
echo -e "${BLUE}╚════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Contar arquivos gerados
AUDIT_FILES=$(ls -1 auditoria_conformidade_*.json 2>/dev/null | wc -l)
PROP_FILES=$(ls -1 Propostas_de_Correcao/*.md 2>/dev/null | wc -l)

echo -e "📄 Relatórios de Auditoria: ${GREEN}${AUDIT_FILES}${NC} arquivo(s)"
echo -e "📝 Propostas de Correção: ${GREEN}${PROP_FILES}${NC} arquivo(s)"
echo ""

# Mostrar arquivo de auditoria mais recente
LATEST_AUDIT=$(ls -1t auditoria_conformidade_*.json 2>/dev/null | head -1)
if [ -n "$LATEST_AUDIT" ]; then
    echo -e "${BLUE}📋 Último Relatório:${NC} $LATEST_AUDIT"
    
    # Extrair informações do JSON (simplificado)
    echo ""
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}Estatísticas Principais:${NC}"
    echo ""
    
    # Tentar extrair dados com grep/jq se disponível
    if command -v jq &> /dev/null; then
        TOTAL=$(jq '.relatorio_consolidado.total_publicacoes' "$LATEST_AUDIT" 2>/dev/null)
        INCONFORMIDADES=$(jq '.relatorio_consolidado.total_inconformidades' "$LATEST_AUDIT" 2>/dev/null)
        MEDIA=$(jq '.relatorio_consolidado.pontuacao_media' "$LATEST_AUDIT" 2>/dev/null)
        
        echo -e "  • Total de Publicações: ${YELLOW}${TOTAL}${NC}"
        echo -e "  • Inconformidades: ${RED}${INCONFORMIDADES}${NC}"
        echo -e "  • Conformidade Média: ${YELLOW}${MEDIA}%${NC}"
    fi
    echo ""
fi

echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo ""

# Instruções finais
echo -e "${GREEN}✅ AUDITORIA CONCLUÍDA COM SUCESSO!${NC}"
echo ""
echo -e "${BLUE}📌 Próximas ações:${NC}"
echo "  1. Abra o arquivo de relatório para revisar"
echo "  2. Acesse Propostas_de_Correcao/Indice.md no Obsidian"
echo "  3. Implemente as correções por ordem de prioridade"
echo "  4. Valide as mudanças"
echo "  5. Re-execute a auditoria para confirmar conformidade"
echo ""

echo -e "${BLUE}📁 Arquivos Gerados:${NC}"
echo "  • auditoria_conformidade_*.json - Relatórios detalhados"
echo "  • Propostas_de_Correcao/ - Propostas de ação"
echo "  • AUDITORIA_CONFORMIDADE_GUIA.md - Documentação"
echo ""

echo -e "${BLUE}🔗 Links:${NC}"
echo "  • DOEM: https://doem.org.br/ba/prado"
echo "  • Obsidian Vault: D:/PREFEITURA_PRADO_BA"
echo ""

echo -e "${YELLOW}📅 Próxima execução recomendada: em 7 dias${NC}"
echo ""
