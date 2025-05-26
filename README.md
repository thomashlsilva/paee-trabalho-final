# 📦 Análise Estatística de Meta-heurísticas para o Problema do Caixeiro Viajante

Este repositório contém os códigos, dados e análises desenvolvidas para o artigo:

**Análise Estatística de Meta-heurísticas para o Problema do Caixeiro Viajante**  
*Daniel Silva da Fonseca, Thomás Henrique Lopes Silva*

Que foi produzido como parte das atividades da disciplina Planejamento e Análise Estatística de Experimentos (PAEE), ministrada pelos professores Elizabeth Fialho Wanner e Fabio Rocha da Silva.

---

## 📚 Descrição

O projeto analisa o desempenho das meta-heurísticas **Simulated Annealing (SA)** e **GRASP** na resolução do **Problema do Caixeiro Viajante (TSP)**.

Três cenários foram avaliados:

| Cenário | Nº de Cidades | Valor Ótimo |
|---------|----------------|--------------|
| pa561   | 561            | 2763         |
| si535   | 535            | 48450        |
| si1032  | 1032           | 92650        |

As análises incluem:

- Implementações dos algoritmos SA, GRASP, Tabu Search e Força Bruta (para pequenas instâncias).
- Estudo estatístico sobre as soluções obtidas.
- Testes de normalidade e comparação das distribuições dos algoritmos.

---

## 🚀 Como Executar

### 📌 Python

1. Instale as dependências:
```bash
pip install numpy matplotlib pandas tqdm
````

2. Execute os scripts:

```bash
python scripts/main.py
```

3. Converta arquivos TSPLIB em matrizes:

```bash
python scripts/mirrormatrix.py
```

4. Rode o modelo de força bruta (apenas instâncias pequenas):

```bash
python scripts/tsp_bruto.py
```

---

### 📌 R

1. Instale as dependências:

```r
install.packages(c("ggplot2", "reshape2"))
```

2. Execute o script de análise:

```r
source("analysis_tsp.R")
```

3. O script irá gerar:

* Testes de normalidade
* Gráficos de densidade
* Arquivos PNG com os gráficos

---

## 👥 Autores

* Daniel Silva da Fonseca - [daniel0547@gmail.com](mailto:daniel0547@gmail.com)
* Thomás Henrique Lopes Silva - [thomashlsilva@gmail.com](mailto:thomashlsilva@gmail.com)

---

## 💡 Referências

* [TSPLIB - Gerhard Reinelt](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/)
* Van Laarhoven & Aarts - *Simulated Annealing*
* Feo & Resende - *GRASP*
* Gendreau & Potvin - *Handbook of Metaheuristics*
