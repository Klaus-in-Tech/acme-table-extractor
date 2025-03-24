# ACME Web Scraper

This project is a web scraper for the ACME website using Python and Selenium. The scraper logs into the ACME website, navigates to the Work Items page, and scrapes tabular data from multiple pages. The scraped data is then saved to an Excel file.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver
- `pip` (Python package installer)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Klaus-in-Tech/acme-table-extractor.git
    cd acme-table-extractor
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # On Windows
    source .venv/bin/activate  # On macOS/Linux
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set the environment variables for your ACME username and password:
    ```sh
    set ACME_USERNAME=your_username  # On Windows
    set ACME_PASSWORD=your_password  # On Windows
    export ACME_USERNAME=your_username  # On macOS/Linux
    export ACME_PASSWORD=your_password  # On macOS/Linux
    ```

## Usage

1. Run the scraper:
    ```sh
    python acme_scrapper.py
    ```

2. The script will log into the ACME website, navigate to the Work Items page, and scrape the data. The scraped data will be saved to an Excel file named `scraped_data.xlsx`.

## Logging

The script logs its actions and any errors to a log file named `ACME_AUTOMATION_LOG_FILE.log`. The log file includes timestamps, log levels, and messages.
