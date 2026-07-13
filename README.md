# Telegram News Aggregator Bot

A Telegram bot built with [Aiogram 3](https://docs.aiogram.dev/en/latest/) that serves news articles from local JSON files. It features an interactive inline keyboard interface, allowing users to browse news categories and read paginated posts with attached images.

## 🚀 Features

*   **Interactive Menus**: Browse available news categories using dynamically generated inline keyboards.
*   **Pagination**: Easily navigate through multiple news posts within a category using "Next" and "Previous" buttons (displays 5 posts per page).
*   **Rich Media**: View news articles directly in Telegram with cover images, titles, full descriptions, and publication dates.
*   **Data-Driven**: Categories and posts are loaded locally from easily updatable JSON files.

## 📝 Project Structure

As seen in the `image_ffe200.png` file, the project follows a clean, modular architecture:

```text
TELEGRAM-NEWS-AGGREGATOR/
├── tg_bot/
│   ├── data/
│   │   ├── categories.json       # JSON containing news categories (e.g., World, Culture, Sport)
│   │   └── posts.json            # JSON containing news articles mapped to specific categories
│   ├── handlers/
│   │   └── user/
│   │       ├── callback.py       # Handles inline keyboard callbacks (pagination, post/category selection)
│   │       └── text.py           # Handles standard text commands (/start, /help)
│   ├── keyboards/
│   │   └── inline.py             # Functions to generate inline keyboards
│   └── utils.py                  # Helper functions (e.g., reading JSON files)
├── .env                          # Environment variables (create this file)
├── .env.example                  # Template for the .env file
├── .gitignore                    # Files and directories ignored by Git
├── main.py                       # Main entry point that initializes and starts the bot
└── requirements.txt              # Project dependencies (aiogram, environs, etc.)
```

## 🛠️ Prerequisites

- Python: Version 3.8+ (Recommended 3.10+)
- Telegram Bot Token: Obtain one by talking to @BotFather on Telegram.

## ⚙️ Installation and Setup

1. **Clone the repository**
   Download or clone the project files to your local machine and navigate into the root directory.
2. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   Create a .env file in the root directory (alongside main.py) and add your bot token:
   ```env
   BOT_TOKEN=your_telegram_bot_token_here
   ```
5. **Prepare the Data**
   Ensure tg_bot/data/categories.json and tg_bot/data/posts.json are properly formatted and populated with your desired news content.

## Usage
Start the bot by running the main.py script:
```bash
python main.py
```
