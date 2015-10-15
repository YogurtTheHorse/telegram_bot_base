from commands.command import Start

class Start(Command):
	def __init__(self):
		super(Start, self).__init__()

	def get_names(self):
		return [ 'start'.lower() ]

	def telegram_update(self, vk_bot, telegram_bot, mongo, update):
		pass

	def call(self, vk_bot, telegram_bot, mongo, args):
		pass
