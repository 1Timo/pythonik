from tkinter import *
from tkinter import messagebox


class Mainpage:
    def __init__(self):
        Label(root, bg='#679222',
              width=width // 30,
              height=11).place(x=-3.5, y=-8.5)
        self.window = Canvas(root, width=width, height=height, bg='lightgrey')
        self.window.place(x=width / 20 * 4, y=0)
        self.window.create_line(20, 100, 20, height-100)
        Label(root, text='CENOTVORBA',
              font='Roboto {}'.format(button_font + 10),
              bg='#679222', ).place(x=width / 20, y=height / 20 * 1.6)

        self.button = Button(root, text='Ovocie/zelenina',
                             anchor='w',
                             font='Roboto {}'.format(button_font),
                             width=15,
                             bg='#98C151',
                             relief=RAISED,
                             bd=3,
                             activebackground='#98C151',
                             command=lambda: worker.do(categories[0], self.button))
        self.button.place(x=width / 20, y=height / 20 * 4)

        self.button1 = Button(root, text='Pečivo',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[1], self.button1))
        self.button1.place(x=width / 20, y=height / 20 * 6)

        self.button2 = Button(root, text='Mäso',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[2], self.button2))
        self.button2.place(x=width / 20, y=height / 20 * 8)

        self.button3 = Button(root, text='Mliečne výrobky',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[3], self.button3))
        self.button3.place(x=width / 20, y=height / 20 * 10)

        self.button4 = Button(root, text='Nápoje',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[4], self.button4))
        self.button4.place(x=width / 20, y=height / 20 * 12)

        self.button5 = Button(root, text='Sladkosti/Slanosti',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[5], self.button5))
        self.button5.place(x=width / 20, y=height / 20 * 14)

        self.button6 = Button(root, text='Ostatné',
                              font='Roboto {}'.format(button_font),
                              width=15,
                              bg='#98C151',
                              relief=RAISED,
                              bd=3,
                              activebackground='#98C151',
                              command=lambda: worker.do(categories[6], self.button6))
        self.button6.place(x=width / 20, y=height / 20 * 16)

        self.message_button = Button(root, text='Potvrdiť',
                                     font='Roboto {}'.format(button_font // 2),
                                     state=ACTIVE,
                                     width=10,
                                     bg='grey',
                                     relief=RAISED,
                                     bd=3,
                                     activebackground='grey',
                                     command=lambda: message_maker())

        self.search_button = Button(root, text='Vyhladaj Tovar',
                                    font='Roboto {}'.format(button_font),
                                    width=15,
                                    bg='#98C151',
                                    relief=RAISED,
                                    bd=3,
                                    activebackground='#98C151',
                                    command=searching)
        self.search_button.place(x=width / 20, y=height / 20 * 18)

    def create_window(self):
        self.window = Canvas(root, width=width, height=height, bg='lightgrey')
        self.window.place(x=width / 20 * 4.5, y=0)
        self.message_button = Button(root, text='Potvrdiť',
                                     font='Roboto {}'.format(button_font // 2),
                                     state=ACTIVE,
                                     width=10,
                                     bg='grey',
                                     relief=RAISED,
                                     bd=3,
                                     activebackground='grey',
                                     command=lambda: message_maker())


class Bar:
    def __init__(self, starting: tuple):
        self.button = Button(page.window, image=image2, bd=0,
                             command=lambda: worker.restarting()).place(x=width / 20 * 12.6, y=0)
        self.starting = starting
        self.main_frame = Frame(page.window)
        self.main_frame.place(x=width / 20 * 5, y=height / 20 * 5)
        self.canvas = Canvas(self.main_frame, bg='white')
        self.frame = Frame(self.canvas, height=height // 2)
        self.scrollbar = Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.scrollbar.pack(fill=Y, side="right")
        self.canvas.pack()
        Label(page.window, bg='lightgrey', width=width // 35, height=height // 220).place(x=80, y=80)
        Label(page.window, text=category[int(starting[0][0])],
              font='Roboto {}'.format(button_font + 10)).place(x=100, y=80)

        self.frame.bind("<Configure>", lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), width=width // 5 , height=height // 2))
        for shift in range(5, 8):
            shift = shift + 0.3 if shift == 6 else shift + 0.65 if shift == 7 else shift
            Label(page.window,
                  text='Kód tovaru:' if shift == 5 else 'Cena tovaru' if shift == 6.15 else 'Cena zakupenia',
                  relief=RAISED,
                  width=20,
                  font=f'Roboto {label_font}').place(x=width / 20 * shift, y=height / 20 * 5 - 18)

        for index, value in enumerate(self.starting):
            value = value.split(';')
            Goods(value[0], value[1], value[2], index, self.frame)


class Goods:
    def __init__(self, code: str, sell: str, buy: str, row: int, frame: Frame):
        self.frame = frame
        self.code = code
        self.sell = sell
        self.buy = buy
        self.row = row
        self.sell_price = IntVar()
        self.sell_price.set(self.sell)
        self.buy_price = IntVar()
        self.buy_price.set(self.buy)
        self.label = Label(self.frame, text=self.code + ':', relief=RAISED, bd=1, width=15)
        self.label.grid(row=self.row, column=0, columnspan=1)
        self.entry1 = Entry(self.frame, textvariable=self.sell_price, font=f'Roboto {label_font}', width=20)
        self.entry1.grid(row=self.row, column=1, columnspan=1)
        self.entry1 = Entry(self.frame, textvariable=self.buy_price, font=f'Roboto {label_font}', width=20)
        self.entry1.grid(row=self.row, column=2, columnspan=1)


class MakeWork:
    def __init__(self):
        self.previous = previous

    def do(self, starting: int, working: Button) -> None:
        page.message_button['state'] = ACTIVE
        self.previous['bd'], self.previous['bg'], self.previous['activebackground'] = 3, '#98C151', '#98C151'
        working['bg'] = working['activebackground'] = 'darkgreen'
        working['bd'] = 6
        Bar(starting)
        page.message_button.place(x=width // 20 * 15, y=height // 20 * 17)
        self.previous = working

    def restarting(self):
        self.previous['bd'], self.previous['bg'], self.previous['activebackground'] = 3, '#98C151', '#98C151'
        page.window.destroy()
        page.create_window()


def make_categories(codes) -> tuple:
    helping = ()
    starting = 0
    for value in codes:
        if int(value[0]) == starting:
            helping += value,
        else:
            starting += 1
            yield helping
            helping = value,


def message_maker() -> None:
    change = messagebox.askyesno(title='Potvrdenie zmien', icon='warning', message='Prajete si uložiť zmeny?')
    if change:
        for changes in changings:
            changes[0].set(changes[1])
        page.message_button['state'] = DISABLED


def massage_confirm() -> None:
    messagebox.showinfo(message='Zmeny boli ulozene :)')


def find_goods(sell, buy, confirm) -> None:
    confirm['state'] = ACTIVE
    sell.set('0.00')
    buy.set('0.00')


def set_goods(sell, buy, search) -> None:
    buy.set(buy.get())
    sell.set(sell.get())
    search.destroy()
    massage_confirm()


def searching() -> None:
    search = Toplevel(root)
    search.lift()
    search.title('Vyhladávanie tovaru')
    search.geometry('600x100')
    root.eval(f'tk::PlaceWindow {str(search)} center')
    search.bind('<Escape>', lambda event: search.destroy())
    Label(search, text='Kod:', width=width // 175, anchor=CENTER).grid(row=0, column=0)
    Label(search, text='Cena tovaru:', width=width // 175, anchor=W).grid(row=0, column=2)
    Label(search, text='Cena zakupenia:', width=width // 125, anchor=W).grid(row=0, column=3)
    code = Entry(search, width=10)
    code.grid(row=1, column=0)
    x = StringVar()
    y = StringVar()
    x.set('')
    y.set('')
    sell = Entry(search, textvariable=x)
    confirm = Button(search, text='confirm', state=DISABLED, command=lambda: set_goods(x, y, search))
    confirm.place(x=0, y=70)
    submit = Button(search, text='Vyhladaj', command=lambda: find_goods(x, y, confirm), pady=0)
    submit.grid(row=1, column=1)
    sell.grid(row=1, column=2)
    buy = Entry(search, textvariable=y)
    buy.grid(row=1, column=3)


root = Tk()
root.configure(bg='white')
root.attributes('-fullscreen', True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
button_font, label_font = width // 100, width // 200
changings = {}
category = ('Ovocie/zelenina', 'Pečivo', 'Mäso', 'Mliečne výrobky', 'Nápoje', 'Sladkosti/Slanosti', 'Ostatné')
image2 = PhotoImage(file='logo.png')
with open('Cennik.txt') as file:
    file = file.read().rstrip().split('\n')[1:]

categories = tuple(make_categories(sorted(file)))

page = Mainpage()
previous = page.button
worker = MakeWork()

root.bind('<Escape>', lambda event: root.destroy())
if __name__ == '__main__':
    root.mainloop()
