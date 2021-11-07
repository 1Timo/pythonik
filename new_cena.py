from tkinter import *
from tkinter import messagebox
from time import strftime, localtime, sleep
import threading


class Mainpage:
    def __init__(self):
        self.window = Canvas(root, width=width, height=height, bg='lightgrey')
        self.window.place(x=width / 5 - 5, y=0)
        self.window.create_line(width/100, 100, width/100, height-100)
        self.window.create_line(width/100, height - 100, width / 1.35, height - 100)
        self.button_logo = Button(self.window, image=image2, bd=0, bg='lightgrey', activebackground='lightgrey',
                                  command=lambda: worker.restarting())
        self.button_logo.place(x=width / 4.5, y=height / 3.5)
        Label(root, bg='#98C151', height=height, width=width//40-1).pack(side=LEFT)
        Label(root, text='CENOTVORBA',
              font='Roboto {}'.format(main_font + width//200),
              bg='#98C151', ).place(x=width / 35, y=height / 20 * 1.6)

        def time_bar() -> None:
            mini_canvas = Canvas(self.window, width=width // 8, height=height // 50, bg='lightgrey')
            mini_canvas.place(x=width / 1.75, y=height / 1.1)
            while True:
                time = mini_canvas.create_text(5, 0, anchor=NW,
                                               text=strftime('%A %d.%b %Y %H:%M:%S', localtime()),
                                               font=f'Roboto {mini_font}')
                mini_canvas.update()
                sleep(1)
                mini_canvas.delete(time)

        self.button = Button(root, text='Ovocie',
                             font='Roboto {}'.format(main_font),
                             highlightthickness=False,
                             width=22,
                             fg='white',
                             bg='#98C151',
                             anchor=W,
                             activeforeground='white',
                             relief=FLAT,
                             height=2,
                             activebackground='#679222',
                             command=lambda: worker.do(categories[0], self.button))
        self.button.place(x=0, y=height / 20 * 3.5)

        self.button1 = Button(root, text='Zelenina',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              fg='white',
                              activeforeground='white',
                              relief=FLAT,
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[1], self.button1))
        self.button1.place(x=0, y=height / 20 * 5.25)

        self.button2 = Button(root, text='Pečivo',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[2], self.button2))
        self.button2.place(x=0, y=height / 20 * 7)

        self.button3 = Button(root, text='Mäso',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              activeforeground='white',
                              relief=FLAT,
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[3], self.button3))
        self.button3.place(x=0, y=height / 20 * 8.75)

        self.button4 = Button(root, text='Mliečne výrobky',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[4], self.button4))
        self.button4.place(x=0, y=height / 20 * 10.5)

        self.button5 = Button(root, text='Nápoje',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[5], self.button5))
        self.button5.place(x=0, y=height / 20 * 12.25)

        self.button6 = Button(root, text='Sladkosti/Slanosti',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              fg='white',
                              activeforeground='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[6], self.button6))
        self.button6.place(x=0, y=height / 20 * 14)

        self.button7 = Button(root, text='Ostatné',
                              font='Roboto {}'.format(main_font),
                              width=22,
                              highlightthickness=False,
                              bg='#98C151',
                              activeforeground='white',
                              relief=FLAT,
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[7], self.button7))
        self.button7.place(x=0, y=height / 20 * 15.75)

        self.search_button = Button(root, text='Vyhladaj Tovar',
                                    font='Roboto {}'.format(main_font),
                                    width=22,
                                    highlightthickness=False,
                                    bg='#98C151',
                                    anchor=W,
                                    fg='white',
                                    activeforeground='white',
                                    relief=FLAT,
                                    height=2,
                                    activebackground='#679222',
                                    command=searching)
        self.search_button.place(x=0, y=height / 20 * 17.5)

        self.message_button = Button(root, text='Potvrdiť',
                                     font='Roboto {}'.format(main_font // 2),
                                     state=ACTIVE,
                                     width=10,
                                     bg='grey',
                                     activeforeground='white',
                                     fg='white',
                                     relief=RAISED,
                                     bd=3,
                                     activebackground='grey',
                                     command=lambda: message_maker())

        time_making = threading.Thread(target=time_bar, daemon=True)
        time_making.start()


class Bar:
    def __init__(self, starting: tuple = (), active: bool = False):
        self.main_frame = Frame(page.window)
        self.canvas = Canvas(self.main_frame, bg='white')
        self.frame = Frame(self.canvas, height=height // 2)
        self.scrollbar = Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        if not active:
            return
        page.button_logo.place(x=width / 20 * 11.5, y=0)
        Label(page.window, bg='lightgrey', width=width // 35, height=height // 220).place(x=80, y=80)
        Label(page.window, text=category[int(starting[0][0])],
              font='Roboto {}'.format(main_font + 10)).place(x=100, y=80)
        page.window.update()
        page.message_button.place(x=width // 20 * 15, y=height // 20 * 17)
        self.main_frame.place(x=width / 20 * 5, y=height / 20 * 5)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.scrollbar.pack(fill=Y, side="right")
        self.canvas.pack()
        self.frame.bind("<Configure>", lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), width=mini_font * 55, height=height // 2))
        for shift in range(5, 9):
            shift = shift + 0.3 if shift == 6 else shift + 0.6 if shift == 7 else shift + 0.9 if shift == 8 else shift
            Label(page.window,
                  text='Kód tovaru:' if shift == 5 else 'Názov tovaru' if shift == 6.3 else'Cena tovaru'
                  if shift == 7.6 else 'Cena zakupenia',
                  relief=RAISED,
                  width=15,
                  font=f'Roboto {mini_font}').place(x=width / 20 * shift, y=height / 20 * 5 - 18)
        for index, value in enumerate(starting):
            value = value.split(';')
            Goods(value[0], value[1], value[2], value[3], index, self.frame)


class Goods:
    def __init__(self, code: str, name: str, sell: str, buy: str, row: int, frame: Frame):
        self.name = name
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
        self.label2 = Label(self.frame, anchor=W, text=self.name, relief=RAISED, bd=1, width=15)
        self.label2.grid(row=self.row, column=1, columnspan=1)
        self.entry1 = Entry(self.frame, textvariable=self.sell_price, font=f'Roboto {mini_font}', width=15)
        self.entry1.grid(row=self.row, column=2, columnspan=1)
        self.entry1 = Entry(self.frame, textvariable=self.buy_price, font=f'Roboto {mini_font}', width=15)
        self.entry1.grid(row=self.row, column=3, columnspan=1)


class MakeWork:
    def __init__(self):
        self.previous = previous
        self.bar_prev = bar_prev

    def do(self, starting: int, working: Button) -> None:
        page.message_button['state'] = ACTIVE
        self.previous['bg'], self.previous['activebackground'] = '#98C151', '#98C151'
        working['bg'] = working['activebackground'] = '#679222'
        self.bar_prev.main_frame.destroy(), self.bar_prev.scrollbar.pack_forget()
        self.bar_prev = Bar(starting, True)
        self.previous = working

    def restarting(self):
        self.previous['bd'], self.previous['bg'], self.previous['activebackground'] = 3, '#98C151', '#98C151'
        page.message_button.place_forget(), page.button_logo.place_forget()
        self.bar_prev.main_frame.destroy(), self.bar_prev.scrollbar.pack_forget()
        Label(page.window, bg='lightgrey', width=width // 15, height=height // 40).place(x=80, y=80)
        page.button_logo = Button(page.window, image=image2, bd=0, bg='lightgrey', activebackground='lightgrey',
                                  command=lambda: worker.restarting())
        page.button_logo.place(x=width / 4.5, y=height / 3.5)


def make_categories(codes: list) -> tuple:
    helping = ()
    starting = 0
    for value in codes:
        if int(value[0]) == starting:
            helping += value,
        else:
            starting += 1
            yield helping
            helping = value,
    yield helping


def message_maker() -> None:
    change = messagebox.askyesno(title='Potvrdenie zmien', icon='warning', message='Prajete si uložiť zmeny?')
    if change:
        for changes in changings:
            changes[0].set(changes[1])
        page.message_button['state'] = DISABLED


def massage_confirm() -> None:
    messagebox.showinfo(message='Zmeny boli ulozene :)')


def find_goods(buy: Button, sell: Button, buy_p: StringVar, sell_p: StringVar, confirm: Button) -> None:
    confirm['state'] = ACTIVE
    buy['state'] = sell['state'] = NORMAL
    sell_p.set('0.00')
    buy_p.set('0.00')


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
    sell = Entry(search, textvariable=x, state=DISABLED)
    sell.grid(row=1, column=2)
    buy = Entry(search, textvariable=y, state=DISABLED)
    buy.grid(row=1, column=3)
    confirm = Button(search, text='confirm', state=DISABLED, command=lambda: set_goods(x, y, search))
    confirm.place(x=0, y=70)
    submit = Button(search, text='Vyhladaj', command=lambda: find_goods(buy, sell, x, y, confirm), pady=0)
    submit.grid(row=1, column=1)


root = Tk()
root.configure(bg='white')
root.attributes('-fullscreen', True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
main_font, mini_font = width // 100, width // 200
changings = {}
category = ('Ovocie', 'zelenina', 'Pečivo', 'Mäso', 'Mliečne výrobky', 'Nápoje', 'Sladkosti/Slanosti', 'Ostatné')
image2 = PhotoImage(file='bez_pozadia.png')
with open('Cennik.txt') as file:
    file = sorted(file.read().rstrip().split('\n')[1:], key=lambda x: x[0:4])

categories = tuple(make_categories(file))

page = Mainpage()
bar_prev = Bar(active=False)
previous = Button()
worker = MakeWork()
root.bind('<Escape>', lambda event: root.destroy())
if __name__ == '__main__':
    root.mainloop()
