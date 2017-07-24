from tkinter import *
from tkinter import ttk
from twitterback import *

class TwitApp:
	def __init__(self, master):
		self.twitter = Twit()
		self.label = ttk.Label(master, text='Hello Twitter')
		self.label.grid(row = 0, column = 0, columnspan = 2)
		
		text = Text(master, width = 40, height = 10, wrap='word').grid(row=1, column=0, columnspan=2)
		
		ttk.Button(master, text = 'Refresh', 
			command = self.get_statuses).grid(row = 2, column = 0)
			
		ttk.Button(master, text = 'Post', 
			command = self.post_status).grid(row = 2, column = 1)
		
		self.resp = ttk.Label(master)
		self.resp.grid(row = 3, column = 0, columnspan = 2)	
		
		self.frame = ttk.Frame(master, height=40, width=500)
		self.frame.grid(row = 4, column = 0, columnspan = 2)
		
	def bundle_tweet(self, user, text, i):
		user = Label(self.frame, text=user).grid(row=i, column=0)
		text = Label(self.frame, text=text).grid(row=i, column=1)
			
	def get_statuses(self):
		for i,item in enumerate(self.twitter.get_statuses(5)):
			#print(i['user']['name'], i['text'])
			self.bundle_tweet(item['user']['name'], item['text'], i)
		
	def post_status(self):
		self.resp.config(text = 'Posted')
		
def main():
	root = Tk()
	app = TwitApp(root)
	root.mainloop()
	
if __name__ == '__main__': main()


