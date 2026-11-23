import csv
import time

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "scraper-estudo/1.0"}
dados = []


for pagina in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Página {pagina} falhou: {response.status_code}")
        break



    soup = BeautifulSoup(response.content, "html.parser")
    for livro in soup.select("article.product_pod"):
        dados.append({
            "titulo": livro.select_one("h3 a")["title"],
            "preco": livro.select_one("p.price_color").get_text(strip=True),
        })

    time.sleep(1)
with open("livros.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["titulo", "preco"])
    writer.writeheader()
    writer.writerows(dados)
print(f"{len(dados)} livros salvos")