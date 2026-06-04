#!/bin/bash

###############################################################################
# DEMONSTRAÇÃO INTERATIVA - Sistema de Auditoria Completo
# Mostra passo a passo como usar o sistema SEM ficar no chat
###############################################################################

set -e

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

clear

echo -e "${BLUE}"
cat << 'EOF'
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║     🎓 DEMONSTRAÇÃO INTERATIVA - Sistema de Auditoria Municipal           ║
║                                                                            ║
║     Prado, Bahia | Auditoria Retrospectiva 2016-2026                      ║
║     Sistema Totalmente Independente (SEM FICAR NO CHAT)                   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo "Este script mostra interativamente como usar o sistema sem depender do chat."
echo ""
read -p "Pressione ENTER para começar..." dummy

###############################################################################
# PARTE 1: ESTRUTURA
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 1: ENTENDER A ESTRUTURA                                             ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "A estrutura de arquivos é simples:"
echo ""
echo -e "${GREEN}✓ dashboard_auditoria.html${NC}"
echo "  └─ Abra em qualquer navegador para ver tudo"
echo ""
echo -e "${GREEN}✓ auditoria_automatizada.sh${NC}"
echo "  └─ Script principal que executa TUDO"
echo ""
echo -e "${GREEN}✓ setup_cron.sh${NC}"
echo "  └─ Configura execução automática (sem você fazer nada)"
echo ""
echo -e "${GREEN}✓ logs/${NC}"
echo "  └─ Histórico completo de todas as execuções"
echo ""
echo -e "${GREEN}✓ Propostas_Recuperacao/${NC}"
echo "  └─ Notas em Markdown para Obsidian"
echo ""

read -p "Pressione ENTER para ver a estrutura completa..." dummy

# Mostrar estrutura
echo ""
echo -e "${YELLOW}Visualizando estrutura:${NC}"
echo ""
tree -L 2 -I 'venv|.git' 2>/dev/null || find . -maxdepth 2 -type d ! -path '*/\.*' ! -path '*/venv/*' ! -path '*/.git/*' | sort | head -20

read -p "Pressione ENTER para próxima parte..." dummy

###############################################################################
# PARTE 2: EXECUTAR MANUALMENTE
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 2: EXECUTAR MANUALMENTE (PRIMEIRO TESTE)                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "Agora vamos executar o sistema completamente:"
echo ""
echo -e "${YELLOW}Comando:${NC}"
echo -e "  ${BLUE}bash auditoria_automatizada.sh${NC}"
echo ""
echo "Isso vai:"
echo "  1. Verificar o ambiente (Python, dependências)"
echo "  2. Executar análise retroativa (2016-2026)"
echo "  3. Gerar propostas de recuperação"
echo "  4. Verificar conformidade DOEM"
echo "  5. Sincronizar com GitHub"
echo "  6. Gerar relatório final"
echo ""
echo "Tempo estimado: 2-5 minutos"
echo ""

read -p "Deseja executar agora? (s/n): " executar

if [ "$executar" = "s" ] || [ "$executar" = "S" ]; then
    echo ""
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo "Iniciando execução..."
    echo -e "${YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
    echo ""
    
    # Executar
    bash auditoria_automatizada.sh
    
    echo ""
    echo -e "${GREEN}✅ Execução concluída!${NC}"
else
    echo -e "${YELLOW}Pulando execução...${NC}"
fi

read -p "Pressione ENTER para próxima parte..." dummy

###############################################################################
# PARTE 3: VISUALIZAR RESULTADOS
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 3: VISUALIZAR RESULTADOS                                            ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "Agora você tem MÚLTIPLAS formas de ver os resultados:"
echo ""

# Opção 1: Dashboard
echo -e "${GREEN}📊 OPÇÃO 1: Dashboard HTML (Mais Fácil)${NC}"
echo ""
echo "   Abra em qualquer navegador:"
echo "   ${BLUE}firefox dashboard_auditoria.html${NC}"
echo "   ou"
echo "   ${BLUE}chrome dashboard_auditoria.html${NC}"
echo "   ou"
echo "   ${BLUE}Clique 2x no arquivo no Explorador${NC}"
echo ""

