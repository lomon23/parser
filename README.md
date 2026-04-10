# Universal Web Scraper CLI

A modular, interactive command-line tool written in Python for extracting data from generic HTML structures. Designed to avoid hardcoding selectors by taking target URLs and CSS classes directly via the CLI.

## Features
* **Interactive CLI**: Built with `rich` for a clean, colorful terminal experience with progress indicators.
* **Dynamic Selectors**: Target any HTML tag and class combination on the fly.
* **Data Export**: Automatically structures scraped data and exports it to a clean `.csv` format using `pandas`.
* **Modular Architecture**: Core scraping logic is strictly separated from the CLI and export modules.

## Tech Stack
* Python 3.10+
* `requests`, `beautifulsoup4`, `pandas`, `rich`

## Usage
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt` (or install manually).
3. Run the tool: `python main.py`
4. Follow the interactive prompts to input the target URL, HTML tag, and CSS class.