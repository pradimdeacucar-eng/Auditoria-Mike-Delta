#!/usr/bin/env python3
"""
Gerador de Propostas de Correção - Obsidian Integration
Cria notas automáticas do Obsidian com propostas de ação para cada inconformidade
"""

import json
from datetime import datetime
import os
from pathlib import Path

class GeradorPropostasObsidian:
    def __init__(self):
        self.pasta_propostas = "Propostas_de_Correcao"
        self.criar_pasta_propostas()
    
    def criar_pasta_propostas(self):
        """Cria pasta para propostas se não existir"""
        Path(self.pasta_propostas).mkdir(exist_ok=True)
    
    def gerar_proposta_arquivo(self, audit_file: str):
        """Gera arquivos de propostas a partir de auditoria"""
        try:
            with open(audit_file, 'r', encoding='utf-8') as f:
                dados = json.load(f)
            
            print(f"\n📄 Gerando propostas a partir de: {audit_file}\n")
            
            detalhes = dados.get('detalhes_publicacoes', [])
            
            for pub in detalhes:
                if pub.get('inconformidades'):
                    self._criar_nota_proposta(pub)
            
            # Criar índice geral
            self._criar_indice_propostas(detalhes)
            
            print(f"\n✅ Propostas geradas em: {self.pasta_propostas}/")
        
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {audit_file}")
        except json.JSONDecodeError:
            print(f"❌ Erro ao ler arquivo JSON")
    
    def _criar_nota_proposta(self, publicacao: Dict):
        """Cria nota individual para publicação com inconformidades"""
        pub_id = publicacao.get('id_publicacao', 'DESCONHECIDO')
        titulo = publicacao.get('titulo', 'Sem título')
        tipo = publicacao.get('tipo', 'geral')
        pontuacao = publicacao.get('pontuacao', 0)
        risco = publicacao.get('categoria_risco', 'Desconhecido')
        inconformidades = publicacao.get('inconformidades', [])
        propostas = publicacao.get('propostas', [])
        
        # Montar conteúdo markdown
        conteudo = f"""# 🔧 Proposta de Correção - {pub_id}

**Data:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  
**Publicação Original:** {titulo}  
**Tipo:** {tipo}  
**Conformidade:** {pontuacao:.0f}%  
**Nível de Risco:** {self._emoji_risco(risco)} {risco}

---

## ❌ Problemas Identificados ({len(inconformidades)})

"""
        
        # Agrupar por categoria
        por_categoria = {}
        for inc in inconformidades:
            cat = inc.get('categoria', 'geral')
            if cat not in por_categoria:
                por_categoria[cat] = []
            por_categoria[cat].append(inc)
        
        for categoria, incs in por_categoria.items():
            conteudo += f"\n### 📂 {categoria.upper()}\n\n"
            for inc in incs:
                severidade_icon = self._emoji_severidade(inc.get('severidade'))
                conteudo += f"- {severidade_icon} **{inc.get('nome')}** ({inc.get('id_regra')})\n"
                conteudo += f"  - {inc.get('descricao')}\n"
        
        conteudo += f"""

---

## ✅ Propostas de Ação ({len(set(propostas))})

"""
        
        # Listar propostas únicas
        propostas_unicas = list(set(propostas))
        for idx, prop in enumerate(propostas_unicas, 1):
            conteudo += f"### {idx}. {prop}\n\n"
            conteudo += f"- [ ] Implementar\n"
            conteudo += f"- [ ] Validar\n"
            conteudo += f"- [ ] Documentar\n\n"
        
        conteudo += f"""
---

## 📊 Plano de Ação Detalhado

### Prioridade: {self._calcular_prioridade(pontuacao)}

"""
        
        # Adicionar plano por severidade
        conteudo += self._gerar_plano_acao(inconformidades)
        
        conteudo += f"""

---

## 🔗 Links Relacionados

[[{self._limpar_titulo(titulo)}]]  
[[DOEM_Prado_BA]]  
[[Propostas_de_Correcao/Indice]]

---

**Status:** ⏳ Pendente  
**Data de Criação:** {datetime.now().isoformat()}  
**Próxima Revisão:** {datetime.now().strftime('%Y-%m-%d')} + 7 dias

---

## 📝 Notas

> Adicione observações e progresso aqui
"""
        
        # Salvar arquivo
        safe_titulo = "".join(c for c in titulo if c.isalnum() or c in " -_").rstrip()[:50]
        filename = f"{self.pasta_propostas}/{pub_id}_{safe_titulo}.md"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"  📝 Criado: {filename}")
    
    def _gerar_plano_acao(self, inconformidades: list) -> str:
        """Gera plano de ação por prioridade"""
        criticas = [i for i in inconformidades if i.get('severidade') == 'alta']
        medias = [i for i in inconformidades if i.get('severidade') == 'média']
        baixas = [i for i in inconformidades if i.get('severidade') == 'baixa']
        
        plano = ""
        
        if criticas:
            plano += f"""### 🔴 Ações Imediatas (CRÍTICAS) - {len(criticas)} items

**Prazo:** Até 48 horas

"""
            for inc in criticas:
                plano += f"- [ ] {inc.get('nome')}\n"
            plano += "\n"
        
        if medias:
            plano += f"""### 🟡 Ações Curto Prazo (MÉDIA) - {len(medias)} items

**Prazo:** Até 7 dias

"""
            for inc in medias:
                plano += f"- [ ] {inc.get('nome')}\n"
            plano += "\n"
        
        if baixas:
            plano += f"""### 🟢 Melhorias (BAIXA) - {len(baixas)} items

**Prazo:** Até 30 dias

"""
            for inc in baixas:
                plano += f"- [ ] {inc.get('nome')}\n"
            plano += "\n"
        
        return plano
    
    def _criar_indice_propostas(self, publicacoes: list):
        """Cria arquivo índice de todas as propostas"""
        indice = """# 📑 Índice de Propostas de Correção

**Data de Geração:** {DATA}  
**Total de Propostas:** {TOTAL}

---

## 🚨 Críticas (Prazo 48h)

| ID | Título | Status | Prazo |
|----|--------|--------|-------|
{CRITICAS}

## ⚠️ Moderadas (Prazo 7 dias)

| ID | Título | Status | Prazo |
|----|--------|--------|-------|
{MEDIAS}

## 💡 Sugestões (Prazo 30 dias)

| ID | Título | Status | Prazo |
|----|--------|--------|-------|
{BAIXAS}

---

## 📊 Estatísticas

- **Total de Propostas:** {TOTAL}
- **Críticas:** {N_CRITICAS}
- **Moderadas:** {N_MEDIAS}
- **Sugestões:** {N_BAIXAS}
- **Taxa de Conformidade:** {CONFORMIDADE}%

---

## 🔗 Links Rápidos

[[Propostas_de_Correcao/README]]  
[[AUDITORIA_CONFORMIDADE_GUIA]]  
[[DOEM_Prado_BA]]

"""
        
        # Construir tabelas
        criticas_rows = ""
        medias_rows = ""
        baixas_rows = ""
        
        total_criticas = 0
        total_medias = 0
        total_baixas = 0
        conformidade_media = 0
        
        for pub in publicacoes:
            pub_id = pub.get('id_publicacao', '')
            titulo = pub.get('titulo', '')[:40]
            pontuacao = pub.get('pontuacao', 0)
            conformidade_media += pontuacao
            
            for inc in pub.get('inconformidades', []):
                if inc.get('severidade') == 'alta':
                    criticas_rows += f"| {pub_id} | {titulo} | ⏳ Pendente | 48h |\n"
                    total_criticas += 1
                elif inc.get('severidade') == 'média':
                    medias_rows += f"| {pub_id} | {titulo} | ⏳ Pendente | 7d |\n"
                    total_medias += 1
                else:
                    baixas_rows += f"| {pub_id} | {titulo} | ⏳ Pendente | 30d |\n"
                    total_baixas += 1
        
        conformidade_media = conformidade_media / len(publicacoes) if publicacoes else 0
        
        indice = indice.replace('{DATA}', datetime.now().strftime('%Y-%m-%d'))
        indice = indice.replace('{TOTAL}', str(total_criticas + total_medias + total_baixas))
        indice = indice.replace('{CRITICAS}', criticas_rows or "| - | Nenhuma proposta crítica | - | - |")
        indice = indice.replace('{MEDIAS}', medias_rows or "| - | Nenhuma proposta moderada | - | - |")
        indice = indice.replace('{BAIXAS}', baixas_rows or "| - | Nenhuma sugestão | - | - |")
        indice = indice.replace('{N_CRITICAS}', str(total_criticas))
        indice = indice.replace('{N_MEDIAS}', str(total_medias))
        indice = indice.replace('{N_BAIXAS}', str(total_baixas))
        indice = indice.replace('{CONFORMIDADE}', f"{conformidade_media:.0f}")
        
        with open(f"{self.pasta_propostas}/Indice.md", 'w', encoding='utf-8') as f:
            f.write(indice)
        
        print(f"  📑 Criado: {self.pasta_propostas}/Indice.md")
    
    def _emoji_severidade(self, sev: str) -> str:
        """Retorna emoji baseado em severidade"""
        return {
            'alta': '🔴',
            'média': '🟡',
            'baixa': '🟢'
        }.get(sev, '⚪')
    
    def _emoji_risco(self, risco: str) -> str:
        """Retorna emoji baseado em risco"""
        return {
            'excelente': '🟢',
            'bom': '🟡',
            'regular': '🟠',
            'critico': '🔴'
        }.get(risco.lower(), '⚪')
    
    def _limpar_titulo(self, titulo: str) -> str:
        """Limpa título para usar como link"""
        return "".join(c for c in titulo if c.isalnum() or c in " -_").rstrip()[:50]
    
    def _calcular_prioridade(self, pontuacao: float) -> str:
        """Calcula prioridade baseada em pontuação"""
        if pontuacao >= 80:
            return "🟢 Baixa"
        elif pontuacao >= 50:
            return "🟡 Média"
        else:
            return "🔴 Alta"


def main():
    import sys
    
    gerador = GeradorPropostasObsidian()
    
    # Se arquivo passado como argumento
    if len(sys.argv) > 1:
        gerador.gerar_proposta_arquivo(sys.argv[1])
    else:
        # Procurar arquivo de auditoria mais recente
        arquivos = [f for f in os.listdir('.') if f.startswith('auditoria_conformidade_') and f.endswith('.json')]
        
        if arquivos:
            arquivo_recente = sorted(arquivos)[-1]
            print(f"🔍 Usando arquivo: {arquivo_recente}")
            gerador.gerar_proposta_arquivo(arquivo_recente)
        else:
            print("❌ Nenhum arquivo de auditoria encontrado")
            print("Execute primeiro: python3 auditoria_conformidade.py")


if __name__ == "__main__":
    main()
