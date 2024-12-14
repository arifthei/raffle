# raffle
Python script for blockchain transaction hash based provable fairness
# Raffle Script with Provable Fairness

This repository contains a Python script for conducting a raffle with provable fairness, leveraging transaction hashes from the Avalanche blockchain. The script gathers the latest 50 transaction hashes for the `$FLD` token, selects one hash as the random seed, and uses it to determine winners in a weighted raffle system. The results are fully reproducible and transparent.

---

## Features

- **Blockchain-Based Randomness**: Scrapes the latest 50 transaction hashes for `$FLD` from Snowtrace.
- **Weighted Raffle**: Participants have assigned weights that influence their chances of winning.
- **Transparent Process**: Publishes transaction hashes, the selected hash, and raffle results for public verification.
- **Reproducible**: Anyone can run the script with the same hash and participant data to verify the results.

---

## Dependencies

To run the script, ensure the following dependencies are installed:

1. **Python (>= 3.7)**
2. **pip**

Install the required Python packages using the command:
```bash
pip install selenium
```

### Additional Requirements

- **Google Chrome**: Ensure you have Google Chrome installed on your system.
- **ChromeDriver**: Match the ChromeDriver version with your installed Chrome browser. Download it from [here](https://chromedriver.chromium.org/downloads).
- **Selenium**: For browser automation and scraping transaction hashes.

---

## Script Workflow

1. **Scraping Transaction Hashes**:
   - The script navigates to the Snowtrace page for `$FLD` and extracts the latest 50 transaction hashes in their pure form.
   - These hashes are displayed in the terminal and saved to a CSV file (`pure_hashes.csv`).

2. **Random Hash Selection**:
   - One hash is randomly selected from the list of 50 to serve as the seed for the raffle.
   - The selected hash is published for transparency.

3. **Raffle Execution**:
   - Uses the selected hash to seed Python's random generator.
   - Conducts a weighted raffle for 5 prizes:
     - **1 AVAX Winner**
     - **0.25 AVAX worth of BALLN**
     - **Duality Unveiled NFT Winner**
     - **Red Spotlight Reverie NFT Winner**
     - **Cracked Reverence NFT Winner**

4. **Announcing Winners**:
   - Winners are displayed in the terminal, and the process is transparent for participants.

---

## How to Run the Script

### 1. Clone the Repository
```bash
git clone https://github.com/arifthei/raffle-script.git
cd raffle-script
```

### 2. Ensure Dependencies Are Installed
Install Selenium and other dependencies as mentioned above.

### 3. Run the Script
Run the raffle script after ensuring your browser session is active (if required by your setup):
```bash
python raffle_script.py
```

### 4. Follow the Steps
- The script will scrape the transaction hashes, select one randomly, and conduct the raffle.
- All steps are displayed in the terminal for transparency.

---

## Notes

1. **Browser Configuration**:
   - If you’re using a custom Chrome profile for Selenium (e.g., to maintain login sessions), modify the script to include your profile path.

2. **Reproducibility**:
   - To reproduce the results, use the same list of transaction hashes and the selected hash.

3. **Error Handling**:
   - If scraping fails (e.g., due to CAPTCHA), ensure your browser session is configured correctly.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Support
For questions or issues, please open an issue on the GitHub repository.

