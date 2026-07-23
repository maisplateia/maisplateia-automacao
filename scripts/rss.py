import feedparser
import json

RSS_URL = "https://www.maisplateia.com.br/syndication/noticias/"

feed = feedparser.parse(RSS_URL)

if not feed.entries:
    print("Nenhuma notícia encontrada.")
    exit()

noticia = feed.entries[0]

dados = {
    "titulo": noticia.title,
    "link": noticia.link,
    "descricao": noticia.description,
    "autor": noticia.get("author", ""),
    "data": noticia.get("published", "")
}

print(json.dumps(dados, indent=4, ensure_ascii=False))
