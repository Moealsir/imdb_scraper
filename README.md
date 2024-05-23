# IMDb Scraper
![Extracted Data](./src/extracted_data.png)
This project is aimed at scraping the IMDb Top 250 movies list, extracting various details about each movie, and exporting the data into different formats such as JSON, Excel, XML, CSV, and SQLite database.

## Contents


- [IMDb Scraper](#imdb-scraper)
  - [Contents](#contents)
  - [Overview](#overview)
  - [Dependencies](#dependencies)
    - [! SCRIPT IS NOT FREE](#-script-is-not-free)


## Overview

This project is aimed at scraping the IMDb Top 250 movies list, extracting various details about each movie, and exporting the data into different formats such as JSON, Excel, XML, CSV, and SQLite database.

The IMDb scraper is implemented in Python and utilizes the following libraries:
- `selenium` for web scraping
- `BeautifulSoup` for HTML parsing
- `pandas` for data manipulation and exporting to Excel
- `xml.etree.ElementTree` for exporting data to XML
- `sqlite3` for SQLite database operations

The scraper extracts details such as movie title, year, length, image URL, rating, votes, URL, story, genres, directors, writers, stars, popularity, etc., for each movie in the IMDb Top 250 list.

## Dependencies

Before running the IMDb scraper, ensure you have the required dependencies installed. You can install them using pip with the provided `requirements.txt` file.

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install dependencies using the following command:
   ```bash
   pip install -r requirements.txt

## Usage

To use the IMDb scraper:

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the scraper using the following command:
   ```bash
   python scraper.py
The scraper will extract data from the IMDb Top 250 list, process it, and export it to JSON, Excel, XML, CSV, and SQLite database formats in the output_data folder.

## Automating the Scraper

The scraper can be automated to run daily at a specified time using the `schedule` library. The `automate.py` script schedules the scraper to run every day at 6:30 AM. Adjust the schedule timing in the script if needed.

To run the automation script:
   ```bash
   python scraper.py
```
<br>
<br>

### ! SCRIPT IS NOT FREE