from pyrogram import Client
import logging
from os import environ
from dotenv import load_dotenv
import multiprocessing


API_ID = int(environ.get('API_ID', '20407293'))
API_HASH = environ.get('API_HASH', 'a87b0b6065257882824b6d566488fb9b')
BOT_TOKEN = environ.get('BOT_TOKEN', '5544784741:AAHKpsuyerZKfdKA97nu7WylZY0eNNJwav4')
LOG_GROUP = int(environ.get('LOG_GROUP', '')) if environ.get('LOG_GROUP') else None
DUMP_GROUP = int(environ.get('DUMP_GROUP', '')) if environ.get('DUMP_GROUP') else None
OWNER_ID = int(environ.get('OWNER_ID', '1019484223'))

logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

Mbot = Client(
    name="instabot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
    workers=64,
    sleep_threshold=22
)

if __name__ == '__main__':
    print("Insta-DL Bot started running...")
    num_workers = 64
    pool = multiprocessing.Pool(processes=num_workers)
    Mbot.run()
    pool.close()
    pool.join()
