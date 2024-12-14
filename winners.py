import random
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

def scrape_transaction_hashes():
    """Scrape the latest 50 transaction hashes from the given Snowtrace URL."""
    url = "https://snowtrace.io/token/0x88F89BE3E9b1dc1C5F208696fb9cABfcc684bD5F?chainid=43114"

    # Setup Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(3)  # Wait for the page to load

    # Locate the transaction hash elements
    hash_elements = driver.find_elements(By.CSS_SELECTOR, "span.hash-tag.text-truncate")

    pure_hashes = []
    actions = ActionChains(driver)

    for elem in hash_elements[:50]:  # Limit to 50 hashes
        actions.move_to_element(elem).perform()
        full_hash = elem.get_attribute("data-original-title")
        if full_hash:
            pure_hashes.append(full_hash)

    driver.quit()
    return pure_hashes

def save_hashes_to_csv(hashes, filename="pure_hashes.csv"):
    """Save the list of hashes to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Transaction Hash"])
        for h in hashes:
            writer.writerow([h])

def weighted_random_choice(participants):
    """Weighted random choice function for raffle."""
    total_weight = sum(weight for _, weight in participants)
    pick = random.uniform(0, total_weight)
    current = 0
    for name, weight in participants:
        current += weight
        if current >= pick:
            return name
    return participants[-1][0]  # Fallback

def main():
    # Step 1: Scrape transaction hashes
    print("Scraping the latest 50 transaction hashes...")
    pure_hashes = scrape_transaction_hashes()

    # Step 2: Display the hashes in the terminal
    print("\nLatest 50 Transaction Hashes:")
    for h in pure_hashes:
        print(h)

    # Step 3: Save hashes to a CSV file
    save_hashes_to_csv(pure_hashes)
    print("\nHashes saved to pure_hashes.csv")

    # Step 4: Randomly select a hash from the list
    selected_hash = random.choice(pure_hashes)
    print(f"\nRandomly Selected Hash for Raffle: {selected_hash}")

    # Step 5: Seed the random generator with the selected hash
    seed_int = int(selected_hash, 16)
    random.seed(seed_int)

    # Step 6: Raffle Logic
    raffle_list_1 = [("Alice", 1), ("Bob", 2), ("Charlie", 3)]
    raffle_list_2 = [("David", 5), ("Eve", 1), ("Frank", 2)]
    raffle_list_3 = [("Grace", 10), ("Heidi", 2), ("Ivan", 4)]
    raffle_list_4 = [("Judy", 1), ("Karl", 3), ("Leo", 2)]
    raffle_list_5 = [("Mia", 1), ("Noah", 2), ("Olivia", 3)]

    winner_1 = weighted_random_choice(raffle_list_1)
    winner_2 = weighted_random_choice(raffle_list_2)
    winner_3 = weighted_random_choice(raffle_list_3)
    winner_4 = weighted_random_choice(raffle_list_4)
    winner_5 = weighted_random_choice(raffle_list_5)

    # Step 7: Announce Winners
    print("\nWinners:")
    print(f"1 AVAX Winner: {winner_1}")
    print(f"0.25 AVAX worth of BALLN: {winner_2}")
    print(f"Duality Unveiled NFT Winner: {winner_3}")
    print(f"Red Spotlight Reverie NFT Winner: {winner_4}")
    print(f"Cracked Reverence NFT Winner: {winner_5}")

if __name__ == "__main__":
    main()
