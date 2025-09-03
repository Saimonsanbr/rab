import discord
import random
import os

# Ative os intents para ler mensagens
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Lista de respostas aleatórias
respostas = [
    "Amigo, já pensou que talvez pinguins sejam só patos de smoking?",
    "E se a Terra for só um server que Deus esqueceu desligado?",
    "Odeio spoilers, mas seu futuro é tomar café amanhã.",
    "Será que o Wi-Fi também fica cansado?",
    "Imagina se galinhas tivessem dentes… medo."
]

@client.event
async def on_ready():
    print(f"Bot {client.user} está online! 🚀")

@client.event
async def on_message(message):
    # Evitar o bot responder a si mesmo
    if message.author == client.user:
        return

    # Chance de 5% de responder
    if random.random() < 0.05:
        resposta = random.choice(respostas)
        await message.channel.send(resposta)

# Rode o bot
TOKEN = os.getenv("DISCORD_TOKEN")  # configure no seu .env ou variável de ambiente
client.run(TOKEN)
