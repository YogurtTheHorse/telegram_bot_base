import pymongo

class MongoHelper(object):
	instance = None

	def __new__(cls):
		if cls.instance is None:
			cls.instance = super(MongoHelper, cls).__new__(cls)

		return cls.instance

	def __init__(self):
		super(MongoHelper, self).__init__()
		self.db_name = 'telegram_vk'

		#mongo_uri = os.environ['OPENSHIFT_MONGODB_DB_URL'] if 'OPENSHIFT_MONGODB_DB_URL' in os.environ else "mongodb://localhost:27017/"
		self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
		self.db = self.mongo_client[self.db_name]

		print("Mongo database: ", self.db)

	def __getitem__(self, name):
		return CollectionHelper(self.db[name])
		 	

class CollectionHelper(object):
	def __init__(self, collection):
		self.collection = collection

	def __getitem__(self, key):
		return self.collection.find_one({'id': key})['value']

	def __setitem__(self, key, value):
		self.collection.update_one({'id': key}, {"$set": {'id': key, 'value': value}}, True)

	def set_special(self, value, **kwargs):
		args = kwargs.copy()
		args['value'] = value
		self.collection.update_one(kwargs, {"$set": args}, True)

	def get_special(self, **kwargs):
		return self.collection.find_one(kwargs)['value']
		