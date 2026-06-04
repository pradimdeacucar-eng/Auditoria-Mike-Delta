#!/usr/bin/env python3
"""
Gerador de Propostas de Recuperação - Auditoria Retroativa
Cria notas do Obsidian com planos de recuperação de valores
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

class GeradorPropostasRecuperacao:
    def __init__(self):
        self.pasta_propostas = "Propostas_Recuperacao"
        self.criar_pasta()
    
    def criar_pasta(self):
        """Cria pasta se não existir"""
        Path(self.pasta_propostas).mkdir(exist_ok=True)
    
    def processar_auditoria_retroativa(self, arquivo: str):
        """Processa resultado de auditoria retrospectiva"""
        try:
            with open(arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            print(f"\n📄 Gerando propostas de recuperação...\n")
            
            # Processar perdas financeiras
            for perda in dados.get('perdas_financeiras', []):
                self._criar_proposta_financeira(perda)
            
            # Processar perdas patrimoniais
            for perda in dados.get('perdas_patrimoniais', []):
                self._criar_proposta_patrimonial(perda)
            
            # Criar índice geral
            self._criar_indice_recuperacao(dados)
            
            print(f"\n✅ Propostas geradas em: {self.pasta_propostas}/")
        
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {arquivo}")
        except json.JSONDecodeError:
            print(f"❌ Erro ao ler arquivo JSON")
    
    def _criar_proposta_financeira(self, perda: Dict):
        """Cria proposta para recuperação financeira"""
        perda_id = perda.get('id', 'DESCONHECIDO')
        nome = perda.get('nome', 'Sem título')
        valor_total = perda.get('total_perdas') or perda.get('total_irregular') or perda.get('total_desviado', 0)
        casos = perda.get('casos', [])
        
        conteudo = f"""# 💰 Proposta de Recuperação - {perda_id}

**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Categoria:** Financeira  
**Problema:** {nome}  
**Valor Total Recuperável:** R$ {self._formatar_valor(valor_total)}

---

## ❌ Problema Identificado

{nome}

**Período Afetado:** 2016-2026  
**Casos Documentados:** {len(casos)}

---

## 📋 Detalhamento dos Casos

"""
        
        for idx, caso in enumerate(casos, 1):
            conteudo += f"\n### Caso {idx}: {caso.get('descricao', 'Sem descrição')}\n\n"
            conteudo += f"**Valor:** R$ {self._formatar_valor(caso.get('valor_total', 0))}\n"
            conteudo += f"**Status:** {caso.get('status', 'A verificar')}\n\n"
            
            if 'periodo' in caso:
                conteudo += f"**Período:** {caso.get('periodo')}\n"
            if 'quantidade' in caso:
                conteudo += f"**Quantidade:** {caso.get('quantidade')}\n"
            if 'evidencia' in caso:
                conteudo += f"**Evidência:** {caso.get('evidencia')}\n"
            
            conteudo += "\n"
        
        # Plano de Ação
        conteudo += f"""
---

## ✅ Plano de Ação de Recuperação

### Responsável
- Secretário de Finanças
- Procurador Jurídico (se necessário)

### Fase 1: Confirmação (1-2 semanas)

- [ ] Verificar todos os casos em documentação oficial
- [ ] Validar cálculos e períodos
- [ ] Identificar responsáveis
- [ ] Status do item: ⏳ Planejado

### Fase 2: Cobrança (2-4 semanas)

- [ ] Emitir notificações para devedores
- [ ] Iniciar procedimento administrativo
- [ ] Oferecer parcelamento se aplicável
- [ ] Status do item: ⏳ Em progresso

### Fase 3: Recuperação (1-6 meses)

- [ ] Débitos em folha de pagamento (se aplicável)
- [ ] Ação judicial (se necessário)
- [ ] Compensação de valores
- [ ] Status do item: ⏳ Em progresso

### Fase 4: Validação (Contínuo)

- [ ] Confirmar recebimento de valores
- [ ] Registrar recuperação contábil
- [ ] Documentar aprendizados
- [ ] Status do item: ⏳ Planejado

---

## 📊 Metas

| Item | Meta | Prazo |
|------|------|-------|
| Confirmação | 100% | 14 dias |
| Cobrança iniciada | 100% | 28 dias |
| Recuperação | 80% | 90 dias |
| Validação | 100% | Contínuo |

