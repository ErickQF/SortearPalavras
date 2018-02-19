from tkinter import *
from random import randrange


class App(Frame):
	def __init__(self, master):
		super().__init__(master)

		self.pack(expand='yes', fill='both')

		self.fr_left = Frame(self)
		self.fr_box = Frame(self.fr_left)
		self.scroll = Scrollbar(self.fr_box) 		
		self.lt = Listbox(self.fr_box, yscrollcommand=self.scroll.set)
		

		self.add_fr = Frame(self.fr_left)
		self.form = Entry(self.add_fr)
		self.bt_add = Button(self.add_fr, text="add", command=self.add)
		self.form.bind("<Return>", self.add)		

		self.fr_right = Frame(self)
		self.result = Label(self.fr_right, text='')
		self.bt_rand = Button(self.fr_right, text = 'rand', command=self.escolher)		
		
		self.inst_pack()		

	def escolher(self):
		num = randrange(self.lt.size())
		result = self.lt.get(num)
		self.result['text'] = result
		
	def add(self, event=''):
		palavra = self.form.get()
		if palavra not in self.lt.get(0,END):
			self.lt.insert(END, palavra)
		self.form.delete(0,END)
		self.lt.see(END)		

	def inst_pack(self):
		self.fr_left.pack(fill='both', expand='yes', side='left')
		self.fr_box.pack(expand='yes', fill='both')
		self.scroll.pack(side='right', fill='y')
		self.lt.pack(side='left', expand='yes', fill='both')
		self.add_fr.pack()
		self.form.pack(side='left')
		self.bt_add.pack(side='right')
		self.fr_right.pack(side='left', expand='yes', fill='both')
		self.result.pack( expand='yes',fill='both')
		self.bt_rand.pack(fill='x')


if __name__ =="__main__":
	root = Tk()
	root.title("Sorteio de Palavras")
	app = App(root)
	app.mainloop()


