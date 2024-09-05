
# Sistema de Monitoramento de Trânsito - Florianópolis

Este projeto implementa um sistema interativo de monitoramento de trânsito em tempo real para a cidade de Florianópolis, usando a API do Google Maps. O sistema coleta dados de trânsito entre dois pontos específicos e apresenta as informações em um painel interativo construído com Streamlit. O objetivo é fornecer um recurso para visualização do trânsito em tempo real e um histórico gráfico de tempos de viagem estimados.

## Funcionalidades Principais

- **Coleta de dados de trânsito** em tempo real usando a API do Google Maps, incluindo o tempo estimado de viagem.
- **Visualização gráfica do histórico** de tempos de viagem entre os pontos definidos.
- **Painel interativo com Streamlit** para exibir os dados de trânsito em tempo real e o histórico de viagens em um gráfico.
- **Suporte a múltiplas execuções**, permitindo que o usuário colete e visualize novos dados de trânsito a cada execução.
  
## Tecnologias Utilizadas

- **Python 3.8+**
- **Google Maps API**
- **Streamlit** para o painel interativo.
- **Pandas** para manipulação e visualização de dados.
- **Matplotlib** para visualização gráfica dos dados.
- **Python-dotenv** para gerenciar variáveis de ambiente.

## Estrutura do Projeto

```bash
├── .venv/                # Ambiente virtual com as dependências do projeto
├── main.py               # Script principal para coleta de dados
├── transito_painel.py     # Script para rodar o painel interativo com Streamlit
├── dados_transito.csv     # Arquivo de saída onde os dados coletados são armazenados (gerado durante a execução)
├── README.md             # Documentação do projeto
├── requirements.txt      # Arquivo com as dependências do projeto
├── .gitignore            # Arquivo para ignorar arquivos indesejados no Git
└── .env                  # Arquivo de configuração das variáveis de ambiente
```

## Requisitos

Antes de começar, você precisará ter instalado:

- Python 3.8 ou superior
- Chave da API do Google Maps (instruções abaixo)

### Dependências do Projeto

O projeto depende das seguintes bibliotecas Python:

- `googlemaps`
- `streamlit`
- `pandas`
- `matplotlib`
- `python-dotenv`

Estas dependências estão listadas no arquivo `requirements.txt`.

## Instalação

### Passo 1: Clonar o Repositório

Clone este repositório na sua máquina local:

```bash
git clone https://github.com/seu-usuario/transito_floripa.git
cd transito_floripa
```

### Passo 2: Criar o Ambiente Virtual

Crie um ambiente virtual para o projeto:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

- No Windows:
  ```bash
  .venv\Scripts\activate
  ```
- No Linux/Mac:
  ```bash
  source .venv/bin/activate
  ```

### Passo 3: Instalar as Dependências

Instale as dependências do projeto listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Passo 4: Configurar as Variáveis de Ambiente

Crie um arquivo **`.env`** na raiz do projeto e insira a sua chave da API do Google Maps:

```env
GOOGLE_MAPS_API_KEY=your_api_key_here
```

Você pode obter uma chave da API do Google Maps [aqui](https://console.cloud.google.com/).

## Usabilidade

### Coleta de Dados de Trânsito

O script principal **`main.py`** coleta os dados de trânsito entre dois pontos definidos (neste caso, `Centro` e `Lagoa da Conceição` em Florianópolis) e salva os dados em um arquivo CSV.

Para rodar o script, execute o seguinte comando:

```bash
python main.py
```

### Painel Interativo com Streamlit

O **`transito_painel.py`** cria um painel interativo para visualizar os dados de trânsito em tempo real e o gráfico do histórico de tempos de viagem.

Para rodar o painel, execute:

```bash
streamlit run transito_painel.py
```

Isso abrirá o painel no seu navegador, onde você poderá:

- Clicar no botão **"Atualizar Trânsito"** para coletar novos dados de trânsito.
- Clicar no botão **"Mostrar Gráfico"** para visualizar o histórico de tempos de viagem em um gráfico.

### Saída

O sistema gera um arquivo CSV chamado **`dados_transito.csv`** que armazena os dados de trânsito coletados em formato tabular, incluindo:

- Origem
- Destino
- Tempo estimado de viagem
- Horário da coleta de dados

## Exemplo de Uso

1. Execute o script principal para coletar dados de trânsito:

   ```bash
   python main.py
   ```

2. Visualize o painel interativo e o gráfico de histórico de trânsito:

   ```bash
   streamlit run transito_painel.py
   ```

   No painel, você poderá ver o tempo estimado de viagem e clicar em "Mostrar Gráfico" para visualizar um gráfico do histórico.

## Como Contribuir

Se você deseja contribuir para este projeto, siga os passos abaixo:

1. Faça um fork do projeto.
2. Crie uma nova branch para a sua funcionalidade:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça suas alterações e commit:
   ```bash
   git commit -m "Implementa nova funcionalidade"
   ```
4. Envie para sua branch remota:
   ```bash
   git push origin feature/nova-funcionalidade
   ```

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
