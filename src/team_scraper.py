import csv

from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL_TEAM")
TEAM_IDS = os.getenv("TEAM_IDS").split(",")
OUTPUT_DIR_RAW = os.getenv("OUTPUT_DIR_RAW_TEAMS")


def scrape_teamlist(page, team_id, output_dir_raw):
    team_data = []
    # table element's class
    scoring_list = page.locator(".vbw-o-table.vbw-team-roster-table").all()
    for pl in scoring_list:
        # colnames are same in all table
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        position = pl.locator(".vbw-o-table__cell.position").all_inner_texts()
        team = pl.locator(".vbw-team_header_name").all_inner_texts()

        team_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "position": position,
            "team": team
        })
    with open(f"{output_dir_raw}/{team_id}.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "position", "team"])
        writer.writeheader()
        writer.writerows(team_data)

def scrape_all_matches(team_ids, base_url, output_dir_raw):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        os.makedirs(output_dir_raw, exist_ok=True)
        print(f"Match ID's: {team_ids}")
        for match_id in team_ids:
            url = f"{base_url}/{match_id}/players"
            page.goto(url)
            page.wait_for_selector(".vbw-o-table__body")
            scrape_teamlist(page, match_id, output_dir_raw)
        browser.close()


if __name__ == "__main__":
    scrape_all_matches(TEAM_IDS, BASE_URL, OUTPUT_DIR_RAW)
