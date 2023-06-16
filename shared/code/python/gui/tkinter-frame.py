class MyFrame(tk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        tk.Frame.__init__(self, *args, **kwargs)
        self.pack()

root = tk.Tk()
a_new_frame = MyFrame(root)
root.mainloop()