---

## 💼 Impacto

**Valor a Recuperar:** R$ {self._formatar_valor(valor_total)}

**Impacto Orçamentário:** 
- Aumenta receita do município
- Melhora capacidade de investimento
- Sinaliza rigor fiscal

**Impacto Político:**
- Demonstra compliance
- Recupera confiança
- Melhora ratings de governo

---

## 🔗 Links Relacionados

[[Propostas_Recuperacao/Indice]]  
[[AUDITORIA_RETROATIVA_GUIA]]  
[[DOEM_Prado_BA]]

---

**Status:** ⏳ Pendente  
**Última Atualização:** {datetime.now().isoformat()}  
**Próxima Revisão:** {(datetime.now() + __import__('timedelta', fromlist=['timedelta']).timedelta(days=7)).strftime('%Y-%m-%d')}
"""
        
        # Salvar arquivo
        safe_nome = "".join(c for c in nome if c.isalnum() or c in " -_").rstrip()[:40]
        filename = f"{self.pasta_propostas}/{perda_id}_{safe_nome}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"  💰 Criado: {filename}")
    
    def _criar_proposta_patrimonial(self, perda: Dict):
        """Cria proposta para recuperação patrimonial"""
        perda_id = perda.get('id', 'DESCONHECIDO')
        nome = perda.get('nome', 'Sem título')
        area_total = perda.get('area_ociosa_total') or perda.get('area_desviada') or perda.get('area_doada_irregular') or perda.get('lotes_problematicos', 0)
        valor_total = perda.get('valor_estimado') or perda.get('valor_perdido') or perda.get('valor_prejuizo') or 0
        casos = perda.get('casos', [])
        
        conteudo = f"""# 📍 Proposta de Recuperação Patrimonial - {perda_id}

**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Categoria:** Patrimonial/Imobiliária  
**Problema:** {nome}  
**Área Afetada:** {area_total:,} m²  
**Valor Estimado:** R$ {self._formatar_valor(valor_total)}

---

## ❌ Problema Identificado

{nome}

**Tipo de Perda:**
- Área ociosa (não utilizada)
- Desvio de finalidade
- Doação irregular
- Projeto incompleto
- Loteamento incompleto

**Período:** 2016-2026  
**Casos:** {len(casos)}

---

## 📋 Detalhamento dos Casos

"""
        
        for idx, caso in enumerate(casos, 1):
            conteudo += f"\n### Caso {idx}\n\n"
            
            # Dados comuns
            if 'imovel' in caso:
                conteudo += f"**Imóvel:** {caso['imovel']}\n"
            if 'identificacao' in caso:
                conteudo += f"**ID:** {caso['identificacao']}\n"
            if 'area_m2' in caso:
                conteudo += f"**Área:** {caso['area_m2']:,} m²\n"
            if 'finalidade_original' in caso:
                conteudo += f"**Finalidade Original:** {caso['finalidade_original']}\n"
            if 'uso_atual' in caso or 'situacao_atual' in caso:
                conteudo += f"**Situação Atual:** {caso.get('uso_atual') or caso.get('situacao_atual')}\n"
            
            conteudo += f"**Valor:** R$ {self._formatar_valor(caso.get('valor_total', 0))}\n"
            conteudo += f"**Status:** {caso.get('status', 'A verificar')}\n"
            
            conteudo += "\n"
        
        # Plano de Recuperação
        conteudo += f"""
---

## ✅ Plano de Ação de Recuperação

### Responsável
- Secretário de Planejamento
- Procurador Jurídico
- Controladoria

### Estratégia de Recuperação

#### Opção A: Retomada Administrativa
- [ ] Verificação de documentação de domínio
- [ ] Constatação de desvio/irregularidade
- [ ] Notificação ao ocupante
- [ ] Reintegração de posse
- **Prazo:** 30-60 dias
- **Impacto:** Recuperar uso correto

#### Opção B: Ação Judicial
- [ ] Avaliar vícios legais
- [ ] Preparar ação (anulação, nulidade)
- [ ] Ajuizar processo
- [ ] Acompanhamento em juízo
- **Prazo:** 6-18 meses
- **Impacto:** Garantir recuperação legal

