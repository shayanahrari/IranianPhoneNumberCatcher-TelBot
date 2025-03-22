# Number Catcher Telegram Bot

This project is a Telegram bot that catches Iranian phone numbers from forwarded messages in the bot, saves them in a `.txt` file, and provides other useful functionalities.

## Features

- Automatically extracts Persian/Iranian phone numbers from forwarded messages.
- Saves the extracted phone numbers into a `numbers.txt` file located in the root directory of the project.
- Simple configuration to set the bot's token.
- You can even forward multiple messages in a batch, and the bot will get all the numbers without any errors!
  
## Prerequisites

To run this project, ensure you have the following:

- Python 3.7 or higher installed.
- `pip` (Python package manager).
  
## Installation

1. Clone this repository or download it as a ZIP and extract it.

   ```bash
   git clone https://github.com/shayanahrari/IranianPhoneNumberCatcher-TelBot.git
   ```

   ```bash
   cd IranianPhoneNumberCatcher-TelBot
   ```

2. Install the required dependencies.

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. In the `setting/` directory, you will find a configuration file (e.g., `config.py`).
   
2. Set your Telegram bot token in the `config.py` file:
   
   ```python
   TOKEN = "YOUR_BOT_TOKEN"
   ```

   Replace `"YOUR_BOT_TOKEN"` with your actual Telegram bot token, which you can obtain by creating a bot with [BotFather](https://core.telegram.org/bots#botfather).

## Running the Bot

Once everything is set up, you can start the bot by running the following command:

```bash
python run.py
```

The bot will now be active and ready to catch Persian/Iranian phone numbers from any forwarded messages.

## Saving Phone Numbers

- All the phone numbers detected by the bot will be saved in a `numbers.txt` file located in the root directory of the project.
  
## Requirements

All required Python libraries are listed in the `requirements.txt` file. You can install them with:

```bash
pip install -r requirements.txt
```

## Usage

1. Forward messages containing Iranian phone numbers to your bot.
2. The bot will automatically extract and save them in the `numbers.txt` file.
3. You can check the `numbers.txt` file at any time to retrieve all the captured phone numbers.

## License

This project is open-source and available for anyone to use and modify.
