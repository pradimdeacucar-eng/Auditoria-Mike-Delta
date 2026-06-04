# 🔍 Sistema de Auditoria Automática de Conformidade Legal

## 📋 Visão Geral

Sistema inteligente que raspa publicações do **DOEM (Diário Oficial do Estado da Bahia)** e analisa automaticamente conformidade legal em 6 áreas:

- ✅ **Administrativa** - Atos, decretos, portarias
- ✅ **Jurídica** - Conformidade com legislação
- ✅ **Legislativa** - Processos de lei
- ✅ **Financeira** - LRF, orçamento, despesas
- ✅ **Política** - Nepotismo, conflitos de interesse
- ✅ **Social** - Políticas públicas, inclusão

---

## 🚀 Como Usar

### 1. Executar Auditoria Completa

```bash
python3 auditoria_conformidade.py
```

**Saída esperada:**
- ✅/⚠️/❌ Status de cada publicação
- 📊 Relatório consolidado
- 📁 Arquivo JSON com detalhes
- 💡 Recomendações de ações

### 2. Exemplos de Conformidades Verificadas

#### Administrativa
- ✓ Publicação de atos no DOEM
- ✓ Nomenclatura padronizada
- ✓ Assinatura digital

#### Jurídica
- ✓ Conformidade com leis federais
- ✓ Conformidade com leis estaduais
- ✓ Fundamentação legal presente

#### Legislativa
- ✓ Processo legislativo correto
- ✓ Consulta pública realizada
- ✓ Sanção do Executivo

#### Financeira
- ✓ Lei de Responsabilidade Fiscal
- ✓ Cobertura orçamentária
- ✓ Limite de despesas
- ✓ Publicação de despesas
- ✓ Transparência fiscal

#### Política
- ✓ Sem nepotismo (parentes até 3º grau)
- ✓ Sem conflito de interesses
- ✓ Equilíbrio político

#### Social
- ✓ Planejamento de políticas sociais
- ✓ Acesso à informação
- ✓ Participação cidadã
- ✓ Políticas de inclusão

---

## 📊 Interpretando Resultados

### Pontuação
- **90-100%**: 🟢 Excelente
- **70-89%**: 🟡 Bom
- **50-69%**: 🔴 Regular
- **0-49%**: ⛔ Crítico

### Severidade
- **Alta** (🔴): Ação imediata necessária
- **Média** (🟡): Revisar em curto prazo
- **Baixa** (🟢): Melhorias recomendadas

---

## 💡 Propostas de Correção Automáticas

O sistema gera propostas específicas para cada problema:

```
ID: ADM-001 | Severidade: ALTA
Problema: Publicação de Atos Administrativos
Proposta: Revisar publicação no DOEM e padronizar nomenclatura de atos

ID: FIN-001 | Severidade: ALTA
Problema: Lei de Responsabilidade Fiscal
Proposta: Adequar despesa à legislação fiscal e garantir transparência

ID: POL-001 | Severidade: ALTA
Problema: Proibição de Nepotismo
Proposta: Revisar nomeações e garantir conformidade com lei de nepotismo
```

---

## 🔄 Fluxo de Trabalho Sugerido

1. **Executar Auditoria** → Gera relatório com problemas
2. **Revisar Relatório** → Identificar prioridades
3. **Implementar Propostas** → Corrigir publicações
4. **Re-auditar** → Validar correções
5. **Documentar** → Registrar no Obsidian

---

## 📁 Arquivos Gerados

```
auditoria_conformidade_YYYYMMDD_HHMMSS.json
├── relatorio_consolidado
│   ├── total_publicacoes
│   ├── total_inconformidades
│   ├── categorias
│   ├── severidades
│   ├── pontuacao_media
│   └── recomendacoes
└── detalhes_publicacoes
    ├── id_publicacao
    ├── inconformidades
    ├── pontuacao
    ├── categoria_risco
    └── propostas
```

---

## 🎯 Casos de Uso

### Auditoria Administrativa
```bash
# Identifica atos não publicados corretamente
python3 auditoria_conformidade.py
# Proposta: Publicar no DOEM com nomenclatura correta
```

### Conformidade Fiscal
```bash
# Detecta despesas sem cobertura orçamentária
python3 auditoria_conformidade.py
# Proposta: Obter aprovação orçamentária antes
```

### Risco Legal
```bash
# Identifica possível nepotismo em nomeações
python3 auditoria_conformidade.py
# Proposta: Revisar vínculo de parentesco
```

---

## 🔧 Personalização

### Adicionar Nova Regra

Edit `gabarito_compliance_expandido.json`:

```json
{
  "id": "ADM-004",
  "nome": "Sua Regra",
  "descricao": "Descrição da regra",
  "severidade": "alta",
  "criterio": "seu_criterio"
}
```

### Adicionar Verificação

Edit `auditoria_conformidade.py` - função `verificar_regra()`:

```python
'seu_criterio': self.sua_funcao_verificacao(publicacao)
```

---

## 📚 Integração Obsidian

1. Salve relatórios em JSON
2. Use o plugin Dataview para visualizar
3. Crie links entre inconformidades e propostas
4. Acompanhe histórico de correções

---

## 🔗 Links Úteis

- [DOEM Prado/BA](https://doem.org.br/ba/prado)
- [Lei de Responsabilidade Fiscal](http://www.planalto.gov.br/ccivil_03/leis/lcp/lcp101.htm)
- [Lei de Nepotismo](http://www.tce.sp.gov.br/institucional/legislacao/decreto-7203-04)

---

**Versão:** 1.0  
**Última atualização:** 2026-06-03  
**Status:** ✅ Funcional e testado
