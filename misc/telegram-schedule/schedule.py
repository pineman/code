import sys
import subprocess
subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "telethon"])

from telethon import TelegramClient
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import argparse
import yaml

def weekday_generator(start_date, count):
    current = start_date
    for _ in range(count):
        if current.weekday() < 5:
            yield current
        current += timedelta(days=1)
        while current.weekday() > 4:
            current += timedelta(days=1)

async def schedule(client, number, message, start_date):
    for date in weekday_generator(start_date, 100):
        await client.send_message(number, message, schedule=date)

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: {date_str}. Use YYYY-MM-DD")

def load_config():
    with open('secrets.yaml', 'r') as file:
        return yaml.safe_load(file)

def main(args):
    config = load_config()
    start_date = args.date.replace(hour=18, minute=30, tzinfo=ZoneInfo("Europe/Lisbon"))
    with TelegramClient('me', config['api_id'], config['api_hash']) as client:
        client.loop.run_until_complete(schedule(client, config['number'], config['message'], start_date))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Schedule Telegram messages at 18:30 lisbon.")
    parser.add_argument('date', type=parse_date, help="Start date in YYYY-MM-DD format")
    args = parser.parse_args()
    main(args)
