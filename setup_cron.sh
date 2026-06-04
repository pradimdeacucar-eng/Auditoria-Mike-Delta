#!/bin/bash

###############################################################################
# CONFIGURADOR DE CRON - Agendamento Automático de Auditorias
# Este script configura a execução automática das auditorias
###############################################################################

set -e

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CRON_FILE="/tmp/auditoria_cron_temp.txt"

echo -e "${BLUE}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║  ⏰ CONFIGURADOR DE CRON - Agendamento de Auditorias         ║"
echo "╚═══════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Menu de opções
echo "Escolha a frequência de execução:"
echo ""
echo "1) 📅 Diária (0h00 - todos os dias)"
echo "2) 📅 Diária (8h00 - todos os dias)"
echo "3) 📅 Diária (16h00 - todos os dias)"
echo "4) 📅 Semanal (Segundas às 0h00)"
echo "5) 📅 Semanal (Sextas às 20h00)"
echo "6) 📅 A Cada 6 Horas (Contínuo)"
echo "7) 📅 A Cada 1 Hora (Monitoramento contínuo)"
echo "0) ❌ Cancelar"
echo ""
read -p "Escolha uma opção [0-7]: " escolha

case $escolha in
    1)
        CRON_TIME="0 0 * * *"
        DESC="Diária às 0h00"
        ;;
    2)
        CRON_TIME="0 8 * * *"
        DESC="Diária às 8h00"
        ;;
    3)
        CRON_TIME="0 16 * * *"
        DESC="Diária às 16h00"
        ;;
    4)
        CRON_TIME="0 0 * * 1"
        DESC="Segundas às 0h00"
        ;;
    5)
        CRON_TIME="0 20 * * 5"
        DESC="Sextas às 20h00"
        ;;
    6)
        CRON_TIME="0 */6 * * *"
        DESC="A Cada 6 Horas"
        ;;
    7)
        CRON_TIME="0 * * * *"
        DESC="A Cada 1 Hora"
        ;;
    *)
        echo -e "${RED}Cancelado${NC}"
        exit 0
        ;;
esac

echo ""
echo -e "${GREEN}✅ Frequência selecionada: ${DESC}${NC}"
echo -e "${BLUE}Padrão Cron: ${CRON_TIME}${NC}"
echo ""

# Criar entrada de cron
CRON_COMMAND="cd $SCRIPT_DIR && bash auditoria_automatizada.sh >> logs/cron_execucoes.log 2>&1"

# Backup do crontab atual
echo -e "${YELLOW}ℹ️  Fazendo backup do crontab atual...${NC}"
crontab -l > "$CRON_FILE.backup" 2>/dev/null || true

# Verificar se job já existe
if crontab -l 2>/dev/null | grep -q "auditoria_automatizada.sh"; then
    echo -e "${YELLOW}⚠️  Já existe uma tarefa de auditoria no cron!${NC}"
    echo ""
    read -p "Deseja remover a tarefa anterior? (s/n): " remover
    
    if [ "$remover" = "s" ] || [ "$remover" = "S" ]; then
        crontab -l | grep -v "auditoria_automatizada.sh" > "$CRON_FILE"
        crontab "$CRON_FILE"
        echo -e "${GREEN}✅ Tarefa anterior removida${NC}"
    fi
fi

# Adicionar nova entrada
(crontab -l 2>/dev/null || true; echo "$CRON_TIME $CRON_COMMAND") | crontab -

echo -e "${GREEN}✅ Tarefa agendada com sucesso!${NC}"
echo ""

# Mostrar crontab
echo "📋 Tarefas agendadas (crontab):"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
crontab -l | tail -5
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Info do cron service
echo "ℹ️  Status do serviço cron:"
echo ""

if command -v systemctl &> /dev/null; then
    if systemctl is-active --quiet cron; then
        echo -e "${GREEN}✅ Serviço cron ativo${NC}"
    else
        echo -e "${RED}❌ Serviço cron inativo!${NC}"
        echo "Para ativar: sudo systemctl start cron"
    fi
else
    echo "⚠️  systemctl não disponível (verifica manualmente)"
fi

echo ""
echo "📁 Logs de execução serão salvos em:"
echo "   $SCRIPT_DIR/logs/cron_execucoes.log"
echo ""

# Criar diretório de logs se não existir
mkdir -p "$SCRIPT_DIR/logs"

# Script para visualizar logs
cat > "$SCRIPT_DIR/ver_logs.sh" << 'EOFSCRIPT'
#!/bin/bash
echo "📋 Últimas execuções (logs/cron_execucoes.log):"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ -f logs/cron_execucoes.log ]; then
    tail -20 logs/cron_execucoes.log
else
    echo "Nenhum log disponível ainda. Aguardando primeira execução..."
fi
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
EOFSCRIPT

chmod +x "$SCRIPT_DIR/ver_logs.sh"

echo "🎯 Próximos Passos:"
echo ""
echo "1. Aguardar o próximo horário agendado"
echo "2. Ver logs de execução:"
echo "   bash ver_logs.sh"
echo ""
echo "3. Ver todas as tarefas cron:"
echo "   crontab -l"
echo ""
echo "4. Remover tarefa (se necessário):"
echo "   crontab -r"
echo ""

echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${GREEN}✅ Cron configurado com sucesso!${NC}"
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"

# Cleanup
rm -f "$CRON_FILE" "$CRON_FILE.backup"
