from scraper import scrape_all_matches
from cleaner import clean_all_csv_files
from dotenv import load_dotenv
import os
import glob

load_dotenv()
BASE_URL = os.getenv("BASE_URL")
MATCH_IDS = os.getenv("MATCH_IDS").split(",")
OUTPUT_DIR_RAW = os.getenv("OUTPUT_DIR_RAW")
OUTPUT_DIR_CLEAN = os.getenv("OUTPUT_DIR_CLEAN")


def main():
    os.makedirs(OUTPUT_DIR_CLEAN, exist_ok=True)
    check_path = os.path.join(OUTPUT_DIR_CLEAN, '*.csv')
    existing_files = glob.glob(check_path)

    if existing_files:
        print(f"Data is already there in path {OUTPUT_DIR_CLEAN}. Terminating system.")
        return

    print("No existing data found. Starting scraping process...")
    match_ids = MATCH_IDS
    scrape_all_matches(match_ids, BASE_URL, OUTPUT_DIR_RAW)

    clean_all_csv_files(f'{OUTPUT_DIR_RAW}/*.csv', OUTPUT_DIR_CLEAN)
    print("All matches scraped and cleaned successfully!")


if __name__ == "__main__":
    main()
