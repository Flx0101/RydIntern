from telethon import TelegramClient, events, sync
from tqdm import tqdm
import os

# These example values won't work. You must get your own api_id and
# api_hash from `my.telegram.org` , under API Development.
api_id = 1564913
api_hash = 'bc8dd940325bc83bd553a4af77f97e62'
client = TelegramClient('session_name', api_id, api_hash)
client.start()
print(client.get_me().stringify())
channelName=input("Enter channel name from where media is too be downloaded")
with TelegramClient('name', api_id, api_hash) as client:
    messages = client.get_messages(channelName, limit=None) # limit defaults to 1
    for msg in tqdm(messages):
        msg.download_media(file=os.path.join('media', ''))