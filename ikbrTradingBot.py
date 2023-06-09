#Imports
import ibapi
from ibapi.client import EClient
from ibapi.wrapper import EWrapper

#Vars

#Class for IB connection
class IBApi(EWrapper,EClient):
    def __init__(self):
        EClient.__init__(self, self)

#Bot logic
class Bot:
    ib = None
    def __init__(self):
        #Connection to IB on init
        ib = IBApi()
        ib.connect("127.0.0.1", 7497,1)
        ib.run()

#Start Bot
bot = Bot()

