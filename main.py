from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from scraper import UniversalScraper
from exporter import Exporter

console = Console()

def display_header():
    console.print(Panel.fit(
        "[bold cyan]Universal Web Scraper CLI v1.1[/bold cyan]\n"
        "[dim]Розроблено для швидкого збору даних з будь-яких HTML-структур\n"
        "Підтримка експорту: CSV (сирі дані) та TXT (форматовані таблиці)[/dim]",
        border_style="cyan"
    ))

def main():
    display_header()
    
    url = Prompt.ask("\n[bold yellow]1.[/bold yellow] Введіть [green]URL[/green] сайту")
    tag = Prompt.ask("[bold yellow]2.[/bold yellow] Введіть [green]HTML тег[/green] контейнера (напр. div, article, li)")
    css_class = Prompt.ask("[bold yellow]3.[/bold yellow] Введіть [green]CSS клас[/green] контейнера (напр. product_pod)")
    
    scraper = UniversalScraper()
    
    try:

        with console.status(f"[bold green]Завантаження {url}...", spinner="dots"):
            html = scraper.fetch_html(url)
            
        with console.status("[bold green]Парсинг DOM-дерева...", spinner="bouncingBar"):
            data = scraper.extract_data(html, tag, css_class)
            
        if not data:
            console.print(f"[bold red]❌ За тегом <{tag} class=\"{css_class}\"> нічого не знайдено.[/bold red]")
            return

        console.print(f"\n[bold green]✅ Знайдено елементів: {len(data)}[/bold green]")
        
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=4)
        table.add_column("Текст блоку", min_width=30)
        table.add_column("Посилання", style="blue")
        
        for row in data[:5]:
            table.add_row(str(row["ID"]), row["Зміст"], row["Посилання"])
            
        console.print(table)
        if len(data) > 5:
            console.print(f"[dim]... та ще {len(data) - 5} записів приховано.[/dim]")

        console.print("\n[bold cyan]=== Налаштування експорту ===[/bold cyan]")
        export_format = Prompt.ask(
            "[bold yellow]4.[/bold yellow] Виберіть формат збереження", 
            choices=["csv", "txt"], 
            default="csv"
        )
        
        base_filename = Prompt.ask(
            "[bold yellow]5.[/bold yellow] Введіть назву файлу (без розширення)", 
            default="scraped_data"
        )
        
        # Виклик відповідного методу з exporter.p
        if export_format == "csv":
            saved_path = Exporter.to_csv(data, f"{base_filename}.csv")
        else:
            saved_path = Exporter.to_pretty_report(data, f"{base_filename}.txt")
        
        console.print(f"\n[bold green]🎉 Дані успішно збережено у:[/bold green] {saved_path}")

    except Exception as e:
        console.print(f"\n[bold red]❌ Сталася помилка:[/bold red] {e}")

if __name__ == "__main__":
    main()