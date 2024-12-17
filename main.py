from importlib import import_module
from highrise.__main__ import *
import time
import traceback
import psutil

# BOT SETTINGS #
bot_file_name = "musicbot"
bot_class_name = "JellyJell00"
room_id = "6721d10166bbafdb75e8c4a4" 
bot_token = "ef9b5dc9bfb717764e67ab5773e70822e4cf54ccf429b2aecd2a777d3133fd9e"


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