#### Opção C: Regularização
- [ ] Formalizar uso/ocupação
- [ ] Cobrar contrapartida/aluguel
- [ ] Regularizar documentação
- **Prazo:** 30-90 dias
- **Impacto:** Regularizar e arrecadar

### Timeline

```
MÊS 1-2: DIAGNÓSTICO
├─ Confirmar situação
├─ Localizar documentação
└─ Notificar responsáveis

MÊS 2-4: AÇÃO ADMINISTRATIVA
├─ Processos administrativos
├─ Cobranças
└─ Tentativa de acordo

MÊS 4-6: AÇÃO JUDICIAL (se necessário)
├─ Preparação processual
├─ Ajuizamento
└─ Primeiros atos

MÊS 6+: ACOMPANHAMENTO
├─ Execução de sentenças
├─ Recebimento de valores
└─ Retomada de posse
```

---

## 📊 Indicadores

| Métrica | Meta | Prazo |
|---------|------|-------|
| Confirmação | 100% | 14 dias |
| Notificações | 100% | 30 dias |
| Ações iniciadas | 100% | 60 dias |
| Recuperação | 70% | 180 dias |
| Recuperação | 90% | 365 dias |

---

## 💰 Retorno Esperado

**Curto Prazo (6 meses):**
- R$ {self._formatar_valor(valor_total * 0.4)} em cobranças realizadas

**Médio Prazo (12 meses):**
- R$ {self._formatar_valor(valor_total * 0.7)} em recuperações

**Longo Prazo (24 meses):**
- R$ {self._formatar_valor(valor_total)} 100% recuperado
- Geração de renda mensal contínua

---

## 🎯 Benefícios

✅ Recuperação de patrimônio municipal  
✅ Aumento de receita  
✅ Melhor governança  
✅ Maior transparência  
✅ Exemplo para futuras gestões  
✅ Confiança da comunidade

---

## 🔗 Documentação de Apoio

[[Propostas_Recuperacao/Indice]]  
[[AUDITORIA_RETROATIVA_GUIA]]  
[[gabarito_auditoria_retroativa.json]]

---

**Status:** ⏳ Pendente  
**Criada em:** {datetime.now().isoformat()}  
**Próxima Revisão:** {(datetime.now() + __import__('timedelta', fromlist=['timedelta']).timedelta(days=14)).strftime('%Y-%m-%d')}

---

## 📝 Notas e Progresso

> Adicione atualizações de progresso aqui
> 
> Registre documentos encontrados, dificuldades, próximos passos
"""
        
        # Salvar arquivo
        safe_nome = "".join(c for c in nome if c.isalnum() or c in " -_").rstrip()[:40]
        filename = f"{self.pasta_propostas}/{perda_id}_{safe_nome}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"  📍 Criado: {filename}")
    
    def _criar_indice_recuperacao(self, dados: Dict):
        """Cria índice geral de recuperação"""
        total = dados.get('total_geral_recuperavel', 0)
        
        indice = f"""# 📑 Índice de Propostas de Recuperação

**Data de Geração:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Período Analisado:** 2016-2026  
**Total a Recuperar:** R$ {self._formatar_valor(int(total))}

---

## 🎯 Resumo Executivo

### 💰 Financeira
Valores não arrecadados, despesas indevidas, recursos desviados.

### 📍 Patrimonial  
Terras ociosas, desvio de finalidade, doações irregulares, projetos incompletos.

---

## ✅ Propostas de Recuperação

"""
        
        # Listar propostas
        propostas_financeiras = [p for p in dados.get('perdas_financeiras', []) if p.get('casos')]
        propostas_patrimoniais = [p for p in dados.get('perdas_patrimoniais', []) if p.get('casos')]
        
        if propostas_financeiras:
            indice += "### 💰 Propostas Financeiras\n\n"
            for prop in propostas_financeiras:
                valor = prop.get('total_perdas') or prop.get('total_irregular') or prop.get('total_desviado', 0)
                indice += f"- [[{prop['id']}_{prop['nome'].replace(' ', '_')}]] - R$ {self._formatar_valor(valor)}\n"
            indice += "\n"
        
        if propostas_patrimoniais:
            indice += "### 📍 Propostas Patrimoniais\n\n"
            for prop in propostas_patrimoniais:
                area = prop.get('area_ociosa_total') or prop.get('area_desviada', 0)
                valor = prop.get('valor_estimado') or prop.get('valor_perdido', 0)
                indice += f"- [[{prop['id']}_{prop['nome'].replace(' ', '_')}]] - {area:,} m² / R$ {self._formatar_valor(valor)}\n"
            indice += "\n"
        
        indice += f"""
