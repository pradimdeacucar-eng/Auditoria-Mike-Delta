# 📊 GUIA DE ACOMPANHAMENTO - Sistema de Auditoria Independente

## 🎯 O Problema

Você NÃO quer ficar aqui no chat para acompanhar as auditorias. Precisa de:

- ✅ **Dashboard visual** mostrando status em tempo real
- ✅ **Execução automática** sem precisar digitar comandos
- ✅ **Histórico de logs** para revisar o que aconteceu
- ✅ **Integração Obsidian** para análise visual
- ✅ **Versionamento GitHub** para segurança

## 🚀 Solução: Fluxo de Ponta a Ponta

```
[Cron] → [auditoria_automatizada.sh] → [Python Scripts] → [JSON + Markdown]
  ↓                                                            ↓
Executa                                              Dashboard + Obsidian
automaticamente                                      Visão centralizada
```

---

## 📁 Estrutura de Arquivos

```
PREFEITURA_PRADO_BA/
├── 📊 dashboard_auditoria.html          ← ABRA AQUI para visualizar
├── ⚙️ auditoria_automatizada.sh         ← Script principal
├── ⏰ setup_cron.sh                      ← Configurar agendamento
├── 📋 ver_logs.sh                        ← Ver histórico
├── 📚 README_ACOMPANHAMENTO.md           ← Este arquivo
│
├── 📂 logs/                              ← Histórico de execuções
│   ├── auditoria_execucoes.log          (logs da execução)
│   ├── cron_execucoes.log               (logs do agendamento)
│   ├── retroativa_output.log            (saída Python)
│   ├── conformidade_output.log          (saída Python)
│   └── propostas_output.log             (saída Python)
│
├── 📂 relatorios_auditoria/             ← Relatórios finais
│   └── relatorio_YYYYMMDD_HHMMSS.md    (cada execução)
│
├── 📂 Propostas_Recuperacao/            ← Integração Obsidian
│   ├── Indice.md                        (visão geral)
│   ├── RETRO-FIN-001_*.md              (propostas financeiras)
│   ├── RETRO-FIN-002_*.md
│   ├── RETRO-FIN-003_*.md
│   ├── RETRO-PAT-001_*.md              (propostas patrimoniais)
│   ├── RETRO-PAT-002_*.md
│   └── ... (mais 4 categorias)
│
└── 📂 Propostas_de_Correcao/           ← Conformidade DOEM
    └── (Gerado pela auditoria_conformidade.py)
```

---

## 🎯 COMO ACOMPANHAR SEM FICAR NO CHAT

### ✅ Opção 1: Dashboard HTML (Mais Fácil)

**Abra em qualquer navegador:**

```bash
# Linux/WSL
firefox dashboard_auditoria.html
# ou
chrome dashboard_auditoria.html
# ou simplesmente clique 2x no arquivo no Explorador

# Windows (cmd)
start dashboard_auditoria.html
```

**O que você verá:**

- 📊 Estatísticas consolidadas (R$ 29.15M, 233.4K m², etc)
- ⚙️ Histórico de execuções com status
- 📅 Timeline de progresso
- 🎯 Prioridades de ação
- 🔗 Links para Obsidian, GitHub, etc

**Atualização Automática:** A cada 5 minutos (ou clique F5 manualmente)

---

### ✅ Opção 2: Obsidian Vault (Mais Análise)

**Configurar Obsidian uma vez:**

```
1. Abra Obsidian
2. Menu: File → Open Folder as Vault
3. Navegue para: D:\PREFEITURA_PRADO_BA
4. Selecione a pasta
5. Clique "Open"
```

**Agora você tem:**

- 🧠 Todas as propostas em notas interligadas
- 🔗 Links bi-direcionais mostrando relações
- 📊 Tabelas com Dataview (se configurado)
- ✏️ Possibilidade de editar e anotar progresso
- 📱 Sincronização entre dispositivos (se usar Obsidian Sync)

**Navegar:**

```
Pasta: Propostas_Recuperacao/
├─ Indice.md (COMECE AQUI)
├─ RETRO-FIN-001_Valores_Não_Arrecadados.md
├─ RETRO-PAT-005_Loteamento_Limbo.md
└─ ... (mais 7 propostas)

Cada proposta tem:
- Descrição detalhada
- Plano em 4 fases
- Responsáveis
- Prazos
- Checklist
```

---

