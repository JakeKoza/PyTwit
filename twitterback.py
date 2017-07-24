from twitter import *

class Twit:
	def __init__(self):
		self._Token = '756467029436137472-X2HM5DNVfhhxP5kiw5O0RfVSwFpe33x'
		self._TokenKey = 'J8vWKp94HGoWlLqiLmqdw0zNHh72QHzBw9Zb5rBDx1slW'
		self._ConSec = 'sQkugjT7pVuoo8zbhVZOzLu4X'
		self._ConSecKey = 'pK49l5JoHBULXHNDwgWJ2fCziPLqUSCflz2ncKGio77S9H8suZ'
		self.t = Twitter(auth=OAuth(self._Token, self._TokenKey, self._ConSec, self._ConSecKey))
 
	def get_statuses(self, count):
		return self.t.statuses.home_timeline(count=count)
	
def main():
	t = Twit()
	t.get_statuses(5)
	
if __name__ == '__main__': main()