---

## 📊 Estatísticas

| Métrica | Valor |
|---------|-------|
| **Total a Recuperar** | R$ {self._formatar_valor(int(total))} |
| **Propostas Financeiras** | {len(propostas_financeiras)} |
| **Propostas Patrimoniais** | {len(propostas_patrimoniais)} |
| **Casos Totais** | {sum(len(p.get('casos', [])) for p in propostas_financeiras + propostas_patrimoniais)} |

---

## 🚀 Plano de Ação Consolidado

### Fase 1: DIAGNÓSTICO (Semanas 1-2)
- [ ] Confirmar todas as perdas
- [ ] Localizar documentação de apoio
- [ ] Identificar responsáveis
- [ ] **Status:** ⏳ Iniciando

### Fase 2: COBRANÇA (Semanas 3-8)
- [ ] Notificações formais
- [ ] Procedimentos administrativos
- [ ] Oferecimento de acordo
- [ ] **Status:** ⏳ Planejado

### Fase 3: AÇÃO JUDICIAL (Semanas 9+)
- [ ] Ajuizamento de ações
- [ ] Acompanhamento processual
- [ ] Execução de sentenças
- [ ] **Status:** ⏳ Planejado

### Fase 4: VALIDAÇÃO (Contínuo)
- [ ] Recebimento de valores
- [ ] Retomada de bens
- [ ] Documentação final
- [ ] **Status:** ⏳ Planejado

---

## 📅 Cronograma

```
Hoje (Junho 2026)
├─ Semanas 1-2: Diagnóstico
├─ Semanas 3-8: Cobrança Administrativa
├─ Semanas 9-26: Ação Judicial
└─ Semana 27+: Recebimento/Regularização
```

---

## 💡 Recomendações Gerais

1. **Prioridade Máxima**
   - Comunicar Ministério Público (possíveis fraudes)
   - Bloquear novas transações irregulares
   - Reintegração de terras públicas

2. **Designar Força-Tarefa**
   - Procurador Jurídico (coordenador)
   - Secretário de Finanças
   - Controladoria
   - Assistência Técnica

3. **Implementar Controles**
   - Auditoria interna mensal
   - Aprovação dupla para transferências > R$ 50.000
   - Edital obrigatório para doações

4. **Comunicação**
   - Informar Câmara de Vereadores
   - Informar comunidade (transparência)
   - Relatório mensal de progresso

---

## 🔗 Links Úteis

- [[AUDITORIA_RETROATIVA_GUIA]]
- [[gabarito_auditoria_retroativa.json]]
- [[auditoria_retroativa.py]]

---

**Próxima Atualização:** {(datetime.now() + __import__('timedelta', fromlist=['timedelta']).timedelta(days=7)).strftime('%Y-%m-%d')}  
**Status Geral:** ⏳ Em Diagnóstico  
**Responsável:** Procurador Jurídico

---

## 📝 Atualizações de Progresso

> Use esta seção para registrar avanços semanais
"""
        
        with open(f"{self.pasta_propostas}/Indice.md", 'w', encoding='utf-8') as f:
            f.write(indice)
        
        print(f"  📑 Criado: {self.pasta_propostas}/Indice.md")
    
    def _formatar_valor(self, valor: float) -> str:
        """Formata valor em BRL"""
        return f"{valor:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')


def main():
    if len(sys.argv) > 1:
        arquivo = sys.argv[1]
    else:
        # Procurar arquivo mais recente
        import os
        arquivos = [f for f in os.listdir('.') if f.startswith('auditoria_retroativa_') and f.endswith('.json')]
        
        if arquivos:
            arquivo = sorted(arquivos)[-1]
            print(f"🔍 Usando arquivo: {arquivo}")
        else:
            print("❌ Nenhuma auditoria retrospectiva encontrada")
            print("Execute primeiro: python3 auditoria_retroativa.py")
            return
    
    gerador = GeradorPropostasRecuperacao()
    gerador.processar_auditoria_retroativa(arquivo)


if __name__ == "__main__":
    main()
