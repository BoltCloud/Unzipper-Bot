# Copyright (c) 2022 Itz-fork
# Don't kang this else your dad is gae

import math
import time

from pyrogram import enums
from functools import partial
from aiohttp import ClientSession
from asyncio import get_running_loop
from aiofiles import open as openfile
from unzipper import unzipperbot as client
from config import Config


# Credits: SpEcHiDe's AnyDL-Bot for Progress bar + Time formatter
async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "[{0}{1}] \n**Process**: {2}%\n".format(
            ''.join(["█" for i in range(math.floor(percentage / 5))]),
            ''.join(["░" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "{0} of {1}\n**Speed:** {2}/s\n**ETA:** {3}\n".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(text="{}\n {} \n\n**Join @Modzilla For Premium Applications**".format(ud_type, tmp))
        except:
            pass


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

# Function to download files from direct link using aiohttp
async def download(url, path, udt, message):
    async with ClientSession() as session:
        async with session.get(url, timeout=None) as resp:
            total = resp.headers["Content-Length"]
            curr = 0
            st = time.time()
            async with openfile(path, mode="wb") as file:
                async for chunk in resp.content.iter_chunked(Config.CHUNK_SIZE):
                    await file.write(chunk)
                    if total:
                        curr += len(chunk)
                        await progress_for_pyrogram(curr, total, udt, message, st)


# Execute blocking functions asynchronously
async def run_cmds_on_cr(func, **kwargs):
    loop = get_running_loop()
    return await loop.run_in_executor(
        None,
        partial(func, kwargs)
    )


# Checking log channel
def check_logs():
    try:
        if Config.LOGS_CHANNEL:
            c_info = client.get_chat(chat_id=Config.LOGS_CHANNEL)
            if c_info.type != enums.ChatType.CHANNEL:
                return print("TF? Chat is not a channel")
            elif c_info.username is not None:
                return print("TF? Chat is not private")
            else:
                client.send_message(
                    chat_id=Config.LOGS_CHANNEL, text="`Unzipper-Bot has Successfully Started!` \n\n**Powered by @Modzilla**")
        else:
            print("No Log Channel ID is Given! Imma leaving Now!")
            exit()
    except:
        print("Error Happend while checking Log Channel! Make sure you're not dumb enough to provide a wrong Log Channel ID!")
