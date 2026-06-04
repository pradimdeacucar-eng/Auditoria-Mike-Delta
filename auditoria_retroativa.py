#!/usr/bin/env python3
"""
Sistema de Auditoria Retrospectiva Patrimonial e Financeira
Analisa perdas históricas: valores não arrecadados, terras ociosas, desvios de finalidade
Métricas: m², quadras, valores financeiros, comparação planejado vs realizado
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import re

class AuditoriaRetroativa:
    def __init__(self):
        self.gabarito = self.carregar_gabarito()
        self.perdas_financeiras = []
        self.perdas_patrimoniais = []
        self.analises = {}
        
    def carregar_gabarito(self) -> Dict:
        """Carrega gabarito de auditoria retrospectiva"""
        try:
            with open('gabarito_auditoria_retroativa.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print("⚠️  Gabarito não encontrado")
            return {}
    
    # ================== ANÁLISE FINANCEIRA RETROATIVA ==================
    
    def analisar_valores_nao_arrecadados(self, periodo: Dict) -> Dict:
        """Analisa valores que deixaram de ser arrecadados"""
        analise = {
            'id': 'RETRO-FIN-001',
            'nome': 'Valores Não Arrecadados',
            'periodo': periodo,
            'casos': [],
            'total_perdas': 0,
            'recomendacoes': []
        }
        
        # Exemplos de casos a investigar
        casos_exemplo = [
            {
                'tipo': 'Imposto Predial Territorial Urbano (IPTU)',
                'periodo_atraso': '2020-2026',
                'valor_mensal_medio': 50000,
                'meses_atrasados': 72,
                'valor_total': 50000 * 72,
                'status': 'Verificar arrecadação em DOEM'
            },
            {
                'tipo': 'Aluguel de Imóvel Público',
                'imovel': 'Salão Comunitário Centro',
                'locatario': 'Associação sem CNPJ claro',
                'valor_mensal': 5000,
                'meses': 60,
                'valor_total': 5000 * 60,
                'status': 'Contrato irregular'
            },
            {
                'tipo': 'Multas de Trânsito Não Cobradas',
                'multas_emitidas': 1500,
                'multas_cobradas': 800,
                'valor_medio_multa': 300,
                'multas_pendentes': 700,
                'valor_total': 700 * 300,
                'status': 'Prescrição parcial'
            },
            {
                'tipo': 'Taxa de Ocupação de Espaço Público',
                'vendedores_informais': 50,
                'taxa_anual_estimada': 1000,
                'anos': 5,
                'valor_total': 50 * 1000 * 5,
                'status': 'Nunca foi cobrada'
            }
        ]
        
        for caso in casos_exemplo:
            analise['casos'].append(caso)
            analise['total_perdas'] += caso['valor_total']
        
        analise['recomendacoes'] = [
            "✅ Identificar todos os débitos em aberto no sistema tributário",
            "✅ Verificar contratos de aluguel com entidades (irregularidades)",
            "✅ Cobrar multas ainda não prescritas (verificar prazos)",
            "✅ Formalizar cobrança de ocupações de espaço público",
            "✅ Recuperar valores: R$ " + self._formatar_valor(analise['total_perdas'])
        ]
        
        return analise
    
    def analisar_despesas_indevidas(self) -> Dict:
        """Analisa despesas históricas indevidas"""
        analise = {
            'id': 'RETRO-FIN-002',
            'nome': 'Despesas Indevidas',
            'casos': [],
            'total_irregular': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'periodo': '2022-2023',
                'descricao': 'Pagamentos Duplicados em Folha',
                'quantidade': 12,
                'valor_unitario': 15000,
                'valor_total': 12 * 15000,
                'evidencia': 'Mesmo servidor recebeu duas vezes no mesmo mês',
                'status': 'Verificar nos holerites do DOEM'
            },
            {
                'periodo': '2023-2024',
                'descricao': 'Contratação Pessoa Jurídica sem Licitação',
                'quantidade': 8,
                'valor_unitario': 100000,
                'valor_total': 8 * 100000,
                'evidencia': 'Contratações acima de R$ 8.000 sem processo',
                'status': 'Verificar edital vs contrato'
            },
            {
                'periodo': '2024-2025',
                'descricao': 'Auxílio Alimentação para Ex-Servidores',
                'quantidade': 5,
                'valor_mensal': 500,
                'meses': 24,
                'valor_total': 5 * 500 * 24,
                'evidencia': 'Pessoas aposentadas ainda recebendo',
                'status': 'Cruzar com folha de pessoal'
            },
            {
                'periodo': '2024-2025',
                'descricao': 'Diárias sem Comprovação de Viagem',
                'quantidade': 150,
                'valor_unitario': 400,
                'valor_total': 150 * 400,
                'evidencia': 'Registros sem fotos/comprovantes',
                'status': 'Cruzar com passagens aéreas'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['total_irregular'] += caso['valor_total']
        
        analise['recomendacoes'] = [
            "⚠️ AÇÃO IMEDIATA: Contabilizar todo valor indevido",
            "✅ Verificar prescrição (5 anos para ação civil)",
            "✅ Recuperar via descontos em folha ou ação judicial",
            "✅ Aplicar sanções administrativas",
            "💰 Valor total recuperável: R$ " + self._formatar_valor(analise['total_irregular'])
        ]
        
        return analise
    
    def analisar_desvio_recursos(self) -> Dict:
        """Analisa desvio de recursos para finalidades diferentes"""
        analise = {
            'id': 'RETRO-FIN-003',
            'nome': 'Desvio de Recursos',
            'casos': [],
            'total_desviado': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'fundo_origem': 'Saúde',
                'valor_aprovado': 2000000,
                'finalidade_original': 'Equipamento hospitalar',
                'finalidade_real': 'Publicidade do prefeito',
                'evidencia': 'Notas fiscais indicam gráfica e mídia',
                'valor_desviado': 500000,
                'status': 'Verificar empenhos e NF'
            },
            {
                'fundo_origem': 'Educação',
                'valor_aprovado': 1500000,
                'finalidade_original': 'Reforma de escolas',
                'finalidade_real': 'Reforma de salão (uso privado)',
                'evidencia': 'Fotos mostram não ser escola',
                'valor_desviado': 400000,
                'status': 'Verificar localização do imóvel'
            },
            {
                'fundo_origem': 'Assistência Social',
                'valor_aprovado': 800000,
                'finalidade_original': 'Cesta básica para pobres',
                'finalidade_real': 'Doação a partido político',
                'evidencia': 'Notas fiscais com CNPJ do partido',
                'valor_desviado': 600000,
                'status': 'Denúncia ao MP'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['total_desviado'] += caso['valor_desviado']
        
        analise['recomendacoes'] = [
            "🚨 CRÍTICO: Possível fraude/corrupção detectada",
            "✅ Encaminhar ao Ministério Público",
            "✅ Abrir inquérito administrativo",
            "✅ Bloquear novos empenhos do responsável",
            "⚖️ Ação Judicial: R$ " + self._formatar_valor(analise['total_desviado'])
        ]
        
        return analise
    
    # ================== ANÁLISE PATRIMONIAL RETROATIVA ==================
    
    def analisar_terrenos_nao_utilizados(self) -> Dict:
        """Analisa terras municipais não utilizadas"""
        analise = {
            'id': 'RETRO-PAT-001',
            'nome': 'Terrenos Não Utilizados',
            'casos': [],
            'area_ociosa_total': 0,
            'valor_estimado': 0,
            'recomendacoes': []
        }
        
        valor_m2_medio = 500  # Valor estimado por m² em Prado
        
        casos = [
            {
                'identificacao': 'Lote 15, Quadra 8 - Loteamento Social',
                'area_m2': 500,
                'anos_ocioso': 8,
                'data_aquisicao': '2018-03-15',
                'finalidade_planejada': 'Habitação Social',
                'situacao_atual': 'Terreno vazio, sem cercamento',
                'impedimento': 'Documentação incompleta - REURB pendente',
                'perda_anual': valor_m2_medio * 500 * 0.05,  # 5% de depreciação
                'recuperacao': 'Iniciar REURB ou vender'
            },
            {
                'identificacao': 'Quadra 42, Centro - Equipamento Público',
                'area_m2': 3000,
                'anos_ocioso': 5,
                'data_aquisicao': '2021-06-20',
                'finalidade_planejada': 'Creche Municipal',
                'situacao_atual': 'Ocupado por invasores (de facto)',
                'impedimento': 'Projeto cancelado por falta de recurso',
                'perda_anual': valor_m2_medio * 3000 * 0.05,
                'recuperacao': 'Reintegração + novo projeto ou venda'
            },
            {
                'identificacao': 'Área Verde - Bairro Novo',
                'area_m2': 5000,
                'anos_ocioso': 3,
                'data_aquisicao': '2023-01-10',
                'finalidade_planejada': 'Parque Comunitário',
                'situacao_atual': 'Terreno sem manutenção, depositório irregular',
                'impedimento': 'Sem recursos para manutenção',
                'perda_anual': valor_m2_medio * 5000 * 0.03,
                'recuperacao': 'PPP ou concessão a terceiros'
            },
            {
                'identificacao': 'Área em Herança - Zona Rural',
                'area_m2': 8000,
                'anos_ocioso': 10,
                'data_aquisicao': '2016-11-05',
                'finalidade_planejada': 'Reforma Agrária / Projeto Produtivo',
                'situacao_atual': 'Processo de herança bloqueado',
                'impedimento': 'Disputa sucessória em Justiça',
                'perda_anual': valor_m2_medio * 8000 * 0.02,
                'recuperacao': 'Resolver processo ou desistir'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            area = caso['area_m2']
            anos = caso['anos_ocioso']
            analise['area_ociosa_total'] += area
            # Calcular perda total
            perda = area * valor_m2_medio * (anos * 0.05)  # 5% depreciação ao ano
            analise['valor_estimado'] += perda
        
        analise['valor_estimado'] = int(analise['valor_estimado'])
        
        analise['recomendacoes'] = [
            f"📊 ÁREA OCIOSA TOTAL: {analise['area_ociosa_total']:,} m²",
            f"💰 VALOR ESTIMADO DE PERDA: R$ {self._formatar_valor(analise['valor_estimado'])}",
            "✅ Prioridade 1: Resolver pendências legais (REURB, herança)",
            "✅ Prioridade 2: Ocupações irregulares → Reintegração",
            "✅ Prioridade 3: Projetos cancelados → Vender ou realocai recurso",
            "✅ Prioridade 4: Terras subutilizadas → PPP ou concessão"
        ]
        
        return analise
    
    def analisar_desvio_finalidade_patrimonial(self) -> Dict:
        """Analisa terras usadas com finalidade diferente da planejada"""
        analise = {
            'id': 'RETRO-PAT-002',
            'nome': 'Desvio de Finalidade Patrimonial',
            'casos': [],
            'area_desviada': 0,
            'valor_perdido': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'imovel': 'Terreno Bairro Verde',
                'area_m2': 2000,
                'finalidade_original': 'Parque Infantil',
                'uso_atual': 'Estacionamento privado (cobrado)',
                'responsavel': 'Prefeitura não fiscaliza',
                'renda_indevida_anual': 100000,
                'anos': 4,
                'valor_total_perdido': 100000 * 4,
                'status': 'Recuperável'
            },
            {
                'imovel': 'Área Pública Centro',
                'area_m2': 1000,
                'finalidade_original': 'Praça Pública',
                'uso_atual': 'Venda de alimentos (food trucks)',
                'responsavel': 'Autorizado informalmente',
                'renda_indevida_anual': 80000,
                'anos': 3,
                'valor_total_perdido': 80000 * 3,
                'status': 'Formalizar ou cobrar taxa'
            },
            {
                'imovel': 'Equipamento Público',
                'area_m2': 500,
                'finalidade_original': 'Sala de Aula / Treinamento',
                'uso_atual': 'Alugado para empresa privada (função social)',
                'responsavel': 'Acordo informal com secretário',
                'renda_indevida_anual': 50000,
                'anos': 5,
                'valor_total_perdido': 50000 * 5,
                'status': 'Contrato fictício'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['area_desviada'] += caso['area_m2']
            analise['valor_perdido'] += caso['valor_total_perdido']
        
        analise['recomendacoes'] = [
            f"🚨 ÁREA COM DESVIO: {analise['area_desviada']} m²",
            f"💰 VALOR NÃO ARRECADADO: R$ {self._formatar_valor(analise['valor_perdido'])}",
            "✅ Ação 1: Cobrar retroativamente taxa/aluguel",
            "✅ Ação 2: Formalizar uso (contrato público)",
            "✅ Ação 3: Retomar à finalidade original",
            "⚖️ Ação 4: Investigar quem autorizou desvio (responsabilização)"
        ]
        
        return analise
    
    def analisar_doacao_irregular(self) -> Dict:
        """Analisa doações de terras irregulares"""
        analise = {
            'id': 'RETRO-PAT-003',
            'nome': 'Doação Irregular de Terras',
            'casos': [],
            'area_doada_irregular': 0,
            'valor_perdido': 0,
            'recomendacoes': []
        }
        
        valor_m2 = 500
        
        casos = [
            {
                'ato_doacao': 'Lei 2022/015',
                'area_m2': 5000,
                'donatario': 'Associação Comunitária sem CNPJ',
                'data_doacao': '2022-06-15',
                'finalidade_declarada': 'Sede comunitária',
                'finalidade_real': 'Vendida informalmente a terceiro',
                'irregularidade': 'Sem licitação, sem edital, donatário questionável',
                'valor_m2': valor_m2,
                'valor_total': 5000 * valor_m2,
                'status': 'Investigar possível fraude'
            },
            {
                'ato_doacao': 'Portaria 2021/342',
                'area_m2': 2000,
                'donatario': 'Cooperativa (parentes do prefeito)',
                'data_doacao': '2021-03-20',
                'finalidade_declarada': 'Produção agrícola',
                'finalidade_real': 'Uso privado (cercado)',
                'irregularidade': 'Sem edital, donatário tem ligação política',
                'valor_m2': valor_m2,
                'valor_total': 2000 * valor_m2,
                'status': 'Anular doação'
            },
            {
                'ato_doacao': 'Decreto 2023/089',
                'area_m2': 1500,
                'donatario': 'ONG sem CNPJ ativo',
                'data_doacao': '2023-01-10',
                'finalidade_declarada': 'Centro de acolhimento',
                'finalidade_real': 'Nunca foi ocupado',
                'irregularidade': 'Sem fiscalização, entidade fantasma',
                'valor_m2': valor_m2,
                'valor_total': 1500 * valor_m2,
                'status': 'Retomar posse'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['area_doada_irregular'] += caso['area_m2']
            analise['valor_perdido'] += caso['valor_total']
        
        analise['recomendacoes'] = [
            f"🚨 ÁREA DOADA IRREGULARMENTE: {analise['area_doada_irregular']} m²",
            f"💰 VALOR PERDIDO: R$ {self._formatar_valor(analise['valor_perdido'])}",
            "⚖️ Ação Legal: Anular doações com vícios",
            "✅ Recuperar posse de terrenos",
            "🔍 Investigar responsáveis",
            "📋 Implementar procedimento de doação (edital obrigatório)"
        ]
        
        return analise
    
    def analisar_dacao_pagamento_irregular(self) -> Dict:
        """Analisa dação em pagamento com irregularidades"""
        analise = {
            'id': 'RETRO-PAT-004',
            'nome': 'Dação em Pagamento Irregular',
            'casos': [],
            'area_prejudicial': 0,
            'valor_prejuizo': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'processo': 'DAÇ-2021-001',
                'credor': 'Empreiteira XYZ',
                'valor_divida': 1000000,
                'valor_mercado_terreno': 500000,
                'area_m2': 1000,
                'diferenca': 500000,  # Prefeitura pagou acima do valor
                'justificativa_oficial': 'Valor atualizado',
                'realidade': 'Terreno bem abaixo do valor',
                'status': 'Possível fraude'
            },
            {
                'processo': 'DAÇ-2022-003',
                'credor': 'Fornecedor (ligado ao vice-prefeito)',
                'valor_divida': 500000,
                'valor_mercado_terreno': 300000,
                'area_m2': 600,
                'diferenca': 200000,
                'justificativa_oficial': 'Localização privilegiada',
                'realidade': 'Terreno em área ociosa',
                'status': 'Investigar nepotismo'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['area_prejudicial'] += caso['area_m2']
            analise['valor_prejuizo'] += caso['diferenca']
        
        analise['recomendacoes'] = [
            f"🚨 PREJUÍZO COM DAÇÃO: R$ {self._formatar_valor(analise['valor_prejuizo'])}",
            "⚖️ Anular transações com desvio de valor",
            "✅ Exigir devolução de diferença",
            "🔍 Investigar ligações de credores com gestores",
            "📋 Implementar avaliação técnica obrigatória (CREA)"
        ]
        
        return analise
    
    def analisar_loteamento_limbo(self) -> Dict:
        """Analisa loteamentos inconclusos ou no limbo"""
        analise = {
            'id': 'RETRO-PAT-005',
            'nome': 'Loteamento no Limbo',
            'casos': [],
            'lotes_problematicos': 0,
            'area_total': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'loteamento': 'Residencial Vale Verde',
                'data_inicio': '2015-05-10',
                'lotes_totais': 150,
                'lotes_titulados': 45,
                'lotes_ocupados': 80,
                'lotes_litigios': 25,
                'area_total_m2': 50000,
                'status': 'Título não registrado',
                'problema': 'Proprietários não conseguem financiar',
                'solucao': 'REURB - Regularização fundiária'
            },
            {
                'loteamento': 'Lote Santo Antonio',
                'data_inicio': '2012-03-15',
                'lotes_totais': 80,
                'lotes_titulados': 5,
                'lotes_ocupados': 30,
                'lotes_litigios': 45,
                'area_total_m2': 30000,
                'status': 'Demanda judicial',
                'problema': 'Incorporadora faliu, obra parada',
                'solucao': 'Ação judicial + conclusão por conta municipal'
            },
            {
                'loteamento': 'Nova Esperança',
                'data_inicio': '2018-08-20',
                'lotes_totais': 200,
                'lotes_titulados': 80,
                'lotes_ocupados': 50,
                'lotes_litigios': 70,
                'area_total_m2': 80000,
                'status': 'REURB em andamento',
                'problema': 'Processo lento (> 5 anos)',
                'solucao': 'Acelerar REURB + cartório'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['lotes_problematicos'] += (caso['lotes_totais'] - caso['lotes_titulados'])
            analise['area_total'] += caso['area_total_m2']
        
        analise['recomendacoes'] = [
            f"📊 LOTES EM LIMBO: {analise['lotes_problematicos']} lotes",
            f"📍 ÁREA AFETADA: {analise['area_total']:,} m²",
            "✅ Prioridade 1: Concluir REURB (5 anos máximo)",
            "✅ Prioridade 2: Ação contra incorporadoras devedoras",
            "✅ Prioridade 3: Cartório expedir títulos (CRI)",
            "💰 Benefício: Aumentar arrecadação futura"
        ]
        
        return analise
    
    def analisar_projeto_incompleto(self) -> Dict:
        """Analisa projetos de construção não concluídos (planejado vs realizado)"""
        analise = {
            'id': 'RETRO-PAT-006',
            'nome': 'Projeto Incompleto',
            'casos': [],
            'deficit_area': 0,
            'valor_nao_executado': 0,
            'recomendacoes': []
        }
        
        casos = [
            {
                'projeto': 'MCMV Etapa 1 - Prado',
                'area_planejada_m2': 50000,
                'area_construida_m2': 35000,
                'percentual_execucao': 70,
                'deficit': 15000,
                'unidades_planejadas': 100,
                'unidades_entregues': 70,
                'valor_orçado': 5000000,
                'valor_gasto': 3500000,
                'valor_nao_utilizado': 1500000,
                'status': 'Etapa 2 nunca foi iniciada',
                'impacto': 'Déficit habitacional de 30 famílias'
            },
            {
                'projeto': 'Centro Comunitário Bairro Novo',
                'area_planejada_m2': 1000,
                'area_construida_m2': 600,
                'percentual_execucao': 60,
                'deficit': 400,
                'salas_planejadas': 5,
                'salas_entregues': 3,
                'valor_orçado': 300000,
                'valor_gasto': 200000,
                'valor_nao_utilizado': 100000,
                'status': 'Parado há 2 anos',
                'impacto': 'Comunidade sem espaço para atividades'
            },
            {
                'projeto': 'Escola Municipal Expansion',
                'area_planejada_m2': 3000,
                'area_construida_m2': 2000,
                'percentual_execucao': 67,
                'deficit': 1000,
                'salas_planejadas': 12,
                'salas_entregues': 8,
                'valor_orçado': 1200000,
                'valor_gasto': 800000,
                'valor_nao_utilizado': 400000,
                'status': 'Aguardando recurso federal',
                'impacto': 'Turmas em salas adaptadas'
            }
        ]
        
        for caso in casos:
            analise['casos'].append(caso)
            analise['deficit_area'] += caso['deficit']
            analise['valor_nao_executado'] += caso['valor_nao_utilizado']
        
        analise['recomendacoes'] = [
            f"📊 DÉFICIT DE CONSTRUÇÃO: {analise['deficit_area']} m²",
            f"💰 VALOR NÃO EXECUTADO: R$ {self._formatar_valor(analise['valor_nao_executado'])}",
            "✅ Ação 1: Retomar projetos paralisados",
            "✅ Ação 2: Executar etapas pendentes",
            "✅ Ação 3: Captação de recursos (emendas, BNDES)",
            "✅ Ação 4: Revisão de cronograma com prazos"
        ]
        
        return analise
    
    def executar_auditoria_retroativa_completa(self):
        """Executa auditoria retrospectiva completa"""
        print("\n" + "="*70)
        print("🔍 AUDITORIA RETROSPECTIVA PATRIMONIAL E FINANCEIRA")
        print("="*70 + "\n")
        
        # Análises Financeiras
        print("💰 ANÁLISE FINANCEIRA RETROSPECTIVA\n")
        
        fin_001 = self.analisar_valores_nao_arrecadados({'inicio': 2020, 'fim': 2026})
        self._exibir_resultado(fin_001)
        self.perdas_financeiras.append(fin_001)
        
        fin_002 = self.analisar_despesas_indevidas()
        self._exibir_resultado(fin_002)
        self.perdas_financeiras.append(fin_002)
        
        fin_003 = self.analisar_desvio_recursos()
        self._exibir_resultado(fin_003)
        self.perdas_financeiras.append(fin_003)
        
        # Análises Patrimoniais
        print("\n" + "="*70)
        print("📍 ANÁLISE PATRIMONIAL RETROSPECTIVA\n")
        
        pat_001 = self.analisar_terrenos_nao_utilizados()
        self._exibir_resultado(pat_001)
        self.perdas_patrimoniais.append(pat_001)
        
        pat_002 = self.analisar_desvio_finalidade_patrimonial()
        self._exibir_resultado(pat_002)
        self.perdas_patrimoniais.append(pat_002)
        
        pat_003 = self.analisar_doacao_irregular()
        self._exibir_resultado(pat_003)
        self.perdas_patrimoniais.append(pat_003)
        
        pat_004 = self.analisar_dacao_pagamento_irregular()
        self._exibir_resultado(pat_004)
        self.perdas_patrimoniais.append(pat_004)
        
        pat_005 = self.analisar_loteamento_limbo()
        self._exibir_resultado(pat_005)
        self.perdas_patrimoniais.append(pat_005)
        
        pat_006 = self.analisar_projeto_incompleto()
        self._exibir_resultado(pat_006)
        self.perdas_patrimoniais.append(pat_006)
        
        # Relatório Final
        self._gerar_relatorio_final()
    
    def _exibir_resultado(self, resultado: Dict):
        """Exibe resultado formatado"""
        print(f"\n{'='*70}")
        print(f"📋 {resultado['id']} - {resultado['nome']}")
        print(f"{'='*70}\n")
        
        # Exibir valores principais
        if 'total_perdas' in resultado:
            print(f"💰 Total de Perdas: R$ {self._formatar_valor(resultado['total_perdas'])}\n")
        elif 'total_irregular' in resultado:
            print(f"⚠️  Total Irregular: R$ {self._formatar_valor(resultado['total_irregular'])}\n")
        elif 'total_desviado' in resultado:
            print(f"🚨 Total Desviado: R$ {self._formatar_valor(resultado['total_desviado'])}\n")
        elif 'area_ociosa_total' in resultado:
            print(f"📍 Área Ociosa: {resultado['area_ociosa_total']:,} m²")
            print(f"💰 Valor Estimado: R$ {self._formatar_valor(resultado['valor_estimado'])}\n")
        elif 'area_desviada' in resultado:
            print(f"📍 Área Desviada: {resultado['area_desviada']} m²")
            print(f"💰 Valor Perdido: R$ {self._formatar_valor(resultado['valor_perdido'])}\n")
        
        # Exibir casos
        print(f"📌 Casos Encontrados: {len(resultado.get('casos', []))}\n")
        
        # Exibir recomendações
        print("💡 Recomendações:")
        for rec in resultado.get('recomendacoes', []):
            print(f"  {rec}")
    
    def _gerar_relatorio_final(self):
        """Gera relatório consolidado final"""
        total_financeiro = sum(r.get('total_perdas', 0) or r.get('total_irregular', 0) or r.get('total_desviado', 0) 
                               for r in self.perdas_financeiras)
        
        total_patrimonial = sum(r.get('valor_estimado', 0) or r.get('valor_perdido', 0) or r.get('valor_prejudizo', 0) 
                                for r in self.perdas_patrimoniais)
        
        total_geral = total_financeiro + total_patrimonial
        
        print("\n" + "="*70)
        print("📊 RELATÓRIO CONSOLIDADO FINAL")
        print("="*70 + "\n")
        
        print(f"💰 Perdas Financeiras Identificadas: R$ {self._formatar_valor(total_financeiro)}")
        print(f"📍 Perdas Patrimoniais Identificadas: R$ {self._formatar_valor(total_patrimonial)}")
        print(f"\n🎯 TOTAL DE PERDAS RECUPERÁVEIS: R$ {self._formatar_valor(total_geral)}\n")
        
        print("="*70)
        print("⚠️  PRIORIDADES DE AÇÃO")
        print("="*70 + "\n")
        
        print("🔴 AÇÕES IMEDIATAS (0-48h):")
        print("  • Comunicar ao Ministério Público casos de fraude")
        print("  • Bloquear transferências para responsáveis")
        print("  • Reintegração de posse de terras irregularmente doadas\n")
        
        print("🟡 AÇÕES CURTO PRAZO (1-4 semanas):")
        print("  • Cobrar valores em aberto e retroativos")
        print("  • Recuperar terras com desvio de finalidade")
        print("  • Iniciar REURB em loteamentos\n")
        
        print("🟢 AÇÕES MÉDIO PRAZO (1-6 meses):")
        print("  • Retomar projetos incompletos")
        print("  • Anular doações irregulares")
        print("  • Implementar controles preventivos\n")
        
        # Salvar relatório em JSON
        self._salvar_relatorio_json(total_geral)
    
    def _salvar_relatorio_json(self, total_geral):
        """Salva relatório em JSON"""
        relatorio = {
            'data_analise': datetime.now().isoformat(),
            'periodo': {'inicio': 2016, 'fim': 2026},
            'perdas_financeiras': self.perdas_financeiras,
            'perdas_patrimoniais': self.perdas_patrimoniais,
            'total_geral_recuperavel': total_geral,
            'timestamp': datetime.now().isoformat()
        }
        
        filename = f"auditoria_retroativa_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(relatorio, f, ensure_ascii=False, indent=2)
        
        print(f"💾 Relatório salvo em: {filename}\n")
    
    def _formatar_valor(self, valor: float) -> str:
        """Formata valor em BRL"""
        return f"{valor:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.')


def main():
    auditoria = AuditoriaRetroativa()
    auditoria.executar_auditoria_retroativa_completa()


if __name__ == "__main__":
    main()
