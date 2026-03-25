# FIVB Volleyball Stats Scraper

This project is a web scraper built to extract and clean player statistics from the FIVB Volleyball World Championship website. It uses **Playwright** for robust browser automation and **Pandas** for data cleaning and transformation.

The primary goal is to demonstrate a simple, maintainable, and extensible data pipeline, from raw data extraction to a clean, analysis-ready dataset.

-----

## Key Features

* **Targeted Scraping**: Extracts 6 key player-stat categories: Scoring, Attack, Block, Serve, Reception, and Dig.
* **Data Cleaning**: Processes raw, nested data into a clean, flat, tabular format (one row per player per stat).
* **Configurable**: Uses a `.env` file to manage match IDs, base URLs, and output directories.
* **Idempotent**: The script checks if clean data already exists before running, preventing redundant scraping.
* **Modular**: Code is separated by concern:
    * `scraper.py`: Handles all browser interaction and data extraction.
    * `cleaner.py`: Handles all data transformation and cleaning.
    * `main.py`: Acts as the main controller.

-----

## Tech Stack

* **Python**: The core programming language.
* **Playwright**: For web scraping and browser automation.
* **Pandas**: For data cleaning, transformation, and processing.
* **python-dotenv**: For managing environment variables and configuration.

-----

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1\. Clone the Repository

```bash
git clone https://github.com/Eceakinci/MatchScraping
cd MatchScraping
```

### 2\. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

### 3\. Install Dependencies

Install all required Python packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 4\. Install Playwright Browsers

Playwright requires its own set of browser binaries. This command downloads them.

```bash
playwright install
```

-----

## How to Run

Once you have completed the setup, you can run the entire pipeline with a single command:

```bash
cd src
python main.py
```

### What Happens:

1.  The script checks if `.csv` files already exist in your `OUTPUT_DIR_CLEAN` (`data/clean/`).
2.  If files exist, it prints a message and exits.
3.  If not, it launches Playwright, scrapes all `MATCH_IDS`, and saves the raw data to `OUTPUT_DIR_RAW` (`data/raw/`).
4.  It then runs the cleaning script, which reads from `data/raw/`, processes the data, and saves the final, clean CSV files to `OUTPUT_DIR_CLEAN` (`data/clean/`).

-----

## Project Structure

```

├── .env
├── requirements.txt
└── src/              # (This directory is created by the script)
    ├── main.py
    ├── scraper.py
    ├── cleaner.py
    └── data
        ├── raw/           # Stores raw CSVs with nested data
            └── ...        # Raw stats for matches
        └── clean/         # Stores final, analysis-ready CSVs
            └── ...        # Clean stats for matches
```

-----

## How It Works: Data Flow

This project follows a simple **Extract, Load, Transform (ELT)** pattern.

1.  **Orchestration (`main.py`)**: The `main.py` script acts as the orchestrator. It first checks for existing data in the "clean" directory to ensure idempotency.
2.  **Extract (`scraper.py`)**: If no clean data is found, it calls `scrape_all_matches()`. This function uses Playwright to navigate to each match URL, extract the raw stats tables, and save them as-is (with nested list data) into the `data/raw` directory.
3.  **Transform (`cleaner.py`)**: `main.py` then calls `clean_all_csv_files()`. This script reads each raw CSV from `data/raw`, uses Pandas to "explode" the nested lists into proper tabular rows, adds a `match_id` column for reference, and saves the final, clean data to the `data/clean` directory.