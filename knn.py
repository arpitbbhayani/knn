__author__ = 'arpit'

"""
    Code for the window skeleton for
    knn visualization and classification.
"""

from Tkinter import Tk, BOTH, Frame
from ttk import Button, Style


class KnnFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.style = Style()
        self.init_ui()

    def center_window(self):
        width_knn = 500
        height_knn = 500

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw-width_knn)/2
        y = (sh-height_knn)/2

        self.parent.geometry('%dx%d+%d+%d' % (width_knn, height_knn, x, y))

    def init_ui(self):
        self.parent.title("knn - Classification")
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)
        self.center_window()
        quit_button = Button(self, text="Close", command=self.quit)
        quit_button.place(x=50, y=50)


def main():
    root = Tk()
    app = KnnFrame(root)
    root.mainloop()


if __name__ == '__main__':
    main()

print "Hello Devilo"