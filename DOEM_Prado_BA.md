# 📰 DOEM - Diário Oficial do Estado da Bahia

## Dados da Prefeitura Municipal de Prado

**Link Oficial:** https://doem.org.br/ba/prado

---

## 📋 Publicações Recentes

| Data | Tipo | Descrição | Status |
|------|------|-----------|--------|
|      |      |           | ⏳ A preencher |

---

## 🔍 Como Raspar Dados do DOEM

### Script Python
```python
import requests
from bs4 import BeautifulSoup

url = "https://doem.org.br/ba/prado"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Processar dados
publicacoes = soup.find_all('div', class_='publicacao')
for pub in publicacoes:
    print(pub.text)
```

---

## 📊 Dados Consolidados

### Quantidade de Publicações
- **Total:** 0
- **Este mês:** 0
- **Esta semana:** 0

---

## 🎯 Próximas Ações

- [ ] Sincronizar dados do DOEM
- [ ] Atualizar base de compliance
- [ ] Gerar relatório mensal
- [ ] Validar conformidades

---

**Última sincronização:** 2026-06-03  
**Próxima sincronização:** 2026-06-04
