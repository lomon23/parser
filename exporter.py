# Встанови: pip install tabulate
from tabulate import tabulate
import pandas as pd

class Exporter:
    @staticmethod
    def to_csv(data: list, filename: str):
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        return filename

    @staticmethod
    def to_pretty_report(data: list, filename: str):
        """Зберігає дані у вигляді красивої ASCII-таблиці (псевдо-таблиця)."""
        if not data:
            return None
            
        # Формуємо таблицю
        # headers="keys" автоматично візьме назви з ключів словника
        table = tabulate(data, headers="keys", tablefmt="grid")
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(table)
            
        return filename