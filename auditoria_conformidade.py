#!/usr/bin/env python3
"""
Sistema Automático de Auditoria de Conformidade Legal
Analisa publicações do DOEM e identifica inconformidades
Propõe correções em áreas: Administrativa, Jurídica, Legislativa, Financeira, Política, Social
"""

import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
from typing import Dict, List, Tuple

class AuditoriaConformidade:
    def __init__(self):
        self.doem_url = "https://doem.org.br/ba/prado"
        self.gabarito = self.carregar_gabarito()
        self.publicacoes = []
        self.inconformidades = []
        self.relatorio = {}
        
    def carregar_gabarito(self) -> Dict:
        """Carrega gabarito de conformidade"""
        try:
            with open('gabarito_compliance_expandido.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Gabarito não encontrado. Usando padrão básico.")
            return {"conformidade": {}}
    
    def raspar_doem(self) -> List[Dict]:
        """Raspa publicações do DOEM"""
        try:
            print("🔍 Raspando DOEM...")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(self.doem_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            publicacoes = []
            
            # Extrair dados
            items = soup.find_all(['article', 'div'], class_=['item', 'publicacao'])
            
            for idx, item in enumerate(items, 1):
                titulo = item.find(['h2', 'h3', 'a'])
                data = item.find(['span', 'time'])
                texto = item.find(['p', 'div'], class_=['conteudo', 'texto'])
                
                pub = {
                    'id': f"PUB-{idx:05d}",
                    'titulo': titulo.get_text(strip=True) if titulo else "Sem título",
                    'data': data.get_text(strip=True) if data else "Data não encontrada",
                    'texto': texto.get_text(strip=True)[:500] if texto else "",
                    'tipo': self.classificar_tipo(titulo.get_text(strip=True) if titulo else ""),
                    'url': self.doem_url,
                    'data_analise': datetime.now().isoformat()
                }
                publicacoes.append(pub)
            
            print(f"✅ {len(publicacoes)} publicações raspadas")
            return publicacoes
        
        except Exception as e:
            print(f"❌ Erro ao raspar DOEM: {e}")
            return []
    
    def classificar_tipo(self, titulo: str) -> str:
        """Classifica tipo de publicação"""
        titulo_lower = titulo.lower()
        
        if any(x in titulo_lower for x in ['lei', 'decreto', 'portaria']):
            return 'administrativo'
        elif any(x in titulo_lower for x in ['licitação', 'edital', 'contrato']):
            return 'financeiro'
        elif any(x in titulo_lower for x in ['nomeação', 'nomeação', 'exoneração']):
            return 'politico'
        elif any(x in titulo_lower for x in ['auxílio', 'bolsa', 'programa']):
            return 'social'
        else:
            return 'geral'
    
    def analisar_conformidade(self, publicacao: Dict) -> Dict:
        """Analisa conformidade de uma publicação"""
        resultado = {
            'id_publicacao': publicacao['id'],
            'titulo': publicacao['titulo'],
            'tipo': publicacao['tipo'],
            'inconformidades': [],
            'pontuacao': 100,
            'categoria_risco': 'Excelente',
            'propostas': []
        }
        
        # Análise por categoria
        for categoria, dados in self.gabarito.get('conformidade', {}).items():
            score_categoria = self.analisar_categoria(publicacao, categoria, dados)
            
            for regra in dados.get('regras', []):
                conforme = self.verificar_regra(publicacao, regra)
                
                if not conforme:
                    resultado['inconformidades'].append({
                        'id_regra': regra['id'],
                        'categoria': categoria,
                        'nome': regra['nome'],
                        'descricao': regra['descricao'],
                        'severidade': regra['severidade'],
                        'peso': self.gabarito['niveis_severidade'].get(regra['severidade'], 1)
                    })
                    resultado['propostas'].append(dados.get('proposta_correcao', 'Revisar'))
                    resultado['pontuacao'] -= self.gabarito['niveis_severidade'].get(regra['severidade'], 1) * 10
        
        # Calcular categoria de risco
        resultado['pontuacao'] = max(0, resultado['pontuacao'])
        resultado['categoria_risco'] = self.calcular_risco(resultado['pontuacao'])
        
        return resultado
    
    def analisar_categoria(self, pub: Dict, categoria: str, dados: Dict) -> float:
        """Analisa categoria específica"""
        regras_ok = 0
        total_regras = len(dados.get('regras', []))
        
        for regra in dados.get('regras', []):
            if self.verificar_regra(pub, regra):
                regras_ok += 1
        
        return (regras_ok / total_regras * 100) if total_regras > 0 else 0
    
    def verificar_regra(self, publicacao: Dict, regra: Dict) -> bool:
        """Verifica se publicação atende regra"""
        criterio = regra.get('criterio', '').lower()
        texto = (publicacao.get('titulo', '') + ' ' + publicacao.get('texto', '')).lower()
        
        # Verificações específicas
        verificacoes = {
            'atos_publicados > 0': len(publicacao.get('titulo', '')) > 5,
            'nomenclatura_padrao': self.verificar_nomenclatura(publicacao),
            'assinatura_digital_valida': 'assinado' in texto or 'digital' in texto,
            'conforme_lei_federal': 'federal' in texto or 'lei federal' in texto,
            'conforme_lei_estadual': 'estadual' in texto or 'lei estadual' in texto,
            'fundamentacao_legal_presente': 'artigo' in texto or 'lei' in texto,
            'processo_legislativo_correto': 'câmara' in texto or 'legislativo' in texto,
            'consulta_publica_realizada': 'consulta' in texto or 'público' in texto,
            'sancionada_prefeito': 'prefeito' in texto or 'sanciona' in texto,
            'conforme_lrf': 'lrf' in texto or 'responsabilidade fiscal' in texto,
            'cobertura_orcamentaria': 'orçamento' in texto or 'dotação' in texto,
            'dentro_limite_despesa': not self.detectar_excesso_despesa(publicacao),
            'despesas_publicadas': 'despesa' in texto or 'gasto' in texto,
            'transparencia_fiscal': 'transparência' in texto or 'público' in texto,
            'sem_nepotismo': not self.detectar_nepotismo(publicacao),
            'sem_conflito_interesse': 'conflito' not in texto,
            'equilibrio_politico': True,
            'politicas_sociais_planejadas': 'social' in texto or 'programa' in texto,
            'acesso_informacao': 'público' in texto or 'informação' in texto,
            'participacao_cidada': 'participação' in texto or 'cidadão' in texto,
            'politicas_inclusao': 'inclusão' in texto or 'acessibilidade' in texto
        }
        
        return verificacoes.get(criterio, True)
    
    def verificar_nomenclatura(self, pub: Dict) -> bool:
        """Verifica se nomenclatura segue padrão"""
        titulo = pub.get('titulo', '').upper()
        palavras_esperadas = ['LEI', 'DECRETO', 'PORTARIA', 'RESOLUÇÃO', 'EDITAL', 'ATO']
        return any(palavra in titulo for palavra in palavras_esperadas)
    
    def detectar_nepotismo(self, pub: Dict) -> bool:
        """Detecta possível nepotismo"""
        texto = (pub.get('titulo', '') + ' ' + pub.get('texto', '')).lower()
        parentescos = ['filho', 'filha', 'irmão', 'irmã', 'pai', 'mãe', 'esposo', 'esposa', 'sobrinho']
        nomeacoes = ['nomeação', 'contratação', 'indicação']
        
        tem_nomeacao = any(nome in texto for nome in nomeacoes)
        tem_parentesco = any(par in texto for par in parentescos)
        
        return tem_nomeacao and tem_parentesco
    
    def detectar_excesso_despesa(self, pub: Dict) -> bool:
        """Detecta possível excesso de despesa"""
        texto = (pub.get('titulo', '') + ' ' + pub.get('texto', '')).lower()
        
        # Procurar por valores grandes
        valores = re.findall(r'r\$?\s*[\d.,]+', texto)
        
        for valor in valores:
            try:
                # Converter para número
                num = float(valor.replace('r$', '').replace('.', '').replace(',', '.'))
                if num > 1000000:  # Acima de 1 milhão
                    return True
            except:
                pass
        
        return False
    
    def calcular_risco(self, pontuacao: float) -> str:
        """Calcula categoria de risco"""
        for categoria, dados in self.gabarito.get('pontuacao', {}).items():
            if pontuacao >= dados['minimo']:
                return categoria
        return 'critico'
    
    def gerar_relatorio(self) -> Dict:
        """Gera relatório consolidado"""
        return {
            'data_analise': datetime.now().isoformat(),
            'total_publicacoes': len(self.publicacoes),
            'total_inconformidades': len(self.inconformidades),
            'categorias': self._agrupar_por_categoria(),
            'severidades': self._contar_severidades(),
            'pontuacao_media': self._calcular_pontuacao_media(),
            'recomendacoes': self._gerar_recomendacoes()
        }
    
    def _agrupar_por_categoria(self) -> Dict:
        """Agrupa inconformidades por categoria"""
        grupos = {}
        for inc in self.inconformidades:
            cat = inc.get('categoria', 'geral')
            if cat not in grupos:
                grupos[cat] = []
            grupos[cat].append(inc)
        return grupos
    
    def _contar_severidades(self) -> Dict:
        """Conta inconformidades por severidade"""
        return {
            'alta': len([i for i in self.inconformidades if i.get('severidade') == 'alta']),
            'média': len([i for i in self.inconformidades if i.get('severidade') == 'média']),
            'baixa': len([i for i in self.inconformidades if i.get('severidade') == 'baixa'])
        }
    
    def _calcular_pontuacao_media(self) -> float:
        """Calcula pontuação média de conformidade"""
        if not self.relatorio:
            return 0
        pontuacoes = [r.get('pontuacao', 0) for r in self.relatorio.values()]
        return sum(pontuacoes) / len(pontuacoes) if pontuacoes else 0
    
    def _gerar_recomendacoes(self) -> List[str]:
        """Gera recomendações gerais"""
        recomendacoes = []
        severidades = self._contar_severidades()
        
        if severidades['alta'] > 0:
            recomendacoes.append(f"🔴 CRÍTICO: {severidades['alta']} inconformidades graves detectadas. Ação imediata necessária.")
        
        if severidades['média'] > 3:
            recomendacoes.append(f"🟡 ATENÇÃO: {severidades['média']} problemas moderados. Revisar em curto prazo.")
        
        if self._calcular_pontuacao_media() < 50:
            recomendacoes.append("📋 Realizar auditoria completa da Prefeitura")
            recomendacoes.append("👨‍⚖️ Consultar Procuradoria Jurídica")
            recomendacoes.append("📊 Revisar processos administrativos e financeiros")
        
        return recomendacoes
    
    def executar_auditoria_completa(self):
        """Executa auditoria completa"""
        print("\n" + "="*60)
        print("🔍 AUDITORIA AUTOMÁTICA DE CONFORMIDADE LEGAL")
        print("="*60 + "\n")
        
        # 1. Raspar dados
        self.publicacoes = self.raspar_doem()
        
        if not self.publicacoes:
            print("⚠️  Nenhuma publicação para analisar")
            return
        
        # 2. Analisar cada publicação
        print("\n📋 Analisando conformidade...\n")
        for pub in self.publicacoes:
            resultado = self.analisar_conformidade(pub)
            self.relatorio[pub['id']] = resultado
            self.inconformidades.extend(resultado['inconformidades'])
            
            # Mostrar status
            icon = "✅" if resultado['pontuacao'] >= 80 else "⚠️ " if resultado['pontuacao'] >= 50 else "❌"
            print(f"{icon} {pub['id']}: {resultado['categoria_risco']} ({resultado['pontuacao']:.0f}%)")
        
        # 3. Gerar relatório final
        self.relatorio_final = self.gerar_relatorio()
        self._exibir_relatorio()
        self._salvar_relatorio()
    
    def _exibir_relatorio(self):
        """Exibe relatório na tela"""
        rel = self.relatorio_final
        
        print("\n" + "="*60)
        print("📊 RELATÓRIO CONSOLIDADO")
        print("="*60)
        print(f"\n📈 Estatísticas:")
        print(f"  • Total de publicações analisadas: {rel['total_publicacoes']}")
        print(f"  • Inconformidades encontradas: {rel['total_inconformidades']}")
        print(f"  • Pontuação média: {rel['pontuacao_media']:.1f}%")
        
        print(f"\n🚨 Distribuição por Severidade:")
        for sev, count in rel['severidades'].items():
            print(f"  • {sev.upper()}: {count}")
        
        print(f"\n📂 Inconformidades por Categoria:")
        for cat, incs in rel['categorias'].items():
            print(f"  • {cat.upper()}: {len(incs)} problemas")
        
        print(f"\n💡 Recomendações:")
        for rec in rel['recomendacoes']:
            print(f"  {rec}")
        
        print("\n" + "="*60 + "\n")
    
    def _salvar_relatorio(self):
        """Salva relatório em JSON"""
        filename = f"auditoria_conformidade_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        dados_salvar = {
            'relatorio_consolidado': self.relatorio_final,
            'detalhes_publicacoes': list(self.relatorio.values()),
            'timestamp': datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(dados_salvar, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Relatório salvo em: {filename}")


def main():
    auditoria = AuditoriaConformidade()
    auditoria.executar_auditoria_completa()


if __name__ == "__main__":
    main()