### ✅ Opção 3: Ver Logs no Terminal (Técnico)

**Ver logs da última execução:**

```bash
# Atalho criado automaticamente
bash ver_logs.sh

# Ou ver manualmente
tail -50 logs/auditoria_execucoes.log

# Ver específico
tail -20 logs/retroativa_output.log
tail -20 logs/conformidade_output.log
tail -20 logs/cron_execucoes.log
```

**Cada log mostra:**

- Timestamp exato
- Etapa executada (✅/❌)
- Valores encontrados
- Erros (se houver)
- Tempo de execução

---

## ⏰ AGENDAMENTO AUTOMÁTICO

### Configurar Execução Automática

**PRIMEIRA VEZ:**

```bash
bash setup_cron.sh
```

**Você escolhe:**

```
1) 📅 Diária às 0h00
2) 📅 Diária às 8h00
3) 📅 Diária às 16h00
4) 📅 Semanal (Segunda às 0h00)
5) 📅 Semanal (Sexta às 20h00)
6) 📅 A Cada 6 Horas
7) 📅 A Cada 1 Hora (Contínuo)
```

**Exemplo:** Escolher opção **2** = Executa todos os dias às 8h00

### Verificar se está Agendado

```bash
# Ver todas as tarefas
crontab -l

# Você verá algo como:
# 0 8 * * * cd /mnt/d/PREFEITURA_PRADO_BA && bash auditoria_automatizada.sh >> logs/cron_execucoes.log 2>&1
```

### Remover Agendamento (se necessário)

```bash
crontab -r
```

---

## 🔄 FLUXO REAL DE EXECUÇÃO

### Quando você liga o computador (ou no horário agendado):

```
⏰ 08:00 (horário agendado)
    ↓
🏃 Cron executa: bash auditoria_automatizada.sh
    ↓
📝 Etapa 1: Verificar ambiente (Python, dependências)
📝 Etapa 2: Executar auditoria_retroativa.py
    ├─ Analisa 9 categorias de perdas
    ├─ Gera: auditoria_retroativa_*.json
    └─ Registra tempo em: logs/
    ↓
📝 Etapa 3: Executar gerar_propostas_recuperacao.py
    ├─ Converte JSON em Markdown
    ├─ Cria: Propostas_Recuperacao/*.md
    └─ Registra tempo em: logs/
    ↓
📝 Etapa 4: Executar auditoria_conformidade.py (DOEM)
    ├─ Raspa https://doem.org.br/ba/prado
    ├─ Gera: auditoria_conformidade_*.json
    └─ Registra tempo em: logs/
    ↓
📝 Etapa 5: Sincronizar com GitHub
    ├─ git add .
    ├─ git commit -m "Auditoria Automatizada - 2026-06-03 08:00"
    └─ git push origin main
    ↓
📝 Etapa 6: Gerar Relatório
    └─ Cria: relatorios_auditoria/relatorio_*.md
    ↓
✅ CONCLUÍDO EM < 5 MINUTOS
    ↓
📊 Dashboard atualizado
🧠 Obsidian sincronizado
📝 Logs salvos
🐙 GitHub versionado
```

---

## 🎯 ROTINA DIÁRIA (SEM ESFORÇO)

### Seu workflow típico:

```
08:05 (após execução automática)
  ↓
1️⃣ Abrir: firefox dashboard_auditoria.html
  ├─ Ver status da última execução
  ├─ Verificar se tem erros
  └─ Notar se novos achados foram feitos
  
  (demora: 30 segundos)
  ↓
2️⃣ Se necessário, abrir Obsidian
  ├─ Pasta: Propostas_Recuperacao/Indice.md
  ├─ Revisar novos casos
  ├─ Atualizar status de ações
  └─ Documentar progresso
  
  (demora: 5-10 minutos)
  ↓
3️⃣ Se necessário, ver logs técnicos
  └─ bash ver_logs.sh
  
  (demora: 1 minuto)
```

**TOTAL: 10-15 minutos por dia, completamente independente do chat!**

---

## 🔍 INTERPRETANDO O DASHBOARD

### Estatísticas no Topo

```
💰 Total a Recuperar: R$ 29.15M
   → Soma de todas as perdas detectadas

📍 Patrimônio Mapeado: 233.4K m²
   → Área de terras identificadas

📋 Propostas Criadas: 9
   → Categorias de recuperação

✅ Conformidade: XX%
   → Score das publicações DOEM analisadas
```

