import os
import feedparser
from openai import OpenAI

RSS_URL = "https://www.maisplateia.com.br/syndication/noticias/"

# Lê o RSS
feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("Nenhuma matéria encontrada.")
    exit()

materia = feed.entries[0]

titulo = materia.get("title", "")
texto = materia.get("description", "")
link = materia.get("link", "")
autor = materia.get("author", "")
data = materia.get("published", "")

# Tenta obter a imagem da matéria
imagem = ""
if "media_thumbnail" in materia and len(materia.media_thumbnail) > 0:
    imagem = materia.media_thumbnail[0]["url"]
elif "media_content" in materia and len(materia.media_content) > 0:
    imagem = materia.media_content[0]["url"]

prompt = f"""
Você é redator do portal Mais Plateia.

Receberá uma matéria jornalística.

Crie versões prontas para publicação nas seguintes redes sociais:

- Instagram
- Facebook
- Threads
- X
- Telegram
- WhatsApp

Mantenha as informações principais da notícia.

Inclua emojis apenas quando fizer sentido.

No final de cada publicação coloque o link da matéria.

TÍTULO:
{titulo}

AUTOR:
{autor}

DATA:
{data}

IMAGEM:
{imagem}

TEXTO:
{texto}

LINK:
{link}
"""

client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

print(response.output_text)
