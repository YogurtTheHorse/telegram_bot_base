from mongo_help import MongoHelper
import logging
import telegram
import vk_api

from commands import commands

telegram_bot = telegram.Bot(token='135242172:AAFT9NNNApAgHPjEBrGh3BucWKScJZSt8QY')
#vk_handler = vk_bot()
mongo = MongoHelper()

print ("Bot info: ", telegram_bot.getMe())

last_update = mongo['global']['last'] or 0
print('Last message id:', last_update)

def telegram_update(updates):
	for u in [ u for u in updates if u.message.text.startswith('/') ]:
		command(u)

def command(update):
	text = update.message.text
	command_name = text.split(' ')[0][1:].lower()

	commands_apply = [ c for c in commands if command_name in c.get_names() ]
	for c in commands_apply:
		c.call(None, telegram_bot, mongo, text.split(' ')[1:])

while True:
	updates = telegram_bot.getUpdates(offset=last_update)

	if len(updates):
		telegram_update(updates)

		last_update = updates[-1].update_id + 1
		mongo['global']['last'] = last_update