from pymongo import MongoClient

import config

radhedb = MongoClient(config.MONGO_URL)
Radhe = Radhedb["RADHEDb"]["RADHE"]


from .chats import *
from .users import *
