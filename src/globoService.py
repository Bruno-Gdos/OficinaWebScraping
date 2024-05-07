import requests
import bs4

CLASS_LINK_GLOBO = 'feed-post-link'


def get_news(url):

    """
    Função que recebe uma URL e retorna uma lista de dicionários contendo informações sobre as notícias encontradas.

    Parâmetros:
    url (str): A URL da página que contém as notícias.

    Retorna:
    list: Uma lista de dicionários contendo as informações das notícias encontradas. Cada dicionário possui as chaves 'titulo', 'corpo' e 'link'.

    """

    # Faz uma requisição GET para a URL fornecida
    response = requests.get(url)
    
    # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    
    # Encontra todos os elementos <a> com a classe definida em CLASS_LINK_GLOBO
    links = soup.find_all('a', class_=CLASS_LINK_GLOBO)
    
    noticias = []    
    # Itera sobre cada link encontrado
    for link in links:

        try:

            # Faz uma requisição GET para o link encontrado
            response_link = requests.get(link.get('href'))
            
            # Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta do link
            soup_link = bs4.BeautifulSoup(response_link.text, 'html.parser')
            
            # Extrai o título da notícia
            titulo = soup_link.find(class_='content-head__title').text
            
            # Extrai o corpo da notícia
            corpo = soup_link.find_all(class_="content-text__container")
            
            # Concatena o texto de cada elemento do corpo da notícia em uma única string
            strings = '\n'.join([elemento.get_text() for elemento in corpo])
            
            # Adiciona um dicionário contendo as informações da notícia à lista de notícias
            noticias.append({'titulo': titulo, 'corpo': strings, 'link': link['href']}),
        
        except:
            # Em caso de erro, imprime a mensagem de erro e continua para a próxima notícia
            print(f"Erro ao pegar dados da noticia: {link.get('href')}" if link.get('href') else 'Erro ao pegar dados da noticia')
            continue
    
    # Retorna a lista de notícias encontradas
    return noticias