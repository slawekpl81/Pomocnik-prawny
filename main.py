#       Pomocnik prawny
#
#       Program pomaga wyszukiwać słowa w aktach prawnych oraz wskazywać paragrafy
#       i artykuły.

#       Autor: S.Jona
#       10.2019

# pip install docx
# pip install python-docx
# ?? pip install textract

from tkinter import *
from tkinter import filedialog as fd
import webbrowser
import def_pp


class Aplikacja(Frame):

    def __init__(self, master):
        super(Aplikacja, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # MENU
        menubar = Menu(self)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Otwórz', command=self.open_file)
        filemenu.add_command(label="Wyjście", command=root.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)

        root.config(menu=menubar)

        # przycisk SZUKAJ
        self.knefel1 = Button(self, text="SZUKAJ", height=3, width=20)
        self.knefel1.grid(row=7, column=0, sticky=E)
        self.knefel1['command'] = self.knefel_start

        self.logo = PhotoImage(file="python2.gif")
        self.l_image = Label(self, image=self.logo)
        self.l_image.grid(row=12, column=0, sticky=N)

        # Label autor
        self.l_dev = Label(self, text='Sławek Jona - 2019 \n slawomir.jona@gmail.com')
        self.l_dev.grid(row=13, column=0, sticky=N)

        # Label nazwa pliku
        self.l_enter_file = Label(self, text='Szukaj w:')
        self.l_enter_file.grid(row=0, column=0, sticky=W)
        # pole nazwa pliku
        self.enter_file = Entry(self, width=60)
        self.enter_file.grid(row=1, column=0, sticky=W)

        # Label szukane słowo
        self.l_search_word = Label(self, text='Szukane słowo:')
        self.l_search_word.grid(row=2, column=0, columnspan=1, sticky=W)
        # pole szukane słowo
        self.search_word = Entry(self, width=60)
        self.search_word.grid(row=3, column=0, columnspan=4, sticky=W)

        # Label znak podziału dokumentu
        self.l_search_word = Label(self, text='Znak podziału dokumentu:')
        self.l_search_word.grid(row=4, column=0, columnspan=1, sticky=W)
        # Radiobuttons wyboru kontroli
        self.doc_sign = StringVar()  # zmienna przechowuje wynik wyboru
        self.doc_sign.set('Art.')

        Radiobutton(self,
                    text='Artykuły',
                    variable=self.doc_sign,
                    value='Art.',
                    command=self.update_radio
                    ).grid(row=5, column=0, sticky=W)
        Radiobutton(self,
                    text='§ Paragrafy',
                    variable=self.doc_sign,
                    value='§',
                    command=self.update_radio
                    ).grid(row=6, column=0, sticky=W)

        # Label Przydatne linki
        self.link1 = Label(self, text='Przydatne linki:', font='bold')
        self.link1.grid(row=8, column=0, columnspan=1, sticky=N)

        self.link2 = Label(self, text='Wyższy Urząd Górniczy', fg="blue", cursor="hand2")
        self.link2.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.wug.gov.pl/prawo/akty_prawne"))
        self.link2.grid(row=9, column=0, columnspan=1, sticky=N)

        self.link3 = Label(self, text='Państwowa Agencja Atomistyki', fg="blue", cursor="hand2")
        self.link3.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.paa.gov.pl/strona-39-prawo.html"))
        self.link3.grid(row=10, column=0, columnspan=1, sticky=N)

        self.link3 = Label(self, text='Prawo budowlane', fg="blue", cursor="hand2")
        self.link3.bind("<Button-1>", lambda e: webbrowser.open_new("http://prawo-budowlane.org/"))
        self.link3.grid(row=11, column=0, columnspan=1, sticky=N)

        return 0

    def knefel_start(self):
        file = self.enter_file.get()
        word = self.search_word.get()
        sign = self.doc_sign.get()
        if file == '' or file == 'BRAK PLIKU !!!':
            self.enter_file.delete(0, END)
            self.enter_file.insert(0, 'BRAK PLIKU !!!')
            return 0
        if word == '' or file == 'BRAKI !!!':
            self.search_word.delete(0, END)
            self.search_word.insert(0, 'BRAKI !!!')
            return 0

        def_pp.search_word(file, word, sign)
        return 0

    def open_file(self):
        filename = fd.askopenfilename()  # wywołanie okna dialogowego open file
        print(filename)
        if filename:
            self.enter_file.delete(0, END)
            self.enter_file.insert(0, str(filename))

    def update_radio(self):
        self.doc_sign.get()
        print(str(self.doc_sign.get()))


####################
root = Tk()
root.title('Pomocnik prawny 1.0')
root.geometry('410x470')

apka = Aplikacja(root)
root.mainloop()
