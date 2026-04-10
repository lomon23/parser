import pandas as pd
import os

class Exporter:
    @staticmethod
    def to_csv(data: list, filename: str):
        """Зберігає список словників у CSV файл."""
        if not data:
            raise ValueError("Немає даних для збереження.")
            
        # Гарантуємо, що файл буде з розширенням .csv
        if not filename.endswith('.csv'):
            filename += '.csv'
            
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False, encoding="utf-8-sig")
        
        filepath = os.path.abspath(filename)
        return filepath