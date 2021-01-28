from pyrogram import Client, filters
from .. import app, ALIAS, send

@app.on_message(filters.command("start", ALIAS))
def _(c, m):
    send(m.chat.id, f"Ciao! Questo bot è stato programmato da @fedeisalone!")