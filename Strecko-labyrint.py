import tkinter
import os


class Labyrint:
    def __init__(self, canvas: tkinter.Canvas, i: int, j: int, color: str, big: int):
        self.canvas = canvas
        self.y = i
        self.x = j
        self.color = color
        self.big = big

    def paint(self) -> None:
        self.canvas.create_rectangle(self.x * self.big + self.big, self.y * self.big + self.big,
                                     self.x * self.big + 2*self.big, self.y * self.big + 2*self.big,
                                     fill=self.color)


class Game:
    def __init__(self, file: str = 'coordinates.txt', big: int = 30, width: int = 500, height: int = 500):
        self.width, self.height = width, height
        self.big = big
        self.root = tkinter.Tk()
        self.root.title('Labyrint')
        self.canvas = tkinter.Canvas(self.root, width=width, height=height, bg='gray')
        self.canvas.pack()
        self.lab, self.file, = (), file
        self.num, self.color, self.labyrint = None, '', []
        self.x = self.y = 0
        self.canvas.bind_all('<Up>', lambda event: self.move_ball(self.y - 1, self.x))
        self.canvas.bind_all('<Down>', lambda event: self.move_ball(self.y + 1, self.x))
        self.canvas.bind_all('<Left>', lambda event: self.move_ball(self.y, self.x - 1))
        self.canvas.bind_all('<Right>', lambda event: self.move_ball(self.y, self.x + 1))
        self.canvas.bind_all('<Escape>', lambda event: self.destroy())
        self.make_file()
        self.game_plan()

    def make_file(self) -> None:
        if not os.path.exists(self.file):
            with open(self.file, 'w') as file:
                file.write('000000000000000\n011111100000000\n010000100011100'
                           '\n010000111110100\n010000100001100\n010000101111000'
                           '\n010000101000000\n011111101010000\n010000101011100\n'
                           '010000101110100\n010000100010100\n010100100010000'
                           '\n011110100010000\n000011101111112\n000000000000000')

        else:
            raise FileExistsError('subor, ktory chcel program pouzit uz je vytvoreny, prosim premenujte ho'
                                  ' alebo poslite svoj, popripade vymazte :)')

    def game_plan(self) -> None:
        stop = True
        with open(self.file) as file:
            for i, line in enumerate(file):
                self.lab += tuple(line.strip()),

                for j in range(len(self.lab[i])):
                    self.color = 'blue' if self.lab[i][j] == '0' else 'red' if self.lab[i][j] == '2' else 'white'
                    Labyrint(self.canvas, i, j, self.color, self.big).paint()

                    if self.lab[i][j] == '1' and stop:
                        self.x, self.y = i, j
                        self.ball()
                        stop = False

    def ball(self) -> None:
        self.canvas.delete('ball')
        self.canvas.create_oval(self.x * self.big + self.big * 1.2,
                                self.y * self.big + self.big * 1.2, self.x * self.big + 1.8 * self.big,
                                self.y * self.big + 1.8 * self.big, fill='red', tags='ball')

    def move_ball(self, y: int, x: int) -> None:
        if self.control(y, x):
            self.x, self.y = x, y
            self.ball()

    def control(self, y: int, x: int) -> bool:
        if self.lab[y][x] == '2':
            self.victory()

        return self.lab[y][x] == '1'

    def victory(self) -> None:
        self.canvas.delete('all')
        self.canvas.create_text(self.width//4, self.height//2, text='You have won', font='arial 25 bold', anchor='nw')
        os.remove(self.file)
        self.canvas.update()
        self.canvas.after(500)
        self.root.destroy()

    def destroy(self) -> None:
        os.remove(self.file)
        self.root.destroy()


if __name__ == '__main__':
    ''' 
        Game(file=..., g_width=..., big=..., width=..., height=...)
    
        Do parametru file mozete napisat svoj subor ak mate, ak nie sam sa vytvori a nasledne vymaze (nemusite 
        zadavat nic, vsetko je defaultne nastavene).
        
        Parameter big urcuje velkost jedneho stvorca, myslite na to, ze kvoli uprave musi byt aspon
        big * pocet vasich stvrocov mensi ako width a height canvasu.
        
        Dalej paramtere width a height su
        parametre canvasu, ak ich nenastavite predvolene su 500 a 500.
        
        Ukoncit hru mozete a ukoncujte tlacidlom esc
    '''
    Game()
    tkinter.mainloop()
