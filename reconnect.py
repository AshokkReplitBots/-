from importlib import import_module
from highrise.__main__ import *
import time
import traceback
import psutil

# BOT SETTINGS #
bot_file_name = "musicbot"
bot_class_name = "xenoichi"
room_id = "67391339026fa6a14c90bd2b"
#65c56b54ac42f2f98821e501
bot_token = "7d9dcd06eb955320598b95e5b3aa76db8a8b2db19e31c295225c2b6062b7c110"

def terminate_ffmpeg_processes():
    for proc in psutil.process_iter(['pid', 'name']):
        if 'ffmpeg' in proc.info['name']:
            try:
                proc.terminate()
                print(f"Terminated FFmpeg process: {proc.info['pid']}")
            except Exception as e:
                print(f"Failed to terminate process {proc.info['pid']}: {e}")

my_bot = BotDefinition(getattr(import_module(bot_file_name), bot_class_name)(), room_id, bot_token)

while True:
    try:
        # Cleanup lingering FFmpeg processes before restarting
        terminate_ffmpeg_processes()

        definitions = [my_bot]
        arun(main(definitions))
    except Exception as e:
        print(f"An exception occurred: {e}")
        traceback.print_exc()
        
        # Delay before reconnect attempt
        time.sleep(5)
