# EEG Motor Imagery Classification using MNE-Python and Machine Learning

Este repositório contém um pipeline completo para o processamento de sinais de Eletroencefalografia (EEG) e a classificação de tarefas de **Motor Imagery** (imaginação de movimento). O projeto utiliza a biblioteca **MNE-Python** para manipulação de dados neurofisiológicos e **Scikit-learn** para a etapa de aprendizado de máquina.

## 🧠 Sobre o Projeto

A imaginação de movimento (Motor Imagery - MI) é uma técnica onde o indivíduo imagina a execução de um movimento sem realizá-lo fisicamente. Isso gera padrões específicos de atividade cerebral que podem ser capturados por EEG e traduzidos em comandos para interfaces cérebro-computador (BCI).

Este projeto foca na classificação de diferentes estados de MI, aplicando técnicas rigorosas de pré-processamento e extração de características no domínio da frequência.

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **MNE-Python**: Processamento e visualização de dados de EEG.
- **Scikit-learn**: Implementação de modelos de Machine Learning.
- **NumPy & Pandas**: Manipulação de dados e matrizes.
- **Matplotlib**: Visualização de sinais e resultados.

## 📊 Pipeline de Processamento

O fluxo de trabalho está dividido em quatro etapas principais:

1.  **Pré-processamento (`preprocess.py`)**:
    - Carregamento de dados brutos (Raw).
    - Aplicação de filtros de banda (Band-pass filter: 7Hz - 30Hz) para isolar ritmos mu e beta.
    - Remoção de artefatos e normalização.

2.  **Criação de Épocas (`create_epoch.py`)**:
    - Segmentação do sinal contínuo em janelas temporais (épocas) baseadas em eventos de estímulo.
    - Definição de janelas de tempo (ex: 0s a 4s após o trigger).

3.  **Extração de Características (`feature_extraction.py`)**:
    - Cálculo da Densidade Espectral de Potência (**PSD - Power Spectral Density**).
    - Transformação dos sinais do domínio do tempo para o domínio da frequência para identificar padrões de ativação cortical.

4.  **Treinamento e Avaliação (`train_model.py`)**:
    - Divisão dos dados em conjuntos de treino e teste.
    - Treinamento de classificadores (ex: **Random Forest**).
    - Avaliação de métricas de acurácia e performance.

## 🚀 Como Executar

### Pré-requisitos

Certifique-se de ter o Python instalado e instale as dependências necessárias:

```bash
pip install mne scikit-learn numpy pandas matplotlib
```

### Execução

Para rodar o pipeline completo, execute o arquivo principal:

```bash
python main.py
```

Ou explore o passo a passo detalhado através do Jupyter Notebook:
`classifica-o-de-movimento-imaginado-usando-eeg.ipynb`

## 📈 Resultados

O modelo atual utiliza **Random Forest** para classificação, alcançando resultados promissores na distinção entre diferentes tarefas de imaginação motora. O pipeline é modular, permitindo a fácil substituição de classificadores ou ajuste de parâmetros de filtragem.

## 📂 Estrutura do Repositório

```text
├── src/
│   ├── preprocess.py        # Funções de filtragem e limpeza
│   ├── create_epoch.py      # Segmentação de eventos
│   ├── feature_extraction.py # Cálculo de PSD e features
│   └── train_model.py       # Lógica de ML e avaliação
├── main.py                  # Script principal de execução
└── classifica-o-de-movimento-imaginado-usando-eeg.ipynb # Análise exploratória
```

---
Desenvolvido por [Caio Veloso](https://github.com/Caio-Veloso1) como parte de estudos em Neuroengenharia e Inteligência Artificial.
