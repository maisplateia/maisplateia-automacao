import feedparser
from openai import OpenAI
import os

RSS_URL = "https://www.maisplateia.com.br/syndication/noticias/"

# Lê o RSS
feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("Nenhuma matéria encontrada.")
    exit()

materia = feed.entries[0]

titulo = materia.title
texto = materia.description
link = materia.link

cliente = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

prompt = f"""
Você é redator do Mais Plateia.

Adapte a matéria abaixo para redes sociais.

Título:
{titulo}

Texto:
{texto}

Link:
{link}

Crie uma versão para:

- Instagram
- Facebook
- Threads
- X
- Telegram
- WhatsApp
"""

resposta = cliente.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print(resposta.output_text)
