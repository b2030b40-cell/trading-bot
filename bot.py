from telethon import TelegramClient, events

api_id = "37250760"
api_hash = "f7c9d2a7ba2e52402b921b4009245fc9"

SOURCE_CHANNEL = -1003815119163
TARGET_CHANNEL = -1003587377352

client = TelegramClient('my_session', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHANNEL))
async def my_event_handler(event):
    try:
        await client.send_message(TARGET_CHANNEL, event.message)
        print("تم تحويل الإشارة بنجاح!")
    except Exception as e:
        print(f"حدث خطأ: {e}")

print("المراقب يعمل الآن في الخلفية...")
client.start()
client.run_until_disconnected()