# 🚀 GUIA RÁPIDO - Sistema de Auditoria de Conformidade

## ⚡ Em 3 Passos

### 1️⃣ **Executar Auditoria Completa**
```bash
bash auditoria_completa.sh
```

### 2️⃣ **Revisar Relatório**
- Procure por: `auditoria_conformidade_YYYYMMDD_HHMMSS.json`
- Abra no editor ou no Obsidian

### 3️⃣ **Implementar Propostas**
- Abra: `Propostas_de_Correcao/Indice.md` no Obsidian
- Siga as propostas por ordem de prioridade

---

## 📋 O Que o Sistema Faz

```
🌐 DOEM (Diário Oficial)
        ↓
    🔍 RASPA dados
        ↓
    📊 ANALISA conformidade em 6 áreas:
       ✓ Administrativa
       ✓ Jurídica
       ✓ Legislativa
       ✓ Financeira
       ✓ Política
       ✓ Social
        ↓
    ⚠️  IDENTIFICA problemas
        ↓
    💡 PROPÕE correções
        ↓
    📝 GERA notas no Obsidian
```

---

## 🎯 Áreas Analisadas

### 🏛️ **ADMINISTRATIVA**
- Publicação de atos no DOEM
- Nomenclatura padronizada
- Assinatura digital

### ⚖️ **JURÍDICA**
- Conformidade com leis federais/estaduais
- Fundamentação legal

### 📜 **LEGISLATIVA**
- Processo legislativo correto
- Sanção do Executivo

### 💰 **FINANCEIRA** (Mais crítica)
- Lei de Responsabilidade Fiscal (LRF)
- Cobertura orçamentária
- Limite de despesas
- Transparência fiscal

### 🎯 **POLÍTICA**
- Nepotismo (parentes até 3º grau)
- Conflitos de interesse

### 🤝 **SOCIAL**
- Políticas públicas
- Inclusão e acessibilidade

---

## 📊 Exemplos de Conformidade

### ✅ CONFORME
```
Lei Nº 123/2024 - Empenho
Fundamentação: Art. 35 da Lei Federal 1234/56
Orçamento: Dotação 123456 - R$ 50.000,00 ✓
Assinado: Prefeito João Silva (Digital)
Publicado: DOEM 01/06/2026
Resultado: 95% de conformidade ✅
```

### ❌ NÃO CONFORME
```
Nomeação de Maria Silva
Parentesco: Filha do Secretário Pedro Silva
Regra: Proibição de nepotismo
Proposta: REVISAR NOMEAÇÃO - Possível conflito
Resultado: 40% de conformidade ❌
```

---

## 🔥 Prioridades de Ação

| Nível | Prazo | Exemplos |
|-------|-------|----------|
| 🔴 **CRÍTICA** | **48 horas** | Nepotismo, despesa sem orçamento, lei não sancionada |
| 🟡 **MÉDIA** | **7 dias** | Nomenclatura incorreta, falta fundamentação |
| 🟢 **BAIXA** | **30 dias** | Melhorias de transparência, acessibilidade |

---

## 📁 Arquivos Importantes

| Arquivo | O Que Faz |
|---------|-----------|
| `auditoria_completa.sh` | Executa tudo automaticamente |
| `auditoria_conformidade.py` | Faz análise técnica |
| `gerar_propostas_obsidian.py` | Cria notas do Obsidian |
| `gabarito_compliance_expandido.json` | Define regras de conformidade |
| `AUDITORIA_CONFORMIDADE_GUIA.md` | Documentação completa |
| `Propostas_de_Correcao/` | Pasta com propostas de ação |

---

## 🔄 Fluxo Recomendado

```
Semana 1: AUDITORIA INICIAL
├─ Executar: bash auditoria_completa.sh
├─ Revisar relatório
└─ Priorizar ações

Semana 2-3: IMPLEMENTAR CORREÇÕES
├─ Ações críticas (48h)
├─ Ações médias (7 dias)
└─ Documentar mudanças

Semana 4: RE-AUDITORIA
├─ Executar novamente
├─ Validar conformidade
└─ Gerar relatório de progresso

Toda semana: ACOMPANHAMENTO
└─ bash auditoria_completa.sh
```

---

## 💻 Comandos Rápidos

### Executar apenas análise
```bash
python3 auditoria_conformidade.py
```

### Gerar propostas do último relatório
```bash
python3 gerar_propostas_obsidian.py
```

### Especificar arquivo de relatório
```bash
python3 gerar_propostas_obsidian.py auditoria_conformidade_20260603_104530.json
```

### Ver último arquivo gerado
```bash
ls -lt auditoria_conformidade_*.json | head -1
```

---

## 📌 Checklist de Implementação

- [ ] Instalar dependências: `pip3 install requests beautifulsoup4`
- [ ] Executar auditoria: `bash auditoria_completa.sh`
- [ ] Abrir Obsidian vault: `D:\PREFEITURA_PRADO_BA`
- [ ] Revisar Propostas_de_Correcao/Indice.md
- [ ] Priorizar ações por severidade
- [ ] Implementar correções críticas
- [ ] Documentar mudanças
- [ ] Re-executar auditoria
- [ ] Validar conformidade
- [ ] Agendar próxima auditoria

---

## 🆘 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'requests'"
```bash
pip3 install requests beautifulsoup4
```

### Erro: "Connection refused" ao acessar DOEM
- Verifique conexão com internet
- Verifique URL: https://doem.org.br/ba/prado
- Tente depois de alguns minutos

### Scripts sem permissão de execução
```bash
chmod +x *.sh *.py
```

### Obsidian não encontra pasta
- Abra: `File → Open Folder as Vault`
- Navegue até: `D:\PREFEITURA_PRADO_BA`

---

## 📚 Recursos Adicionais

- [DOEM Prado/BA](https://doem.org.br/ba/prado)
- [Lei de Responsabilidade Fiscal](http://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm)
- [Lei de Nepotismo](http://www.tce.sp.gov.br/institucional/legislacao/decreto-7203-04)
- [[AUDITORIA_CONFORMIDADE_GUIA]]

---

**Versão:** 1.0  
**Última atualização:** 2026-06-03  
**Próxima revisão:** 2026-06-10

🎯 **Começar agora:**
```bash
bash auditoria_completa.sh
```
