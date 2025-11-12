import csv
from playwright.sync_api import sync_playwright
import os


def scrape_scoring_stats(page, match_id, output_dir_raw):
    scoring_data = []
    scoring_list = page.locator(".vbw-stats-scoring.vbw-set-all").all()
    for pl in scoring_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        position = pl.locator(".vbw-o-table__cell.position").all_inner_texts()
        totalabs = pl.locator(".vbw-o-table__cell.total-abs").all_inner_texts()
        attacks = pl.locator(".vbw-o-table__cell.attacks").all_inner_texts()
        blocks = pl.locator(".vbw-o-table__cell.blocks").all_inner_texts()
        serves = pl.locator(".vbw-o-table__cell.serves").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.efficiency-percentage").all_inner_texts()

        scoring_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "position": position,
            "scoring_totalabs": totalabs,
            "scoring_attacks": attacks,
            "scoring_blocks": blocks,
            "scoring_serves": serves,
            "scoring_efficiency_percentage": efficiencypercentage
        })
    with open(f"{output_dir_raw}/{match_id}_scoring.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "position", "scoring_totalabs", "scoring_attacks",
                                               "scoring_blocks", "scoring_serves", "scoring_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(scoring_data)


def scrape_attack_stats(page, match_id, output_dir_raw):
    attack_data = []
    attack_list = page.locator(".vbw-stats-attack.vbw-set-all").all()
    for pl in attack_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        point = pl.locator(".vbw-o-table__cell.point").all_inner_texts()
        errors = pl.locator(".vbw-o-table__cell.errors").all_inner_texts()
        attempts = pl.locator(".vbw-o-table__cell.attempts").all_inner_texts()
        total = pl.locator(".vbw-o-table__cell.total").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.efficiency-percentage").all_inner_texts()

        attack_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "attack_point": point,
            "attack_errors": errors,
            "attack_attempts": attempts,
            "attack_total": total,
            "attack_serves": total,
            "attack_efficiency_percentage": efficiencypercentage
        })

    with open(f"{output_dir_raw}/{match_id}_attack.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "attack_point", "attack_errors", "attack_attempts",
                                               "attack_total", "attack_serves", "attack_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(attack_data)


def scrape_block_stats(page, match_id, output_dir_raw):
    block_data = []
    block_list = page.locator(".vbw-stats-block.vbw-set-all").all()
    for pl in block_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        point = pl.locator(".vbw-o-table__cell.point").all_inner_texts()
        errors = pl.locator(".vbw-o-table__cell.errors").all_inner_texts()
        touches = pl.locator(".vbw-o-table__cell.touches").all_inner_texts()
        total = pl.locator(".vbw-o-table__cell.total").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.efficiency-percentage").all_inner_texts()

        block_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "block_point": point,
            "block_errors": errors,
            "block_touches": touches,
            "block_total": total,
            "block_serves": total,
            "block_efficiency_percentage": efficiencypercentage
        })

    with open(f"{output_dir_raw}/{match_id}_block.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "block_point", "block_errors", "block_touches",
                                               "block_total", "block_serves", "block_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(block_data)


def scrape_serve_stats(page, match_id, output_dir_raw):
    serve_data = []
    serve_list = page.locator(".vbw-stats-serve.vbw-set-all").all()
    for pl in serve_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        point = pl.locator(".vbw-o-table__cell.point").all_inner_texts()
        errors = pl.locator(".vbw-o-table__cell.errors").all_inner_texts()
        attempts = pl.locator(".vbw-o-table__cell.attempts").all_inner_texts()
        total = pl.locator(".vbw-o-table__cell.total").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.efficiency-percentage").all_inner_texts()

        serve_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "serve_point": point,
            "serve_errors": errors,
            "serve_attempts": attempts,
            "serve_total": total,
            "serve_efficiency_percentage": efficiencypercentage
        })

    with open(f"{output_dir_raw}/{match_id}_serve.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "serve_point", "serve_errors", "serve_attempts",
                                               "serve_total", "serve_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(serve_data)


def scrape_reception_stats(page, match_id, output_dir_raw):
    reception_data = []
    reception_list = page.locator(".vbw-stats-reception.vbw-set-all").all()
    for pl in reception_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        successful = pl.locator(".vbw-o-table__cell.successful").all_inner_texts()
        errors = pl.locator(".vbw-o-table__cell.errors").all_inner_texts()
        attempts = pl.locator(".vbw-o-table__cell.attempts").all_inner_texts()
        total = pl.locator(".vbw-o-table__cell.total").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.efficiency-percentage").all_inner_texts()

        reception_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "reception_successful": successful,
            "reception_errors": errors,
            "reception_attempts": attempts,
            "reception_total": total,
            "reception_efficiency_percentage": efficiencypercentage
        })

    with open(f"{output_dir_raw}/{match_id}_reception.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "reception_successful", "reception_errors", "reception_attempts",
                                               "reception_total", "reception_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(reception_data)


def scrape_dig_stats(page, match_id, output_dir_raw):
    dig_data = []
    dig_list = page.locator(".vbw-stats-dig.vbw-set-all").all()
    for pl in dig_list:
        shirtnumber = pl.locator(".vbw-o-table__cell.shirtnumber").all_inner_texts()
        name = pl.locator(".vbw-o-table__cell.playername").all_inner_texts()
        digs = pl.locator(".vbw-o-table__cell.digs").all_inner_texts()
        errors = pl.locator(".vbw-o-table__cell.errors").all_inner_texts()
        attempts = pl.locator(".vbw-o-table__cell.attempts").all_inner_texts()
        efficiencypercentage = pl.locator(".vbw-o-table__cell.total").all_inner_texts()

        dig_data.append({
            "shirt_number": shirtnumber,
            "name": name,
            "digs": digs,
            "dig_errors": errors,
            "dig_attempts": attempts,
            "dig_efficiency_percentage": efficiencypercentage
        })

    with open(f"{output_dir_raw}/{match_id}_dig.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["shirt_number", "name", "digs", "dig_errors", "dig_attempts",
                                            "dig_efficiency_percentage"])
        writer.writeheader()
        writer.writerows(dig_data)


def scrape_match_data(page, match_id, output_dir_raw):
    scrape_scoring_stats(page, match_id, output_dir_raw)
    scrape_attack_stats(page, match_id, output_dir_raw)
    scrape_block_stats(page, match_id, output_dir_raw)
    scrape_serve_stats(page, match_id, output_dir_raw)
    scrape_reception_stats(page, match_id, output_dir_raw)
    scrape_dig_stats(page, match_id, output_dir_raw)


def scrape_all_matches(match_ids, base_url, output_dir_raw):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        os.makedirs(output_dir_raw, exist_ok=True)
        print(match_ids)
        for match_id in match_ids:
            url = f"{base_url}/{match_id}/#boxscore"
            page.goto(url)
            page.wait_for_selector(".vbw-mu__player")
            scrape_match_data(page, match_id, output_dir_raw)
        browser.close()