### Histórico de Execuções

```
✅ Sucesso     → Tudo correu bem
⏳ Agendada    → Próxima execução programada
❌ Erro       → Verificar logs
```

### Timeline

```
✅ Etapa 1    Auditoria Retroativa concluída
✅ Etapa 2    Propostas geradas
⏳ Etapa 3    Conformidade (próxima execução)
⏳ Etapa 4    Implementação (ação manual)
```

### Prioridades

```
🔴 CRÍTICAS (48h)     → Ação imediata necessária
🟡 ALTAS (1-4 sem)    → Próximas semanas
🟢 MÉDIAS (1-6 meses) → Planejamento
```

---

## 📊 INTERPRETANDO OS LOGS

### Log Success

```
[2026-06-03 08:00:00] ℹ️  Iniciando ciclo de auditoria automatizado...
[2026-06-03 08:00:01] ✅ Python: Python 3.9.5
[2026-06-03 08:00:05] ✅ Auditoria Retroativa concluída
[2026-06-03 08:00:05] ✅ Total de perdas: R$ 29,150,000.00
[2026-06-03 08:00:10] ✅ Propostas de Recuperação concluídas
[2026-06-03 08:00:10] ✅ Total de propostas: 9
[2026-06-03 08:00:12] ✅ Commit criado: Auditoria Automatizada - 2026-06-03 08:00
[2026-06-03 08:00:13] ✅ Enviado para GitHub com sucesso
[2026-06-03 08:00:14] ✅ Script finalizado com sucesso!
```

→ Tudo OK, nada a fazer

### Log com Warning

```
[2026-06-03 08:00:20] ⚠️  Dependência Python ausente: requests
[2026-06-03 08:00:25] ✅ Instalando dependências...
[2026-06-03 08:00:35] ✅ Dependência instalada
```

→ Script auto-recuperou, tudo bem

### Log com Error

```
[2026-06-03 08:00:05] ❌ Erro na auditoria de conformidade
[2026-06-03 08:00:05] ⚠️  Erro: Connection refused
```

→ Problema de rede ou servidor DOEM offline. Próxima tentativa funcionará.

---

## 🐙 GITHUB - Versionamento Automático

### O que é feito automaticamente:

```bash
# Cada execução:
git add .
git commit -m "🔍 Auditoria Automatizada - 2026-06-03 08:00"
git push origin main
```

### Para ver o histórico:

```bash
# Ultimos 10 commits
git log --oneline -10

# Diferenças desde último commit
git diff HEAD~1

# Ver arquivo específico no tempo
git show HEAD~1:Propostas_Recuperacao/Indice.md
```

### Restaurar versão anterior (se necessário)

```bash
# Desfazer último commit (mantém arquivos)
git reset --soft HEAD~1

# Voltar a versão anterior completamente
git reset --hard HEAD~1
```

---

## 🚨 TROUBLESHOOTING

### Problema: Cron não está rodando

**Verificar:**

```bash
# Status do serviço cron
sudo systemctl status cron

# Se parado, iniciar
sudo systemctl start cron

# Ver erros de cron
grep CRON /var/log/syslog | tail -20
```

### Problema: Python dá erro

**Verificar:**

```bash
# Qual versão
python3 --version

# Dependências instaladas?
pip3 list | grep -E "requests|beautifulsoup"

# Se faltar, instalar
pip3 install requests beautifulsoup4
```

### Problema: GitHub não sincroniza

**Verificar:**

```bash
# Git configurado?
git config --global user.name
git config --global user.email

# Remoto configurado?
git remote -v

# Se não, configurar
git remote add origin https://github.com/seu-usuario/repo.git
git branch -M main
git push -u origin main
```

### Problema: Dashboard não atualiza

**Solução:**

```bash
# F5 para recarregar
# Ou feche e abra novamente
# Ou abra em outro navegador

# Verificar se arquivos JSON estão sendo criados
ls -lt auditoria_retroativa_*.json | head -3
```

---

## 💡 DICAS PRO

### 1. Visualizar execução em tempo real

```bash
# Terminal 1: Ver logs conforme acontecem
tail -f logs/auditoria_execucoes.log

# Terminal 2: Executar
bash auditoria_automatizada.sh

# Você vê tudo em tempo real!
```

### 2. Executar manualmente (sem esperar cron)

