import mysql.connector
from dotenv import load_dotenv
import openai
import edge_tts
import random
import asyncio
import os

load_dotenv()
# Configurações do banco de dados
db_config = {
    "host": "localhost",
    "user": "root",  # Substitua por seu usuário do MySQL
    "password": "",  # Substitua pela sua senha do MySQL
    "database": "ia",  # Certifique-se de que este é o nome correto do seu banco de dados
}

# Conexão com o banco de dados
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)

# Configurar a chave de API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")
# Listas de atributos possíveis para o personagem
character_names = ["Antonio", "Francisca", "Duarte", "Raquel"]
personalities = ["Amigável", "Sério", "Engraçado", "Inteligente"]
backgrounds = ["Cientista", "Aventureiro", "Professor", "Músico"]
speaking_styles = ["Formal", "Informal", "Descontraído", "Educado"]

# Vozes disponíveis do Edge-TTS
voices = [
    {
        "name": "Antonio",
        "short_name": "pt-BR-AntonioNeural",
        "gender": "Male",
        "locale": "pt-BR",
    },
    {
        "name": "Francisca",
        "short_name": "pt-BR-FranciscaNeural",
        "gender": "Female",
        "locale": "pt-BR",
    },
    {
        "name": "Duarte",
        "short_name": "pt-PT-DuarteNeural",
        "gender": "Male",
        "locale": "pt-PT",
    },
    {
        "name": "Raquel",
        "short_name": "pt-PT-RaquelNeural",
        "gender": "Female",
        "locale": "pt-PT",
    },
]

# Faixas para velocidade e tonalidade (rate) com incrementos de 5%
rate_range = [
    "-20%",
    "-15%",
    "-10%",
    "-5%",
    "0%",
    "+5%",
    "+10%",
    "+15%",
    "+20%",
    "+25%",
    "+30%",
]


# Função para criar um novo personagem aleatório
def create_random_character():
    name = random.choice(character_names)
    personality = random.choice(personalities)
    background = random.choice(backgrounds)
    speaking_style = random.choice(speaking_styles)
    voice = random.choice(voices)
    rate = random.choice(rate_range)  # Velocidade de fala aleatória

    character = {
        "name": name,
        "personality": personality,
        "background": background,
        "speaking_style": speaking_style,
        "voice": voice,
        "rate": rate,  # Adicionar a velocidade ao personagem
    }

    return character


# Função assíncrona para síntese de fala usando edge-tts
async def synthesize_speech(text, voice="pt-BR-AntonioNeural", rate="0%"):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    filename = "response.mp3"
    await communicate.save(filename)
    os.system(f"start {filename}")


# Criar um personagem novo
selected_character = create_random_character()

# Exibir as informações do personagem
print(f"Nome: {selected_character['name']}")
print(f"Personalidade: {selected_character['personality']}")
print(f"Histórico: {selected_character['background']}")
print(f"Estilo de fala: {selected_character['speaking_style']}")
print(f"Voz selecionada: {selected_character['voice']['short_name']}")
print(f"Velocidade de fala: {selected_character['rate']}")

# Histórico da conversa
history = []

# Loop de interação
while True:
    user_input = input("Você: ")
    if user_input.lower() in ["sair", "exit", "quit"]:
        break

    # Construir o contexto
    messages = [
        {
            "role": "system",
            "content": (
                f"You are {selected_character['name']}.\n"
                f"Personality: {selected_character['personality']}.\n"
                f"Background: {selected_character['background']}.\n"
                f"Speaking Style: {selected_character['speaking_style']}."
            ),
        }
    ]

    # Adicionar histórico da conversa
    messages.extend(history)

    # Adicionar a entrada do usuário
    messages.append({"role": "user", "content": user_input})

    try:
        # Chamar a API da OpenAI
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

        # Extrair a resposta
        character_response = response["choices"][0]["message"]["content"]
        print(f"{selected_character['name']}: {character_response}")

        # Atualizar o histórico
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": character_response})

        # Sintetizar e reproduzir a resposta usando edge-tts
        asyncio.run(
            synthesize_speech(
                character_response,
                voice=selected_character["voice"][
                    "short_name"
                ],  # Usar a voz do personagem
                rate=selected_character[
                    "rate"
                ],  # Usar a velocidade aleatória do personagem
            )
        )

    except openai.error.OpenAIError as e:
        print(f"Ocorreu um erro ao chamar a API da OpenAI: {e}")

# Encerrar o programa
print("Encerrando a conversa...")