# Opção 2: Logs
echo -e "${GREEN}📋 OPÇÃO 2: Ver Logs${NC}"
echo ""
echo "   Última execução (últimas 20 linhas):"
echo ""
if [ -f logs/auditoria_execucoes.log ]; then
    tail -20 logs/auditoria_execucoes.log | sed 's/^/   /'
else
    echo "   (Nenhum log disponível ainda)"
fi
echo ""

# Opção 3: Arquivos JSON
echo -e "${GREEN}📊 OPÇÃO 3: Arquivos JSON (Dados Brutos)${NC}"
echo ""
echo "   Arquivos de auditoria criados:"
ls -lh auditoria_*.json 2>/dev/null | awk '{print "   " $9 " (" $5 ")"}' || echo "   (Nenhum arquivo gerado ainda)"
echo ""

# Opção 4: Propostas
echo -e "${GREEN}🎯 OPÇÃO 4: Propostas em Markdown (Obsidian)${NC}"
echo ""
echo "   Propostas de recuperação:"
if [ -d Propostas_Recuperacao ]; then
    find Propostas_Recuperacao -name "*.md" -type f | head -5 | sed 's/^/   /'
    COUNT=$(find Propostas_Recuperacao -name "*.md" -type f | wc -l)
    echo "   ... e mais $(($COUNT - 5)) arquivos"
else
    echo "   (Pasta não existe ainda)"
fi
echo ""

read -p "Pressione ENTER para próxima parte..." dummy

###############################################################################
# PARTE 4: CONFIGURAR AUTOMAÇÃO
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 4: CONFIGURAR AUTOMAÇÃO (CRON)                                      ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "O Cron permite que o sistema execute AUTOMATICAMENTE, sem você fazer nada!"
echo ""
echo "Exemplo: Todo dia às 08:00, as auditorias rodam automaticamente"
echo ""
echo "Comando para configurar:"
echo -e "  ${BLUE}bash setup_cron.sh${NC}"
echo ""
echo "Você vai escolher uma frequência:"
echo "  1) 📅 Diária às 00:00"
echo "  2) 📅 Diária às 08:00 ← RECOMENDADO"
echo "  3) 📅 Diária às 16:00"
echo "  4) 📅 Semanal (Segundas)"
echo "  5) 📅 Semanal (Sextas)"
echo "  6) 📅 A Cada 6 Horas"
echo "  7) 📅 A Cada 1 Hora"
echo ""

read -p "Deseja configurar o Cron agora? (s/n): " config_cron

if [ "$config_cron" = "s" ] || [ "$config_cron" = "S" ]; then
    bash setup_cron.sh
else
    echo -e "${YELLOW}Ok, você pode executar depois com: bash setup_cron.sh${NC}"
fi

read -p "Pressione ENTER para próxima parte..." dummy

###############################################################################
# PARTE 5: ABRIR OBSIDIAN
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 5: USAR OBSIDIAN (ANÁLISE PROFUNDA)                                 ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "Obsidian permite visualizar tudo em formato de grafo interligado."
echo ""
echo -e "${YELLOW}Configurar Obsidian (primeira vez):${NC}"
echo ""
echo "  1. Abra Obsidian"
echo "  2. Menu: File → Open Folder as Vault"
echo "  3. Navegue para: D:\\PREFEITURA_PRADO_BA"
echo "  4. Selecione a pasta"
echo "  5. Clique 'Open'"
echo ""
echo -e "${YELLOW}Depois:${NC}"
echo ""
echo "  • Abra: Propostas_Recuperacao/Indice.md"
echo "  • Veja todos os casos encontrados"
echo "  • Clique nos links para ver detalhes"
echo "  • Edite e anote progresso"
echo ""

read -p "Pressione ENTER para próxima parte..." dummy

