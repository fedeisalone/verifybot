from pyrogram import Client, filters
from .. import app, ALIAS, send
from pyrogram.types import InlineKeyboardMarkup as Menu
from pyrogram.types import InlineKeyboardButton as Button
import json
from pyrogram.types import ChatPermissions

lang = open('config.json', encoding='utf8')
data = json.load(lang)
dictionary = {}

for x in data['config']:
    sett = x

@app.on_message(filters.new_chat_members & filters.group)
def _(c, m):
    user = m.new_chat_members[0]
    kb = Menu(inline_keyboard=[
        [Button(text="Join Channel", url=f"{sett['channel']}")],
        [Button(text="✅ | Joined", callback_data=f"checkjoin")]
    ])
    if str(m.chat.id) == sett['chatid']:
        app.send_message(m.chat.id, f"Welcome {user.mention}, join to {sett['channel']}", reply_markup=kb)
        try:
            app.restrict_chat_member(m.chat.id, user.id, ChatPermissions(can_send_messages=False))
        except:
            app.send_message(m.chat.id, "⚠️ I don't have permissions for mute this user!")
        dictionary[m.message_id] = user.id



@app.on_callback_query()
def _(c, q):
    if q.data == "checkjoin":
        for key, value in dictionary.items():
            messageids = 1
            messageids += int(key)
            if str(messageids) == str(q.message.message_id):
                if str(value) == str(q.from_user.id):
                    for member in app.iter_chat_members(sett['channelid']):
                        if q.from_user.id == member.user.id:
                            del dictionary[messageids]
                            q.message.edit("✅ | Successfully unmuted!")
                            app.restrict_chat_member(q.message.chat.id, q.from_user.id, ChatPermissions(can_send_messages=True))
                            return
                    q.answer("⚠️ You are not in channel!")
                else:
                    q.answer("⚠ | This message is not for you!")


