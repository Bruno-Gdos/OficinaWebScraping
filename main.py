import pandas as pd
import src.globoService as globo

URL_GLOBO = "https://g1.globo.com/"

def obter_noticias(url):
    """
    Obtém as notícias do site Globo.com.

    Args:
        url (str): A URL do site Globo.com.

    Returns:
        list: Uma lista de dicionários contendo as notícias obtidas.
    """
    return globo.get_news(url)

# Obtém as notícias do site Globo.com
noticias = obter_noticias(URL_GLOBO)

# Cria um DataFrame a partir das notícias obtidas
df = pd.DataFrame(noticias)

# Salva o DataFrame em um arquivo Excel
df.to_excel('news.xlsx', index=False)
