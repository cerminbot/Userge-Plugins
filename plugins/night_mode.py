# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from userge import userge, Config, Message
from pyrogram.types import ChatPermissions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
import requests
import json
import pytz
from datetime import datetime

@userge.on_cmd("nightmode_on", about={
    'header': "Activate Nightmode In Group",
    'usage': "Ga ada",
    'examples': ["-"]},allow_private=False)
async def job_close():
    now = datetime.now(pytz.timezone('Asia/Jakarta'))
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    tgl = now.strftime('%d/%m/%Y')
    jam = now.strftime('%H:%M:%S')
    await userge.send_message(
      -1001128045651, "📆 Tanggal : "+days[now.weekday()]+", "+tgl+"\n⏰ Jam : "+jam+"\n\n**🌗 Mode Malam Aktif**\n`Proses LockDown dimulai, Grup ditutup dan semua member tidak akan bisa mengirim pesan. Selamat beristirahat dan bermimpi indah !!`"
    )
    await userge.set_chat_permissions(-1001128045651, ChatPermissions(can_send_messages=False, can_invite_users=True)
    )
    
scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_close, trigger="cron", hour=22, minute=0)
scheduler.start()

@userge.on_cmd("nightmode_off", about={
    'header': "Off Nightmode In Group",
    'usage': "Ga ada",
    'examples': ["-"]},allow_private=False)
async def job_open():
    now = datetime.now(pytz.timezone('Asia/Jakarta'))
    days = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    tgl = now.strftime('%d/%m/%Y')
    jam = now.strftime('%H:%M:%S')
    req = requests.get('http://fadhil-s.herokuapp.com/api/random_quotes.php?apikey=dwh20ud9u0q2ijsd092099139jp')
    json = req.json()
    quote = json["data"]["quotes"]
    author = json["data"]["by"]
    await userge.send_message(
        -1001128045651, "📆 Tanggal : `"+days[now.weekday()]+", "+tgl+"`\n⏰ Jam : `"+jam+"`\n\n🌗 Mode Malam Selesai\nSelamat pagi, grup kini telah dibuka semoga hari-harimu menyenangkan.\n\n**Quotes Today:**\n`"+quote+"\n~ "+author+"`"
    )
    await userge.set_chat_permissions(-1001128045651, ChatPermissions(can_send_messages=True, can_send_media_messages=True, can_send_stickers=False, can_send_animations=True, can_invite_users=True, can_add_web_page_previews=True, can_use_inline_bots=True)
    )
    
scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_open, trigger="cron", hour=6, minute=0)
scheduler.start()
