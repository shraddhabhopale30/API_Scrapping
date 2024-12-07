# API Scraping Project

## Setup

1. **Install Python 3.x**:
   - Download and install Python from https://www.python.org/downloads/.

2. **Install Dependencies**:
   - Install the required libraries using `pip`:
     ```bash
     pip install requests beautifulsoup4 selenium
     ```

3. **Download WebDriver** (for Selenium):
   - Download ChromeDriver from https://sites.google.com/a/chromium.org/chromedriver/downloads.

## Running the Scripts

### DIN and PAN Verification
- Run the script:
  ```bash
  python scripts/din_pan_verification.py
The output will be saved in outputs/din_details.json.

### Director Company Details
- Run the script:
  ```bash
  python scripts/director_companies.py
The output will be saved in outputs/director_companies.json.

### Company Details by CIN
- Run the script:
  ```bash
  python scripts/company_details.py
The output will be saved in outputs/company_details.json.


