# Telegram-Bot for Collecting Student Data

## Description

This Telegram bot is designed to collect student information, including their name, age, and class, and store this data in the `school_data.db` database.

## Project Structure

```
project/
│
├── bot/
│   ├── __init__.py       # Package initialization
│   ├── main.py           # Main file to run the bot
│   ├── handlers.py       # Command and message handlers
│   ├── database.py       # Database operations
│
├── .env                  # Environment variables file (bot token)
├── requirements.txt      # Project dependencies list
└── README.md             # Setup and usage instructions
```

## Installation and Launch

### 1. Create a Virtual Environment

Set up a virtual environment to isolate project dependencies:


python -m venv venv


Activate the virtual environment:

- On Linux/MacOS:

  source venv/bin/activate


- On Windows:

 
  venv\Scripts\activate


### 2. Install Dependencies

Ensure you are in the project directory, then install all necessary dependencies:


pip install -r requirements.txt


### 3. Configure Environment Variables

Create a `.env` file in the root of the project and add your bot token:


BOT_TOKEN=your_telegram_bot_token


### 4. Run the Bot

Start the Telegram bot with the following command:


python bot/main.py


## Usage

- After launching the bot, send the `/start` command in Telegram.
- The bot will prompt you for your name, age, and class.
- Once you provide the information, the bot will save it to the `school_data.db` database.

## Requirements

- Python 3.10 or higher
- SQLite (built-in with Python)

## Notes

- In case of errors, ensure that the `.env` file contains the correct bot token.
- If you encounter issues with dependencies, verify that all packages from `requirements.txt` are installed.

## License

This project is licensed under the MIT License.

