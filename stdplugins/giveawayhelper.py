import asyncio
import datetime
from telethon import events
from uniborg.util import admin_cmd


channel = {-1001191913647: "Trash"}
logs_id = -411442681



message = "test"
error_msg = "Error"


@borg.on(admin_cmd("send ?(.*)"))
async def _(event):
  if event.fwd_from:
    return
  input_str = event.pattern_match.group(1)
  if event.reply_to_msg_id:
    previous_message = await event.get_reply_message()
    message = previous_message.message
  error_count = 0
  for chat_id in channel.keys():
    try:
      await borg.send_message(chat_id, message)
      await borg.send_message(logs_id, f"{message} sent at {channel[chat_id]} ({chat_id}) successfully.")
    except:
      try:
        borg.forward_messages(chat_id, previous_message)
        await borg.send_message(logs_id, f"Message sent at {channel[chat_id]} ({chat_id}) successfully.")
      except Exception as error:
        await borg.send_message(logs_id, "Error! " + str(error))
        error_count+=1
  await borg.send_message(logs_id, f"{error_count} Errors")

#client.send_message(chat_ids, message)
