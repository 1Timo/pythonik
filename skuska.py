from tkinter import *
from tkinter import messagebox
from time import strftime, localtime


class Mainpage:
    def __init__(self):
        background = Canvas(root, width=width, height=height, bg='white')
        background.create_rectangle(0, 0, width / 5, height,  fill='#98c151', outline='#98c151')
        background.create_text(width / 10, height / 10, text='Cenotvorba', font='Roboto {}'.format(width//50))
        background.pack()
        self.check = True
        self.window = Canvas(root, width=width, height=height, bg='white')
        self.window.place(x=width / 5, y=0)
        self.window.create_line(0, height / 15 * 14, width, height / 15 * 14, fill='darkgrey', width=2)
        self.window.create_line(1, 0, 1, height, fill='darkgrey', width=2)
        self.button_logo = Button(self.window, image=image,
                                  bd=0,
                                  bg='white',
                                  activebackground='white',
                                  highlightthickness=False,
                                  command=lambda: worker.restarting())
        self.button_logo.place(x=width / 4.5, y=height / 3.5)

        def time_bar(time=self.window.create_line(0, 0, 0, 0)) -> None:
            self.window.delete(time)
            time = self.window.create_text(width / 10 * 6.5, height / 20 * 19, anchor=NW,
                                           text=strftime('%A %d.%b %Y %H:%M:%S', localtime()))
            self.window.update()
            self.window.after(1000, time_bar, time)

        self.button = Button(root, text='Ovocie',
                             font='Roboto {}'.format(main_font),
                             highlightthickness=False,
                             fg='white',
                             bg='#98C151',
                             anchor=W,
                             activeforeground='white',
                             relief=FLAT,
                             height=2,
                             activebackground='#679222',
                             command=lambda: worker.do(categories[0], self.button))
        self.button.place(x=0, y=height / 20 * 3.5, width=width/5)

        self.button1 = Button(root, text='Zelenina',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              fg='white',
                              activeforeground='white',
                              relief=FLAT,
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[1], self.button1))
        self.button1.place(x=0, y=height / 20 * 5.25, width=width/5)

        self.button2 = Button(root, text='Pečivo',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[2], self.button2))
        self.button2.place(x=0, y=height / 20 * 7, width=width/5)

        self.button3 = Button(root, text='Mäso',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              activeforeground='white',
                              relief=FLAT,
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[3], self.button3))
        self.button3.place(x=0, y=height / 20 * 8.75, width=width/5)

        self.button4 = Button(root, text='Mliečne výrobky',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[4], self.button4))
        self.button4.place(x=0, y=height / 20 * 10.5, width=width/5)

        self.button5 = Button(root, text='Nápoje',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              activeforeground='white',
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[5], self.button5))
        self.button5.place(x=0, y=height / 20 * 12.25, width=width/5)

        self.button6 = Button(root, text='Sladkosti/Slanosti',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              relief=FLAT,
                              fg='white',
                              activeforeground='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[6], self.button6))
        self.button6.place(x=0, y=height / 20 * 14, width=width/5)

        self.button7 = Button(root, text='Ostatné',
                              font='Roboto {}'.format(main_font),
                              highlightthickness=False,
                              bg='#98C151',
                              activeforeground='white',
                              relief=FLAT,
                              fg='white',
                              anchor=W,
                              height=2,
                              activebackground='#679222',
                              command=lambda: worker.do(categories[7], self.button7))
        self.button7.place(x=0, y=height / 20 * 15.75, width=width/5)

        self.search_button = Button(root, text='Vyhladaj Tovar',
                                    font='Roboto {}'.format(main_font),
                                    highlightthickness=False,
                                    bg='#98C151',
                                    anchor=W,
                                    fg='white',
                                    activeforeground='white',
                                    relief=FLAT,
                                    height=2,
                                    activebackground='#679222',
                                    command=searching)
        self.search_button.place(x=0, y=height / 20 * 17.5, width=width/5)

        self.message_button = Button(root, text='Potvrdiť',
                                     font='Roboto {}'.format(main_font // 2),
                                     state=DISABLED,
                                     width=10,
                                     bg='grey',
                                     activeforeground='white',
                                     fg='white',
                                     relief=RAISED,
                                     bd=3,
                                     activebackground='grey')
        time_bar()


class Bar:
    def __init__(self, starting: list = None, active=False, categ: tuple = (), working: Button = None, error=()):
        self.main_frame = Frame(page.window)
        self.canvas = Canvas(self.main_frame, bg='white')
        self.frame = Frame(self.canvas, height=height / 2)
        self.scrollbar = Scrollbar(self.main_frame, orient="vertical", command=self.canvas.yview)
        self.categ = categ
        if not active:
            return
        self.errors = error
        self.button = working
        page.button_logo.place(x=width / 20 * 13.75, y=0)
        page.button_logo['image'] = low_img
        page.window.create_rectangle(0, 0, width / 3, height / 4, fill='white', outline='white')
        page.window.create_text(width/10, height/10, anchor=NW, text=category[int(starting[0][0])],
                                font=f'Roboto {main_font + 10}')
        page.window.update()
        page.message_button.place(x=width / 20 * 15, y=height / 20 * 17)
        page.message_button['command'] = lambda: self.controler(starting)
        self.main_frame.place(x=width / 20 * 5, y=height / 20 * 5)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.frame, anchor='nw')
        self.scrollbar.pack(fill=Y, side="right")
        self.canvas.pack()
        self.frame.bind("<Configure>", lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox("all"), width=width / 4 + 5, height=height // 2))
        for shift in range(5, 9):
            shift = shift + 0.3 if shift == 6 else shift + 0.6 if shift == 7 else shift + 0.9 if shift == 8 else shift
            Label(page.window,
                  text='Kód tovaru:' if shift == 5 else 'Názov tovaru' if shift == 6.3 else'Cena zakupenia'
                  if shift == 7.6 else 'Cena tovaru',
                  relief=RAISED,
                  width=width//125,
                  font=f'Roboto {mini_font}').place(x=width / 20 * shift, y=height / 20 * 5 - 18)
        for index, value in enumerate(starting):
            value = value.split(';')
            color1 = 'lightgrey'
            color2 = 'white'
            for error in self.errors:
                if index == error.row:
                    color1 = color2 = 'red'
                    break

            self.categ += (Goods(value[0], value[1], value[2], value[3], index, color1, color2, self.frame)),

        page.window.update()
        page.check = True
        self.controling()

    def controling(self) -> None:
        if self.values_finding():
            page.message_button['state'] = ACTIVE
            return

        if self.categ:
            self.frame.after(1000, self.controling)

    def controler(self, starting) -> None:
        self.errors = ()
        start = 0

        while True:
            value = self.values_finding(start)
            if not value:
                break

            if not isinstance(value, bool):
                val1 = value.entry1.get().replace(' ', '')
                val2 = value.entry2.get().replace(' ', '')

                if val1.isdigit() or val2.isdigit() or len(val1) < 3 or len(val2) < 3:
                    self.errors += value,

                elif val1[-3] != '.' or val2[-3] != '.':
                    self.errors += value,

                elif not (val1[:-3].isdigit() and val1[-2:].isdigit()) or not (val2[:-3].isdigit()
                                                                               and val2[-2:].isdigit()):
                    self.errors += value,

                start = value.row + 1

        message_maker(self.categ, starting, self.button, self.errors)

    def values_finding(self, start: int = 0):
        for Value in self.categ[start:]:
            if Value.sell != Value.entry1.get() or Value.buy != Value.entry2.get():
                return Value

        return False


class Goods:
    def __init__(self, code: str, name: str, sell: str, buy: str, row: int, color1: str, color2: str, frame: Frame):
        self.name = name
        self.frame = frame
        self.code = code
        self.sell = sell
        self.buy = buy
        self.row = row
        self.sell_price = StringVar()
        self.sell_price.set(self.sell)
        self.buy_price = StringVar()
        self.buy_price.set(self.buy)
        self.label = Label(self.frame, text=self.code + ':', relief=RAISED, bd=1, width=width//125, bg=color1)
        self.label.grid(row=self.row, column=0)
        self.label2 = Label(self.frame, anchor=W, text=self.name, relief=RAISED, bd=1, width=width//125, bg=color1)
        self.label2.grid(row=self.row, column=1)
        self.entry1 = Entry(self.frame, textvariable=self.sell_price, width=width//125, bg=color2)
        self.entry1.grid(row=self.row, column=2)
        self.entry2 = Entry(self.frame, textvariable=self.buy_price, width=width//125, bg=color2)
        self.entry2.grid(row=self.row, column=3)

    def __str__(self):
        return f'Goods({self.code}, {self.name}, {self.sell}, {self.buy}, {self.row},' \
               f' {self.entry1.get()}, {self.entry1}, {self.entry2.get()}, {self.entry2})'

    __repr__ = __str__


class MakeWork:
    def __init__(self):
        self.previous = previous
        self.bar_prev = bar
        self.allow = True

    def do(self, starting: list, working: Button, error: tuple = ()) -> None:
        if not page.check or not self.allow:
            return
        if error:
            self.allow = False
        page.check = False
        self.previous['bg'], self.previous['activebackground'] = '#98C151', '#98C151'
        working['bg'] = working['activebackground'] = '#679222'
        self.previous = working
        self.bar_prev.main_frame.destroy(), self.bar_prev.scrollbar.pack_forget()
        self.bar_prev = Bar(starting=starting, active=True, working=working, error=error)

    def restarting(self):
        if not self.allow:
            massage_confirm('Pred presmerovaním na začiatočnú stránku oprav chyby prosím', 'error')
            return

        self.previous['bg'], self.previous['activebackground'] = '#98C151', '#98C151'
        page.message_button.place_forget(), page.button_logo.place_forget()
        self.bar_prev.main_frame.destroy(), self.bar_prev.scrollbar.pack_forget()
        page.window.create_rectangle(0, 0, width / 3, height / 4, fill='white', outline='white')
        Label(page.window, bg='white').place(x=width/6, y=height/6, width=width/2.75, height=height/10)
        page.button_logo = Button(page.window, image=image, bd=0, bg='white', activebackground='white',
                                  highlightthickness=False,
                                  command=lambda: worker.restarting())
        page.button_logo.place(x=width / 4.5, y=height / 3.5)


def make_categories(codes: list) -> tuple:
    helping = []
    starting = 0
    for value in codes:
        if int(value[0]) == starting:
            helping += [value]
        else:
            starting += 1
            yield helping
            helping = [value]
    yield helping


def message_maker(values: tuple, starting: list, button: Button, errors: tuple) -> None:
    change = messagebox.askyesno(title='Potvrdenie zmien', icon='warning', message='Prajete si uložiť zmeny?')
    work = False
    if change:
        for Value in values:
            if Value.sell != Value.entry1.get() or Value.buy != Value.entry2.get():
                categories[int(starting[0][0])][Value.row] = f'{Value.code};{Value.name};' \
                                                             f'{Value.entry1.get()};{Value.entry2.get()}'
                if Value in errors:
                    continue
                work = True

        if work and errors:
            massage_confirm('V zadávaní sa našli chyby, sú označené červenou farbou, '
                            'program Vám neumožní urobiť nič, kým ich neopravíte !', 'error')
            massage_confirm('Ceny v ktorých nebola chyba sa úspešne zmenili :)', 'info')

        elif work and not errors:
            massage_confirm('Zmeny boli úspešne zmenené :)', 'info')

        elif not work and errors:
            massage_confirm('V zadávaní sa našli chyby, sú označené červenou farbou, '
                            'program Vám neumožní urobiť nič, kým ich neopravíte !', 'error')

    page.message_button['state'] = DISABLED
    worker.allow = True
    worker.do(starting=starting, working=button, error=errors if errors else ())


def massage_confirm(say=None, show='warning') -> None:
    messagebox.showinfo(message=say, icon=show)


def find_goods(search: Toplevel, confirming: Button, code: Entry, selling: StringVar, buying: StringVar,
               entry1: Entry, entry2: Entry) -> None:
    if not code.get():
        massage_confirm('Zabudli ste zadat kod')
        search.destroy()
        searching()
        return

    if not code.get().isdigit():
        massage_confirm('Kod sa sklada iba z cisiel!')
        return

    if not len(code.get()) == 4:
        massage_confirm('Kod ma nespravnu dlzku')
        return

    try:
        for i, value in enumerate(categories[int(code.get()[0])]):
            if code.get() == value[:4]:
                value = value.split(';')
                confirming['state'] = ACTIVE
                selling.set(value[2])
                buying.set(value[3])
                entry2['state'] = entry1['state'] = NORMAL
                confirming['command'] = lambda: set_goods(search, i, code, entry1, entry2, value)
                return
        massage_confirm('kod nenajdeny')
    except (IndexError, ValueError):
        massage_confirm('Zle zadany kod')


def set_goods(search: Toplevel, index: int, code: Entry, entry1: Entry, entry2: Entry, value: list) -> None:
    if entry2.get() == value[3] and entry1.get() == value[2]:
        search.destroy()
        return
    entry2['bg'] = entry1['bg'] = 'white'

    if entry1.get().isdigit() or len(entry1.get()) < 3:
        entry1['bg'] = 'red'

    elif entry1.get()[-3] != '.':
        entry1['bg'] = 'red'

    elif not entry1.get()[:-3].isdigit() or not entry1.get()[-2:].isdigit():
        entry1['bg'] = 'red'

    if entry2.get().isdigit() or len(entry2.get()) < 3:
        entry2['bg'] = 'red'

    elif entry2.get()[-3] != '.':
        entry2['bg'] = 'red'

    elif not entry2.get()[:-3].isdigit() or not entry2.get()[-2:].isdigit():
        entry2['bg'] = 'red'

    if entry1['bg'] != 'red' and entry2['bg'] != 'red':
        categories[int(code.get()[0])][index] = f'{value[0]};{value[1]};{entry1.get()};{entry2.get()}'
        search.destroy()
        massage_confirm('Zmeny boli uložené', 'info')

    else:
        massage_confirm('Zle nastavená cena', 'error')


def searching() -> None:
    if not worker.allow:
        return
    search = Toplevel(root)
    search.lift()
    search.title('Vyhladávanie tovaru')
    search.geometry('600x100')
    root.eval(f'tk::PlaceWindow {str(search)} center')
    search.bind('<Escape>', lambda event: search.destroy())
    Label(search, text='Kod:', width=width // 175, anchor=CENTER).grid(row=0, column=0)
    Label(search, text='Cena tovaru:', width=width // 175, anchor=W).grid(row=0, column=2)
    Label(search, text='Cena zakupenia:', width=width // 125, anchor=W).grid(row=0, column=3)
    x = StringVar()
    selling = StringVar()
    buying = StringVar()
    code = Entry(search, width=10, textvariable=x)
    code.grid(row=1, column=0)
    sell = Entry(search, state=DISABLED, textvariable=selling, bg='white')
    sell.grid(row=1, column=2)
    buy = Entry(search, state=DISABLED, textvariable=buying, bg='white')
    buy.grid(row=1, column=3)
    confirm = Button(search, text='confirm', state=DISABLED)
    confirm.place(x=0, y=70)
    submit = Button(search, text='Vyhladaj', command=lambda: find_goods(search, confirm, code, selling, buying,
                                                                        sell, buy))
    submit.grid(row=1, column=1)


def end_of_program():
    if not worker.allow:
        massage_confirm('Pred vypnutím programu opravte všetky chyby prosím', 'error')
        return
    bar.categ = False
    with open('Cennik.txt', 'w') as fil:
        fil.write(open('TOVAR.txt').readline())
        for line in categories:
            for values in line:
                values = values.split(';')
                fil.write('{};{};{}\n'.format(values[0], values[2], values[3]))
    root.destroy()


def txt_files(file: str, file_2: str) -> list:
    with open(file) as file, open(file_2) as file_2:
        categ = []
        check = start = 0
        file = sorted(file.read().rstrip().split('\n')[1:], key=lambda x: x[0:4])
        for good in sorted(file_2.read().rstrip().split('\n')[1:], key=lambda x: x[0:4]):
            code = good[:4]

            if int(code[0]) > check:
                check += 1
                yield categ
                categ = []

            for index in range(start, len(file)):
                price = file[index].split(';')
                if code == price[0]:
                    categ += [';'.join([price[0], good[5:], price[1], price[2]])]
                    break

                elif int(code) > int(price[0]):
                    categ += [code + ';' + good[5:] + ';' + '0.00' + ';' + '0.00']
                    break
            start = index

        yield categ


root = Tk()
root.configure(bg='white')
root.attributes('-fullscreen', True)
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
main_font, mini_font = round(width / 100), round(width / 200)
category = ('Ovocie', 'zelenina', 'Pečivo', 'Mäso', 'Mliečne výrobky', 'Nápoje', 'Sladkosti/Slanosti', 'Ostatné')
image = PhotoImage(file='bez_pozadia.png')
low_img = image.subsample(2, 2)

categories = tuple(txt_files('Cennik.txt', 'TOVAR.txt'))
root.bind('<Escape>', lambda event: end_of_program())
root.protocol("WM_DELETE_WINDOW", end_of_program)

if __name__ == '__main__':
    page = Mainpage()
    bar = Bar(active=False)
    previous = Button()
    worker = MakeWork()
    root.mainloop()

else:
    print(categories[0])
