import edge_tts
import asyncio
import os

async def synthesize_speech(text, voice='pt-BR-AntonioNeural', rate='0%'):
    communicate = edge_tts.Communicate(text=text, voice=voice, rate=rate)
    filename = 'response.mp3'
    await communicate.save(filename)
    os.system(f"start {filename}")

# Chamar a função assíncrona
asyncio.run(synthesize_speech('teste de fala', voice='pt-BR-FranciscaNeural', rate='-30%'))