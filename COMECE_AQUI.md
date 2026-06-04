# 🚀 GUIA DE INÍCIO RÁPIDO - 3 Passos para Acompanhar Tudo

**Tempo total:** 5 minutos

---

## ✅ Passo 1: Executar Primeira Vez (2 minutos)

### Comando:
```bash
bash auditoria_automatizada.sh
```

### O que vai acontecer:

```
✅ Verificar Python e dependências
✅ Executar análise retroativa (2016-2026)
✅ Gerar propostas de recuperação (9 categorias)
✅ Verificar conformidade DOEM
✅ Sincronizar com GitHub
✅ Gerar relatório

Total: 2-5 minutos
```

### Saída esperada:

```
╔════════════════════════════════════════════════════════════════╗
║           🔍 AUDITORIA AUTOMATIZADA - SISTEMA COMPLETO        ║
║        Município: Prado, BA | Período: 2016-2026             ║
╚════════════════════════════════════════════════════════════════╝

[2026-06-03 08:00:05] ✅ Python: Python 3.9.5
[2026-06-03 08:00:10] ✅ Auditoria Retroativa concluída
[2026-06-03 08:00:10] ✅ Total de perdas: R$ 29,150,000
[2026-06-03 08:00:15] ✅ Propostas geradas: 9
[2026-06-03 08:00:20] ✅ GitHub sincronizado
[2026-06-03 08:00:22] ✅ Relatório final criado

╔════════════════════════════════════════════════════════════════╗
║                   ✅ AUDITORIA CONCLUÍDA!                     ║
╚════════════════════════════════════════════════════════════════╝
```

---

## ✅ Passo 2: Visualizar Dashboard (30 segundos)

### Comando:
```bash
firefox dashboard_auditoria.html
```

**Ou:** Clique 2x no arquivo `dashboard_auditoria.html` no Explorador

### O que você vê:

```
┌────────────────────────────────────────────────────────────────┐
│ 🔍 Dashboard de Auditoria Municipal - Prado, Bahia             │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  💰 R$ 29.15M        📍 233.4K m²       📋 9 Propostas       │
│  Total a Recuperar   Patrimônio         Criadas              │
│                                                                │
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  ✅ Auditoria Retroativa        [████████████████████] 100%  │
│  ✅ Propostas de Recuperação    [████████████████████] 100%  │
│  ⏳ Conformidade DOEM           [░░░░░░░░░░░░░░░░░░░░]  0%   │
│                                                                │
│  ────────────────────────────────────────────────────────────  │
│                                                                │
│  🚨 Prioridades:                                               │
│  🔴 CRÍTICA (48h) - Comunicar MP, bloquear transações         │
│  🟡 ALTA (1-4 sem) - Emitir notificações, procedimentos      │
│  🟢 MÉDIA (1-6 meses) - Ações judiciais, recuperação         │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## ✅ Passo 3: Abrir Obsidian (1 minuto)

### Configuração (primeira vez):

```
1. Abra Obsidian

2. File → Open Folder as Vault

3. Navegue para: D:\PREFEITURA_PRADO_BA

4. Selecione a pasta

5. Clique "Open"
```

### Depois, abra este arquivo:

```
Propostas_Recuperacao/Indice.md
```

### O que você vê:

```
# 📑 Índice de Propostas de Recuperação

Total a Recuperar: R$ 29.150.000
Período: 2016-2026 (10 anos)

## 💰 Propostas Financeiras

- [[RETRO-FIN-001_Valores_Não_Arrecadados]] - R$ 4.360.000
  (IPTU, aluguéis, multas, taxas)

- [[RETRO-FIN-002_Despesas_Indevidas]] - R$ 1.200.000
  (Pagamentos duplicados, sem licitação)

- [[RETRO-FIN-003_Desvio_Recursos]] - R$ 1.500.000
  (Saúde → Publicidade, Educação → Privado)

## 📍 Propostas Patrimoniais

- [[RETRO-PAT-001_Terrenos_Ociosos]] - 16.500 m² = R$ 5.700.000
- [[RETRO-PAT-002_Desvio_Finalidade]] - R$ 890.000
- [[RETRO-PAT-003_Doacao_Irregular]] - 8.500 m² = R$ 4.250.000
- [[RETRO-PAT-004_Dacao_Pagamento]] - R$ 700.000
- [[RETRO-PAT-005_Loteamento_Limbo]] - 430 lotes = R$ 8.500.000
- [[RETRO-PAT-006_Projeto_Incompleto]] - R$ 2.050.000
```

**Clique em qualquer proposta para ver detalhes completos!**

---

## 🎯 Que Fazer Agora?

### Opção A: Configurar Automação (Recomendado)

```bash
bash setup_cron.sh
```

Escolha frequência (ex: Diária às 8h00)

**Resultado:** Todos os dias às 8h, as auditorias rodam automaticamente, sem você fazer nada!

### Opção B: Ver Logs da Execução

```bash
bash ver_logs.sh
```

Mostra as últimas 20 linhas dos logs:

```
[2026-06-03 08:00:05] ✅ Python: Python 3.9.5
[2026-06-03 08:00:10] ✅ Auditoria Retroativa concluída
[2026-06-03 08:00:10] ✅ Total de perdas: R$ 29,150,000.00
...
```

### Opção C: Executar Demo Interativa

```bash
bash demo_interativa.sh
```

Mostra tudo passo a passo interativamente

---

## 📊 Sua Rotina Diária (Pós-Configuração)

```
08:00 → Cron executa sozinho
        (você está dormindo ou em outra atividade)

