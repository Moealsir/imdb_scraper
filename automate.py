import schedule
import time
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_scraper():
    logging.info("Running scraper.py...")
    subprocess.run(["python", "scraper.py"])  # Replace "python" with the appropriate command if needed

# Schedule the scraper to run every day at 6:30 AM
schedule.every().day.at("06:30").do(run_scraper)

# Main loop to keep the program running
while True:
    schedule.run_pending()
    time.sleep(60)  # Sleep for 1 minute to avoid high CPU usage
