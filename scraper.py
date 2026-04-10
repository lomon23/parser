import requests
from bs4 import BeautifulSoup

class UniversalScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
        }

    def fetch_html(self, url: str) -> str:
        """Завантажує сторінку з обробкою помилок."""
        try:
            response = requests.get(url, headers=self.headers, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            raise ConnectionError(f"Помилка підключення до {url}: {e}")

    def extract_data(self, html: str, target_tag: str, target_class: str) -> list:
        """Витягує дані за заданим тегом та класом."""
        soup = BeautifulSoup(html, "html.parser")
        items = soup.find_all(target_tag, class_=target_class)
        
        extracted = []
        for index, item in enumerate(items, 1):

            raw_text = " ".join(item.stripped_strings)
            
            link_tag = item.find('a')
            link = link_tag.get('href') if link_tag else "Немає посилання"

            extracted.append({
                "ID": index,
                "Зміст": raw_text[:100] + "..." if len(raw_text) > 100 else raw_text,
                "Посилання": link
            })
            
        return extracted