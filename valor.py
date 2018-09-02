import requests
from bs4 import BeautifulSoup as bs4


class ValorScraper:

    def __init__(self, keywords, page):
        self.keywords = [keyword.strip() for keyword in keywords.split(";")]
        self.page = "https://www.valor.com.br/{}".format(page)
        self.numbers = [str(x) for x in range(0,10)]

    def scrape(self):
        result = requests.get(self.page)
        return result.text

    def get_all_links(self):
        result = self.scrape()
        soup = bs4(result, 'html.parser')
        return soup.find_all('a')

    def retrieve_interesting_links(self):
        links = self.get_all_links()
        links_ret = []
        for link in links:
            if any(c in link.text.strip() for c in self.keywords):
                if any (num in link["href"] for num in self.numbers):
                    if "https://www.valor.com.br/" in link["href"]:
                        links_ret.append((link["href"], link.text.strip()))
                    else:
                        links_ret.append(
                            (
                                "https://www.valor.com.br{}".format(link["href"]),
                                link.text.strip()
                            )
                        )

        return links_ret


a = ValorScraper("FED; EUA", "internacional")
print(a.retrieve_interesting_links())
