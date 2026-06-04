#!/bin/bash

# Script de Auditoria Retrospectiva Completa
# Analisa perdas financeiras e patrimoniais históricas
# Executa: bash auditoria_retroativa_completa.sh

echo ""
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  🔍 AUDITORIA RETROSPECTIVA PATRIMONIAL E FINANCEIRA          ║"
echo "║     Prefeitura Municipal de Prado - BA                        ║"
echo "║     Período de Análise: 2016-2026                             ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
NC='\033[0m'

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ Python 3 não encontrado${NC}"
    exit 1
fi

echo -e "${BLUE}✅ Ambiente pronto${NC}"
echo ""

# Etapa 1: Auditoria Retrospectiva Financeira e Patrimonial
echo -e "${YELLOW}[1/3] Executando Auditoria Retrospectiva...${NC}"
python3 auditoria_retroativa.py
RETRO_STATUS=$?

if [ $RETRO_STATUS -eq 0 ]; then
    echo -e "${GREEN}  ✅ Auditoria Retrospectiva concluída${NC}"
else
    echo -e "${RED}  ❌ Erro na auditoria retrospectiva${NC}"
    exit 1
fi
echo ""

# Etapa 2: Gerar Propostas de Recuperação
echo -e "${YELLOW}[2/3] Gerando Propostas de Recuperação...${NC}"

# Procurar arquivo de auditoria mais recente
LATEST_RETRO=$(ls -1t auditoria_retroativa_*.json 2>/dev/null | head -1)

if [ -n "$LATEST_RETRO" ]; then
    echo -e "${BLUE}  Processando: $LATEST_RETRO${NC}"
    python3 gerar_propostas_recuperacao.py "$LATEST_RETRO"
    echo -e "${GREEN}  ✅ Propostas geradas${NC}"
else
    echo -e "${YELLOW}  ⚠️  Nenhuma auditoria retrospectiva encontrada${NC}"
fi
echo ""

# Etapa 3: Relatório Summary
echo -e "${YELLOW}[3/3] Gerando Resumo Executivo...${NC}"

echo ""
echo -e "${MAGENTA}╔═══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${MAGENTA}║  📊 RESUMO DA AUDITORIA RETROSPECTIVA                        ║${NC}"
echo -e "${MAGENTA}╚═══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Extrair totais se jq disponível
if command -v jq &> /dev/null && [ -n "$LATEST_RETRO" ]; then
    echo -e "${BLUE}Perdas Identificadas:${NC}"
    
    # Contar casos
    CASOS_FIN=$(jq '[.perdas_financeiras[]?.casos[]? | objects] | length' "$LATEST_RETRO" 2>/dev/null)
    CASOS_PAT=$(jq '[.perdas_patrimoniais[]?.casos[]? | objects] | length' "$LATEST_RETRO" 2>/dev/null)
    
    echo -e "  • Casos Financeiros: ${YELLOW}${CASOS_FIN}${NC}"
    echo -e "  • Casos Patrimoniais: ${YELLOW}${CASOS_PAT}${NC}"
    echo -e "  • Total Geral: ${RED}R$ $(jq '.total_geral_recuperavel' "$LATEST_RETRO" 2>/dev/null)${NC}"
fi

echo ""
echo -e "${BLUE}Arquivos Gerados:${NC}"
echo "  • auditoria_retroativa_*.json - Relatório detalhado"
echo "  • Propostas_Recuperacao/ - Propostas de ação"
echo "  • Índice de Recuperação - Prioridades"
echo ""

echo -e "${MAGENTA}═══════════════════════════════════════════════════════════════${NC}"
echo ""

echo -e "${GREEN}✅ AUDITORIA RETROSPECTIVA CONCLUÍDA COM SUCESSO!${NC}"
echo ""

echo -e "${BLUE}📌 Próximos Passos:${NC}"
echo "  1. Revisar relatório: auditoria_retroativa_*.json"
echo "  2. Abrir no Obsidian: Propostas_Recuperacao/Indice.md"
echo "  3. Acompanhar recuperação de valores"
echo "  4. Implementar controles preventivos"
echo ""

echo -e "${YELLOW}📅 Recomendação:${NC}"
echo "  • Re-executar auditoria retrospectiva anualmente"
echo "  • Atualizar dados de patrimônio com IMOVEL e SPU"
echo "  • Integrar com orçamento municipal"
echo ""