```bash
# Forçar execução agora
bash auditoria_automatizada.sh

# Vai rodar em ~2-5 minutos
```

### 3. Exportar relatório para PDF

```bash
# Instalar (primeira vez)
sudo apt-get install wkhtmltopdf

# Converter HTML para PDF
wkhtmltopdf dashboard_auditoria.html dashboard_auditoria.pdf

# Enviar por email, etc
```

### 4. Enviar notificação quando terminar

Editar `auditoria_automatizada.sh` e adicionar ao final:

```bash
# Enviar email
echo "Auditoria concluída!" | mail -s "Auditoria Municipal" seu@email.com

# Ou enviar webhook
curl -X POST https://seu-webhook.com/notify \
  -d '{"status": "concluido", "valor": 29150000}'
```

---

## 📱 ACESSAR DE QUALQUER LUGAR

### Compartilhar Dashboard na Rede

```bash
# Instalar servidor HTTP simples
python3 -m http.server 8000

# Acessar de outro computador na rede:
# http://seu-ip:8000/dashboard_auditoria.html
# http://seu-computador.local:8000/dashboard_auditoria.html
```

### Sincronizar Obsidian com Dispositivos

```
Obsidian → Settings → Sync
  → Enable Vault Sync
  → Acesso em todos os dispositivos
```

### Ver Logs Remotamente

```bash
# Servidor SSH (se tiver)
ssh usuario@seu-servidor

cd /mnt/d/PREFEITURA_PRADO_BA
bash ver_logs.sh
```

---

## 🎓 RESUMO: O QUE FAZER AGORA

### Passo 1: Testar Tudo

```bash
# Executar uma vez manualmente
bash auditoria_automatizada.sh

# Deve levar 2-5 minutos
# Ver logs
bash ver_logs.sh
```

### Passo 2: Configurar Automação

```bash
# Configurar cron para rodar automaticamente
bash setup_cron.sh

# Escolher frequência (ex: diária às 8h)
```

### Passo 3: Abrir Dashboard

```bash
# Abrir em navegador
firefox dashboard_auditoria.html

# Vai mostrar status, histórico, próximas ações
```

### Passo 4: Usar Obsidian

```bash
# Obsidian → Open Folder
# Selecionar: D:\PREFEITURA_PRADO_BA
# Abrir: Propostas_Recuperacao/Indice.md
```

### Passo 5: Acompanhar

```bash
# Todos os dias às 8h (ou horário escolhido):
# 1. Abrir dashboard_auditoria.html
# 2. Revisar Obsidian se necessário
# 3. Ver logs se houver dúvidas

# Tudo 100% automático!
```

---

## 🔗 Arquivos Relacionados

- [SISTEMA_AUDITORIA_RETROATIVA.md](SISTEMA_AUDITORIA_RETROATIVA.md) - Sistema retroativo
- [AUDITORIA_RETROATIVA_GUIA.md](AUDITORIA_RETROATIVA_GUIA.md) - Guia detalhado
- [AUDITORIA_CONFORMIDADE_GUIA.md](AUDITORIA_CONFORMIDADE_GUIA.md) - Conformidade DOEM
- [GUIA_RAPIDO.md](GUIA_RAPIDO.md) - Início rápido

---

## ✅ Checklist Final

- [ ] Testei execução manual: `bash auditoria_automatizada.sh`
- [ ] Vi os logs: `bash ver_logs.sh`
- [ ] Abri o dashboard: `firefox dashboard_auditoria.html`
- [ ] Configurei cron: `bash setup_cron.sh`
- [ ] Abri Obsidian com a pasta como Vault
- [ ] Revisei Propostas_Recuperacao/Indice.md
- [ ] Verifiquei GitHub (git log)
- [ ] Entendi o fluxo completo

---

## 🎯 Resultado Final

**Agora você tem:**

✅ **Dashboard HTML** - Visualizar em qualquer navegador  
✅ **Obsidian Vault** - Análise detalhada em notas  
✅ **Execução Automática** - Cron roda sem intervenção  
✅ **Logs Detalhados** - Histórico completo de tudo  
✅ **GitHub Sincronizado** - Versionamento e backup  
✅ **Relatórios MD** - Documentação de cada execução  

**Tudo funciona INDEPENDENTEMENTE do chat!** 🚀

---

**Data:** 3 de junho de 2026  
**Versão:** 1.0  
**Status:** ✅ Pronto para Uso Independente
