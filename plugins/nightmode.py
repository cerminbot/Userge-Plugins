from userge import userge, Config, Message
# Copyright (C) 2020-2021 by DevsExpo@Github, < https://github.com/DevsExpo >.
#
# This file is part of < https://github.com/DevsExpo/FridayUserBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/DevsExpo/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import ChatPermissions
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import logging
import requests
import json

@userge.on_cmd("night_mode", about={
    'header': "Activate Nightmode In Group",
    'usage': "Ga ada",
    'examples': [
        "-"]},
    allow_private=False)

async def job_close():
  try:
    await userge.send_message(
      -1001168126523, "**🌃 Mode Malam Aktif**\n\n`Sekarang jam 22:00, Grup ditutup dan akan dibuka esok hari secara otomatis. Selamat beristirahat semuanya!!` \n**Powered By Pyrogram**"
    )
    await userge.set_chat_permissions(
      -1001168126523,
      ChatPermissions(
        can_send_messages=False,
        can_invite_users=True,
      )
    )
    
    except Exception as e:
      try:
        await userge.send_message(-1001168126523, f"[NIGHT MODE]\n\nFailed To Close The Group {ido}.\nError : {e}")
        except:
          pass


scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_close, trigger="cron", hour=13, minute=30)
scheduler.start()

async def job_open():
  req = requests.get('http://fadhil-s.herokuapp.com/api/random_quotes.php?apikey=dwh20ud9u0q2ijsd092099139jp')
  json = req.json()
  quote = json["data"]["quotes"]
  author = json["data"]["by"]
  try:
    await userge.send_message(
      -1001168126523, "`Sekarang sudah jam 6 pagi. Selamat pagi, grup kini telah dibuka semoga hari-harimu menyenangkan.`\n\n**Quotes Today:**\n"+quote+"\n~ "+author+"\n**Powered By Pyrogram**"
    )
    await userge.set_chat_permissions(
      -1001168126523,
      ChatPermissions(
        can_send_messages=True,
        can_send_media_messages=True,
        can_send_stickers=False,
        can_send_animations=True,
        can_invite_users=True,
        can_add_web_page_previews=True,
        can_use_inline_bots=True
      )
    )
            
      except Exception as e:
        ido = -1001168126523
        try:
          await userge.send_message(-1001168126523, f"[NIGHT MODE]\n\nFailed To Open The Group {ido}.\nError : {e}")
          except:
            pass
            

scheduler = AsyncIOScheduler(timezone="Asia/Jakarta")
scheduler.add_job(job_open, trigger="cron", hour=13, minute=45)
scheduler.start()
