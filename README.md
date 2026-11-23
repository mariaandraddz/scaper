# Web Scraper de Livros
 
Script em Python que faz web scraping do site [books.toscrape.com](https://books.toscrape.com), um site criado para praticar scraping, e salva o título e o preço de todos os livros em um arquivo CSV.
 
## O que o projeto faz
 
- Percorre as 50 páginas do catálogo
- Extrai o **título** e o **preço** de cada livro (1000 no total)
- Salva os resultados em `livros.csv`
- Faz uma pausa de 1 segundo entre as requisições para não sobrecarregar o servidor
## Requisitos
 
- Python 3.9 ou superior
- Bibliotecas `requests` e `beautifulsoup4`
## Instalação
 
1. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
 
# Windows
.venv\Scripts\activate
 
# Linux/macOS
source .venv/bin/activate
```
 
2. Instale as dependências:
```bash
pip install requests beautifulsoup4
```
 
## Como executar
 
Pelo terminal, dentro da pasta do projeto:
 
```bash
python scraper.py
```
 
No PyCharm, abra o `scraper.py` e clique no ícone ▶ (ou use **Shift+F10**).
 
Ao final, o terminal exibe `1000 livros salvos` e o arquivo `livros.csv` é criado na mesma pasta.
 
## Estrutura do projeto
 
```
scraper/
├── scraper.py    # código do scraper
├── livros.csv    # resultado (gerado após a execução)
└── README.md
```
 
## Formato do resultado
 
O `livros.csv` tem duas colunas:
 
| titulo                  | preco  |
|-------------------------|--------|
| A Light in the Attic    | £51.77 |
| Tipping the Velvet      | £53.74 |
 
Se os acentos ou o símbolo `£` aparecerem errados no Excel, importe o arquivo em **Dados → De Texto/CSV** e escolha a codificação **UTF-8**.
 
## Como funciona
 
1. `requests` baixa o HTML de cada página do catálogo
2. `BeautifulSoup` faz o parsing e localiza cada livro com o seletor `article.product_pod`
3. O título vem do atributo `title` do link dentro de `h3`, e o preço do elemento `p.price_color`
4. Os dados são gravados com o módulo `csv` da biblioteca padrão
## Boas práticas de scraping
 
- Verifique se o site oferece uma API antes de raspar o HTML
- Leia o `robots.txt` e os Termos de Uso do site
- Evite coletar dados pessoais (LGPD)
- Mantenha pausas entre as requisições e identifique seu scraper com um `User-Agent` honesto
## Próximos passos
 
- Extrair mais campos: avaliação, disponibilidade e link de cada livro
- Converter o preço para número (remover o `£`)
- Analisar os dados com `pandas`
- Adaptar o código para outro site, ajustando os seletores
 