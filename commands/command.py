class Command(object):
	def __init__(self):
		super(Command, self).__init__()

	def get_names(self):
		return [ ]

	def telegram_update(self, vk_bot, telegram_bot, mongo, update):
		pass

	def call(self, vk_bot, telegram_bot, mongo, args):
		pass
