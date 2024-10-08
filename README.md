# Emulação de Personagens com OpenAI e Edge-TTS

Este projeto emula personagens fictícios usando a API da OpenAI para gerar respostas e a biblioteca **Edge-TTS** para converter essas respostas em fala, com vozes dinâmicas e variáveis como velocidade de fala.

## Funcionalidades

- Geração de personagens aleatórios com características como nome, personalidade, histórico e estilo de fala.
- Uso da API da OpenAI para emular diálogos entre o usuário e os personagens.
- Conversão de texto em fala utilizando **Edge-TTS**, com variação de vozes, tonalidade e velocidade de fala.
- Facilidade para adicionar novas personalidades e estilos de fala.

## Pré-requisitos

- **Python 3.8+**
- Chave de API da OpenAI
- Instalador de pacotes `pip`

## Configuração do Ambiente

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/SEU_REPOSITORIO/emulacao-personagens.git
cd emulacao-personagens
```

### Passo 2: Configurar Variáveis de Ambiente

1. Renomeie o arquivo **`.env.example`** para **`.env`**:

```bash
cp .env.example .env
```

2. No arquivo **`.env`**, adicione sua chave de API da OpenAI:

```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Passo 3: Instalar Dependências

Instale as dependências necessárias utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Projeto

Agora, basta executar o projeto para começar a interagir com os personagens gerados aleatoriamente:

```bash
python main.py
```

## Estrutura do Projeto

- **main.py**: Arquivo principal que executa a lógica de emulação de personagens e interações.
- **.env**: Arquivo que armazena variáveis de ambiente, incluindo a chave de API da OpenAI. **Este arquivo é ignorado pelo Git.**
- **.env.example**: Um exemplo de como configurar as variáveis de ambiente.
- **requirements.txt**: Arquivo com as dependências do projeto, incluindo **OpenAI**, **Edge-TTS** e **python-dotenv**.

## Dependências

O projeto usa as seguintes bibliotecas Python:

- **openai**: Para acessar a API da OpenAI.
- **edge-tts**: Para converter texto em fala utilizando as vozes disponíveis no Microsoft Edge.
- **python-dotenv**: Para carregar as variáveis de ambiente do arquivo `.env`.

## Como Funciona

1. A cada execução, o projeto cria um personagem fictício com atributos aleatórios como:
   - Nome
   - Personalidade
   - Histórico
   - Estilo de Fala
   - Voz e velocidade de fala variáveis.
   
2. O usuário interage com o personagem, e as respostas são geradas usando a **OpenAI**.

3. As respostas são convertidas em fala usando o **Edge-TTS**.

## Contribuindo

1. Faça um fork do repositório.
2. Crie uma nova branch com sua feature ou correção de bug:
   ```bash
   git checkout -b feature/nome-da-feature
   ```
3. Faça commit de suas alterações:
   ```bash
   git commit -m "Adiciona nova feature"
   ```
4. Faça push para a branch:
   ```bash
   git push origin feature/nome-da-feature
   ```
5. Abra um Pull Request.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

## Notas

- Certifique-se de não compartilhar sua chave de API publicamente, mantendo o arquivo **`.env`** protegido e não incluído no controle de versão.
- Se encontrar problemas ou tiver sugestões, sinta-se à vontade para abrir uma issue no repositório.