08:05 → Você checa:

        1. Abrir Dashboard (30s)
           firefox dashboard_auditoria.html
           Ver status, valores, histórico
           
        2. Revisar Obsidian (5-10 min)
           Se necessário, ver propostas detalhadas
           
        3. Ver logs (1 min)
           Se precisar de informações técnicas
           
TOTAL: 10-15 minutos por dia
STATUS: 100% independente do chat
```

---

## 🔗 Arquivos Importantes

| Arquivo | O Que Faz | Quando Usar |
|---------|-----------|------------|
| `dashboard_auditoria.html` | Visão geral em tempo real | Todo dia (30s) |
| `README_ACOMPANHAMENTO.md` | Documentação completa | Quando precisa entender |
| `FLUXO_INTEGRACAO.md` | Como tudo funciona junto | Para aprender arquitetura |
| `Propostas_Recuperacao/` | Casos detalhados em Markdown | Para análise profunda |
| `logs/auditoria_execucoes.log` | Histórico de tudo | Troubleshooting |

---

## 🎓 Cheat Sheet de Comandos

### Executar Auditoria
```bash
bash auditoria_automatizada.sh
```

### Configurar Automação
```bash
bash setup_cron.sh
```

### Ver Histórico
```bash
bash ver_logs.sh
```

### Executar Demo
```bash
bash demo_interativa.sh
```

### Ver Todas as Tarefas Cron
```bash
crontab -l
```

### Remover Tarefa Cron
```bash
crontab -r
```

### Ver Últimos Relatórios
```bash
ls -lh relatorios_auditoria/
tail -f logs/auditoria_execucoes.log
```

### Abrir Obsidian
```
Abra Obsidian
File → Open Folder as Vault
D:\PREFEITURA_PRADO_BA
```

---

## ✅ Status Depois dos 3 Passos

- ✅ Sistema testado e funcional
- ✅ Dashboard visível em navegador
- ✅ Obsidian configurado com propostas
- ✅ Pronto para automação

**Próximo passo:** `bash setup_cron.sh` para rodar automaticamente

---

## 🚨 Se Algo Não Funcionar

### Terminal mostra erro em Python?
```bash
pip3 install requests beautifulsoup4
bash auditoria_automatizada.sh
```

### Dashboard não aparece?
```bash
# Verificar se o arquivo existe
ls -l dashboard_auditoria.html

# Tentar com outro navegador
chrome dashboard_auditoria.html
```

### Obsidian não abre pasta?
```
File → Open Folder as Vault
Selecione: D:\PREFEITURA_PRADO_BA (não uma subfolder)
```

### Cron não executa?
```bash
# Verificar status
sudo systemctl status cron

# Iniciar se parado
sudo systemctl start cron

# Ver tarefas
crontab -l
```

---

## 💡 Dicas Pro

### 1. Dashboard em Tempo Real
```bash
watch -n 300 'firefox dashboard_auditoria.html'
```
(Atualiza automáticamente a cada 5 minutos)

### 2. Logs em Tempo Real
```bash
tail -f logs/auditoria_execucoes.log
```
(Vê cada linha conforme aparece)

### 3. Sincronizar Obsidian
```
Settings → Sync
Enable Vault Sync
(Acessa de qualquer dispositivo)
```

### 4. Exportar Dashboard para PDF
```bash
wkhtmltopdf dashboard_auditoria.html dashboard.pdf
```

---

## 🎯 Resumo em 1 Minuto

```
✅ Passo 1: bash auditoria_automatizada.sh
           (Executa análises, cria dados)

✅ Passo 2: firefox dashboard_auditoria.html
           (Visualiza resultados)

✅ Passo 3: Abrir Obsidian → Propostas_Recuperacao/Indice.md
           (Vê detalhes)

🎁 BÔNUS: bash setup_cron.sh
          (Automação futura)

RESULTADO: Sistema 100% funcional, independente, automático!
```

---

## 📞 Documentação Completa

Para entender cada parte em detalhes:

- **Auditoria Retroativa:** [AUDITORIA_RETROATIVA_GUIA.md](AUDITORIA_RETROATIVA_GUIA.md)
- **Conformidade DOEM:** [AUDITORIA_CONFORMIDADE_GUIA.md](AUDITORIA_CONFORMIDADE_GUIA.md)
- **Acompanhamento:** [README_ACOMPANHAMENTO.md](README_ACOMPANHAMENTO.md)
- **Integração:** [FLUXO_INTEGRACAO.md](FLUXO_INTEGRACAO.md)
- **Sistema Completo:** [SISTEMA_AUDITORIA_RETROATIVA.md](SISTEMA_AUDITORIA_RETROATIVA.md)

---

## 🚀 Comece Agora!

```bash
# 1️⃣ EXECUTE
bash auditoria_automatizada.sh

# 2️⃣ VISUALIZE
firefox dashboard_auditoria.html

# 3️⃣ ANALISE
# Abra Obsidian → Propostas_Recuperacao/Indice.md

# ✅ PRONTO!
```

**Tempo total:** 5 minutos  
**Resultado:** Sistema completo, independente e funcional  
**Frequência:** Automática (depois que configurar cron)

---

**Data:** 3 de junho de 2026  
**Versão:** 1.0  
**Status:** ✅ Pronto para Usar Agora!  
**Próximo:** Configurar cron com `bash setup_cron.sh`
