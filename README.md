# python-homework
Python homework assignments and exercises from my course.

## 🗄️ Project: Multi-API ETL Pipeline to PostgreSQL
**[View Code](./postgres-weather-api_22/)** An automated ETL (Extract, Transform, Load) pipeline that fetches mock and real-world dynamic data from multiple endpoints (JSONPlaceholder, DummyJSON, OpenWeather API) and streams it directly into a local PostgreSQL database. 

It also includes an interactive CLI loop where users can request real-time weather logs for any city, display them, and append them directly to the DB records.

### 🚀 Key Features
* **Advanced DB Optimization:** Uses `psycopg3`'s streaming capabilities (`cursor.copy()`) to batch-load large datasets instantly via the `COPY FROM STDIN` method instead of executing repetitive `INSERT` commands.
* **Multi-Source Data Integration:** Handles complex JSON structures from 3 distinct REST APIs simultaneously, normalizing conflicting keys to map them into tabular PostgreSQL schemas.
* **Dynamic Interactive Storage:** Features an active runtime CLI loop connected to the OpenWeather API that fetches weather states dynamically and flushes user-requested logs to transactional history records.
* **Production-Ready Configurations:** Completely decouples credential logic from source files using `.env` handling via `python-dotenv` for encrypted database configurations and API tokens.

### 🛠️ Tech Stack
* **Python 3**
* **PostgreSQL** (Relational Database)
* **Psycopg 3** (The modern PostgreSQL adapter for Python)
* **Requests** (REST API integrations)
* **Python-dotenv** (Environment variable management)

## 📰 Project: News Parser (Gazeta.ru)
**[View Code](./parsing-news_25/)** A lightweight web scraper built to fetch the latest news articles from the "Gazeta.ru" news feed. It extracts headlines, source URLs, and the full text of articles, then structured and saves the data into a clean JSON file.

### 🚀 Key Features
* **Anti-Bot Bypass:** Implements custom headers and live browser session tokens (`Cookies`) to successfully bypass advanced anti-scraping and bot-detection walls.
* **Content Extraction:** Parses raw HTML to accurately isolate article paragraphs, stripping away ads, sidebars, and trackers.
* **Polite Scraping:** Includes built-in request throttling (`time.sleep`) to comply with basic web scraping ethics and prevent server overloading.

### 🛠️ Tech Stack
* **Python 3**
* **Requests** (Synchronous HTTP requests)
* **BeautifulSoup4** (HTML parsing and DOM traversal)

## 🛒 Project: OOP Market Scraper (Texnomart) to PostgreSQL
**[View Code](./parsing_market_26/)** A robust Python web scraping application designed to extract household appliance data from Texnomart and manage transactional batch insertions into a relational PostgreSQL database.

### 📝 Description
An advanced, modular web scraper designed with Object-Oriented Programming (OOP) principles. The script extracts electrical appliance data (Vacuum Cleaners) from the "Texnomart" online store, structures it, and saves the results into both a local `market.json` file and a relational **PostgreSQL** database. 

The project strictly follows the **Single Responsibility Principle (SRP)** by separating configurations, network connectivity, HTML parsing, and database logic into isolated, maintainable components.

### 🚀 Key Features
* **Modular OOP Architecture:** Divided into clear responsibilities (`PageDownloader`, `MarketParser`, `Database`, `BotApp`).
* **Robust Data Extraction:** Secure HTML nodes parsing with fallback values to prevent `NoneType` attribute errors.
* **Efficient Pipeline Mode:** Utilizes `psycopg3`'s optimized `executemany` for batch inserting data into PostgreSQL.
* **Data Deduplication:** Implements PostgreSQL `ON CONFLICT (link) DO NOTHING` alongside strict unique constraints to prevent duplicate entries.
* **Secure Environment Configuration:** Sensitive database credentials and host parameters are fully encrypted/hidden using `.env` files and `python-dotenv`.

### 🛠️ Tech Stack
* **Python 3**
* **PostgreSQL** (Relational Database)
* **Psycopg 3** (Modern PostgreSQL adapter for Python)
* **BeautifulSoup 4** (HTML Parsing)
* **Requests** (HTTP Client Manager & Session control)
* **Python-dotenv** (Environment variable manager)

### 📂 Architecture & File Structure
* `config.py` — Manages constant values, request headers, and dynamically extracts database credentials from environment variables.
* `downloader.py` — Contains `PageDownloader` class using persistent `requests.Session` for efficient web requests.
* `parser.py` — Contains `MarketParser` class containing business logic for parsing rows, scrubbing texts, and resolving absolute path links.
* `database.py` — Contains `Database` class responsible for automated schema migrations (`CREATE TABLE IF NOT EXISTS`) and transactional batch insertion management.
* `main.py` — The core engine (`BotApp`) that orchestrates the ETL pipeline execution.
* `.env` — Secure workspace configurations *(hidden via global .gitignore)*.

### ⚙️ How To Run
1. Ensure you have your PostgreSQL server running and create a database named `parsing_market_with_db` (or update your `.env`).
2. Populate the `.env` file in the project folder:
   ```text
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=parsing_market_with_db
   DB_USER=your_username
   DB_PASSWORD=your_password
   ```
3. Run the application execution entrypoint:
   ```bash
   python main.py
   ```

## 🕙 Project: Ordinal Date Calculator

**[View Code](./ordinal-date-calculator/)** A lightweight Python script that calculates the **ordinal date** (the day number of the year, from 1 to 366) for any given Gregorian calendar date.

### 📝 Description

An ordinal date consists of a year and a day number representing the elapsed days within that year. This format is highly efficient for computing elapsed intervals, such as tracking 90-day return policies, expiration dates, or project milestones, without dealing with complex calendar month logic.

The program handles leap years strictly according to the rules of the Gregorian calendar:
- A year is a leap year if it is divisible by 4.
- However, if it is divisible by 100, it is **not** a leap year, **unless** it is also divisible by 400.

### 🚀 Key Features

- **Leap Year Awareness:** Accurately adjusts February to 29 days when necessary.
- **Modular Design:** The core calculation logic is isolated within the `ordinalDate` function, making it easy to reuse.
- **Execution Safeguard:** Uses the `if __name__ == "__main__":` idiom to ensure the interactive CLI runs only when executed directly, preventing unexpected behavior if imported as a module.
- **Robustness:** Includes basic error handling for invalid integer inputs.

### ⚙️ How To Run

1. Navigate to this project folder in your terminal:
   ```bash
   cd <имя-вашего-общего-репозитория>/ordinal-date-calculator
   ```
2. Run the application execution entrypoint:
   ```bash
   python main.py
   ```