###############################################################################
# PARTE 6: ROTINA DIÁRIA
###############################################################################

clear
echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║ PARTE 6: SUA ROTINA DIÁRIA (SEM ESFORÇO)                                  ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

echo "Se você configurar o Cron, sua rotina diária fica assim:"
echo ""
echo -e "${GREEN}08:05 (Cron já rodou, você não fez nada!)${NC}"
echo ""
echo "  1️⃣  ${BLUE}Abrir Dashboard${NC}"
echo "     firefox dashboard_auditoria.html"
echo "     Tempo: 30 segundos"
echo ""
echo "  2️⃣  ${BLUE}Revisar Obsidian (se necessário)${NC}"
echo "     File → Open → Propostas_Recuperacao/Indice.md"
echo "     Tempo: 5-10 minutos"
echo ""
echo "  3️⃣  ${BLUE}Ver Logs (se precisar de detalhes)${NC}"
echo "     bash ver_logs.sh"
echo "     Tempo: 1 minuto"
echo ""
echo -e "${YELLOW}TOTAL: 10-15 minutos por dia, completamente INDEPENDENTE do chat!${NC}"
echo ""

read -p "Pressione ENTER para ver o resumo final..." dummy

###############################################################################
# RESUMO FINAL
###############################################################################

clear
echo -e "${GREEN}"
cat << 'EOF'
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                        ✅ DEMONSTRAÇÃO CONCLUÍDA!                          ║
║                                                                            ║
║              Você agora entende o sistema COMPLETAMENTE                   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
EOF
echo -e "${NC}"

echo ""
echo -e "${CYAN}📊 RESUMO DO QUE VOCÊ TEM${NC}"
echo ""
echo "  ✅ Dashboard HTML (visual)"
echo "  ✅ Auditoria Retroativa (dados)"
echo "  ✅ Propostas em Markdown (ação)"
echo "  ✅ Logs Detalhados (histórico)"
echo "  ✅ Execução Automática (cron)"
echo "  ✅ Sincronização GitHub (versionamento)"
echo "  ✅ Integração Obsidian (análise)"
echo ""

echo -e "${CYAN}🎯 PRÓXIMOS PASSOS${NC}"
echo ""
echo "  1️⃣  Abrir Dashboard:"
echo "      ${BLUE}firefox dashboard_auditoria.html${NC}"
echo ""
echo "  2️⃣  Configurar Cron (opcional):"
echo "      ${BLUE}bash setup_cron.sh${NC}"
echo ""
echo "  3️⃣  Abrir Obsidian:"
echo "      File → Open Folder → D:\\PREFEITURA_PRADO_BA"
echo ""
echo "  4️⃣  Acompanhar diariamente:"
echo "      Dashboard (30s) + Obsidian se necessário"
echo ""

echo -e "${CYAN}💡 DICA PRO${NC}"
echo ""
echo "  Ver todos os comandos úteis:"
echo ""
echo "  • Dashboard real-time:"
echo "    ${BLUE}watch -n 300 'cat logs/auditoria_execucoes.log | tail -10'${NC}"
echo ""
echo "  • Executar agora (sem esperar cron):"
echo "    ${BLUE}bash auditoria_automatizada.sh${NC}"
echo ""
echo "  • Ver histórico de auditorias:"
echo "    ${BLUE}ls -lh auditoria_*.json${NC}"
echo ""
echo "  • Ver logs completos:"
echo "    ${BLUE}tail -f logs/auditoria_execucoes.log${NC}"
echo ""

echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""
echo -e "${GREEN}🚀 SISTEMA 100% FUNCIONAL E INDEPENDENTE!${NC}"
echo ""
echo "Você NÃO precisa mais do chat para acompanhar as auditorias."
echo "Tudo roda automaticamente e é visualizado em tempo real."
echo ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo "Para ver documentação completa:"
echo "  ${BLUE}cat README_ACOMPANHAMENTO.md${NC}"
echo ""
