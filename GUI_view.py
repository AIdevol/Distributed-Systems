import tkinter as tk
from tkinter import ttk, messagebox, simpledialog, font
from tkinter.ttk import Combobox
from threading import Thread
from queue import Queue
import connect as st

globaldata: dict

class Index:

    def __init__(self, master):
        self.master = master
        container = tk.Frame(self.master)
        container.pack(side="top", expand=True, fill="both")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LogInPage, SignInPage, SearchPage, DisplayPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back = tk.Label(self, bg="powder blue", width=1800, height=2)
        back.pack(side=tk.TOP)

        font_Title = font.Font(family="Georgia", weight="bold", size=28)
        font_Button = font.Font(family="Sylfaen")
        font_Bottom = font.Font(family="sylfaen", weight="bold", size=22)

        label = tk.Label(self, text="Welcome To Book Shell", font=font_Title, bg="red")
        label.pack(fill=tk.X)

        button1 = tk.Button(self, text="Log In", bg="yellow", fg="red",
                            font=font_Button, command=lambda: controller.show_frame(LogInPage))

        button1.place(x=250, y=190)

        button2 = tk.Button(self, text="Sign Up",
                            bg="yellow", fg="red", font=font_Button, command=
                            lambda: controller.show_frame(SignInPage))

        button2.place(x=430, y=190)

        bottom_frame = tk.Label(self, text="Wellcome to The Book Inventory System", font=font_Bottom,
                             fg="green", bg="orange")

        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

class SignInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font_Title = font.Font(family="Georgia", weight="bold", size=28)
        font_Button = font.Font(family="Sylfaen")
        font_Bottom = font.Font(family="sylfaen", weight="bold", size=22)
        font_Details = font.Font(family="Georgia", weight="bold", size=14)

        Detail_Block = tk.Label(self, text="Welcome Fill Your Details", font=font_Title,
                             bg="red")
        Detail_Block.pack(fill=tk.X)
        Label_UserEmail = tk.Label(self, text="Email Id", font=font_Details)
        Label_UserEmail.place(x=150, y=136)

        Label_Password = tk.Label(self, text = "Password", font = font_Details)
        Label_Password.place(x=150, y=176)

        UserEmail = tk.Entry(self, font = font_Details)
        UserEmail.place(x = 300, y = 136)

        Password = tk.Entry(self, font = font_Details, show = "*", fg = "black")
        Password.place(x = 300, y = 176)

        SignInButton = tk.Button(self, text = "Sign In", font = font_Button, fg = "red"
                              , command = lambda: self.create(UserEmail.get(), Password.get(), controller))

        SignInButton.place(x = 320, y = 235)

        HomeButton = tk.Button(self, text = "Home", font = font_Button,
                            fg = "red", command = lambda: controller.show_frame(StartPage))

        HomeButton.place(x = 400, y = 235)
        bottom_frame = tk.Label(self, text = "Welcome to The Book Inventory System", font = font_Bottom,
                             fg = "green", bg = "orange")

        bottom_frame.pack(side = tk.BOTTOM, fill = tk.X)

    def create(self, UserEmail, Password, controller):
        b = st.CreateAccount(UserEmail, Password)
        if b == 1:
            controller.show_frame(LogInPage)
        else:
            messagebox.showinfo("Info", "Invalid Password Or Email")

class LogInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font_Title = font.Font(family="Georgia", weight="bold", size=28)
        font_Button = font.Font(family="Sylfaen")
        font_Bottom = font.Font(family="sylfaen", weight="bold", size=22)
        font_Details = font.Font(family="Georgia", weight="bold", size=14)

        DetailBlock = tk.Label(self, text="Enter Your Details", font=font_Title, bg="red")
        DetailBlock.pack(fill=tk.X)
        LabelUserName = tk.Label(self, text="User Name", font=font_Details)
        LabelUserName.place(x=150, y=136)

        LabelPassword = tk.Label(self, text="Password", font=font_Details)
        LabelPassword.place(x=150, y=176)

        UserName = tk.Entry(self, font=font_Details, show="")
        UserName.place(x=300, y=136)

        Password = tk.Entry(self, font=font_Details, show="*", fg="black")
        Password.place(x=300, y=176)

        LogInButton = tk.Button(self, text="Log In", font=font_Button, fg="red"
                             , command=lambda: self.LogInaccount(UserName.get(), Password.get(), controller))

        LogInButton.place(x=320, y=235)

        Forget_Button = tk.Button(self, text="Forget password", fg="black"
                               , height=1, command=lambda: self.Reset_Password())

        Forget_Button.place(x=330, y=285)

        bottom_frame = tk.Label(self, text="Wellcome to The Book Inventory System", font=font_Bottom,
                             fg="green", bg="orange")

        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    def LogInaccount(self, UserName, Password, controller):
        
        b = st.log_in(UserName, Password)
        if b == 1:
            controller.show_frame(SearchPage)
        else:
            messagebox.showinfo("Info", "Invalid Password Or Email")


    def Reset_Password(self):
        s = simpledialog.askstring("Input", "Enter Your Email-Id")
        b = st.ResetPassword(s)
        if b == 1:
            messagebox.showinfo("Info", "reset link send to your Email")

    def LogInaccount(self, UserName, Password, controller):
        b = st.LogAccount(UserName, Password)
        if b == 1:
            controller.show_frame(SearchPage)
        else:
            messagebox.showinfo("Info", "Invalid Password Or Email")

class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back = tk.Label(self, bg="powder blue", width=1800)
        back.pack(side=tk.TOP)
        font_Title = font.Font(family="Georgia", weight="bold", size=28)
        font_Button = font.Font(family="Sylfaen")
        font_Bottom = font.Font(family="sylfaen", weight="bold", size=22)
        font_box = font.Font(family="Georgia", weight="bold", size=16)

        label = tk.Label(self, text = "Welcome To Search Shell", font = font_Title, bg = "red")
        label.pack(fill = tk.X)
        labe2 = tk.Label(self, text = "Enter the Details",
                         font = font_Title, bg = "powder blue")
        labe2.pack(fill = tk.X)

        search_label = tk.Label(self, text = "Search By:", font = font_box)
        search_label.place(x = 110, y = 144)

        search_list = ["Book Name", "Book UPC", "Book price"]
        self.combobox = Combobox(self, values = search_list, height = 5, width = 14, font = font_box)
        self.combobox.place(x = 280, y = 144)

        enter = tk.Label(self, text = "Enter Detail:", font = font_box)
        enter.place(x = 110, y = 190)
        self.entrybox = tk.Entry(self, font = font_box, show = "", fg = "black", width = 16)
        self.entrybox.place(x = 280, y = 190)

        search_button = tk.Button(self, text = "Search", font = font_box, bg = "#47d147",
                               width = 7, command = lambda: self.getEnteredDetails())
        search_button.place(x = 545, y = 160)

        scriptbox = tk.Label(self, text = "Run Script:", font = font_box)
        scriptbox.place(x = 110, y = 250)  # 47d147

        run_button = tk.Button(self, text = "Run", font = font_box, bg = "#47d147",
                            width = 7, command = lambda: self.message())
        run_button.place(x = 335, y = 240)

        view_label = tk.Label(self, text = "View All Records", font = font_box
                           )
        view_label.place(x = 110, y = 320)

        viewall_button: tk.Button = tk.Button(self, text="View", font=font_box,
                                        bg="#47d147", width=7,
                                        command=lambda: controller.show_frame(DisplayPage))
        viewall_button.place(x=335, y=310)
        button2 = tk.Button(self, text="Home", bg="#47d147", width=7
                            , font=font_box, command=lambda: controller.show_frame(StartPage))

        button2.place(x=463, y=420)
        bottom_frame = tk.Label(self, text="Wellcome To Book Inventory system", font=font_Bottom,
                             fg="green", bg="orange")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def message(self):
        messagebox.showinfo("Fetching Data from Website", "Script running successfully in Background")

    def getEnteredDetails(self):
        selected_item_list = self.combobox.get()
        details = self.entrybox.get()

        if selected_item_list and details:
            d = MyDialog(self.master, selected_item_list, details)
            self.master.wait_window(d.top)
            self.callNewFrame(single_book_detail=globaldata)
        else:
            messagebox.showerror("Error", "Please enter any detail to search.")

    def callNewFrame(self, single_book_detail):
        displaySingleBookDetails = tk.Tk()
        displaySingleBookDetails.geometry("780x520+160+80")
        displaySingleBookDetails.title(single_book_detail['Book-name'])

        self.font_box = font.Font(family="Georgia", weight="bold", size=16)
        self.font_data = font.Font(family="Sylfaen", size=16)

        label = tk.Label(displaySingleBookDetails, text="Displaying Book Details", bg="red", font=self.font_box)
        label.pack(fill=tk.X)

        search_label = tk.Label(displaySingleBookDetails, text="Book Name", font=self.font_box)
        search_label.place(x=110, y=144)

        book_name = tk.Label(displaySingleBookDetails, text=single_book_detail['Book-name'], height=5, width=14,
                          font=self.font_data)
        book_name.place(x=525, y=90)

        enter = tk.Label(displaySingleBookDetails, text="Book Price", font=self.font_box)
        enter.place(x=110, y=190)

        book_price = tk.Label(displaySingleBookDetails, text=single_book_detail['Book-price'], fg="black", width=16,
                           font=self.font_data)
        book_price.place(x=485, y=190)

        scriptbox = tk.Label(displaySingleBookDetails, text="Number of Books Available", font=self.font_box)
        scriptbox.place(x=110, y=250)

        run_button = tk.Label(displaySingleBookDetails, text=single_book_detail['Book-avail'], font=self.font_data)
        run_button.place(x=550, y=250)

        view_label = tk.Label(displaySingleBookDetails, text="Book UPC Code", font=self.font_box)
        view_label.place(x=110, y=320)

        viewall_button = tk.Label(displaySingleBookDetails, text=single_book_detail['Book-UPC'], font=self.font_data)
        viewall_button.place(x=525, y=320)

        button2 = tk.Button(displaySingleBookDetails, text="Close", bg="#47d147", width=7, font=self.font_box,
                            command=displaySingleBookDetails.destroy)
        button2.place(x=350, y=420)

        displaySingleBookDetails.mainloop()


class MyDialog:
    def __init__(self, parent, search_criteria, search_details):
        self.top = tk.Toplevel(parent)
        self.top.title("Search Results")

        self.font_box = font.Font(family="Georgia", weight="bold", size=16)
        self.font_data = font.Font(family="Sylfaen", size=16)

        self.label = tk.Label(self.top, text="Search Results", bg="red", font=self.font_box)
        self.label.pack(fill=tk.X)

        self.result_label = tk.Label(self.top, text=f"Searching for {search_criteria}: {search_details}",
                                     font=self.font_box)
        self.result_label.pack(fill=tk.X)

        self.queue = Queue()

        self.search_thread = Thread(target=self.search_thread_function, args=(search_criteria, search_details))
        self.search_thread.start()

        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

    def search_thread_function(self, search_criteria, search_details):
        result = st.SearchBooks(search_criteria, search_details)
        self.queue.put(result)

    def on_closing(self):
        self.top.destroy()


class DisplayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        back = tk.Label(self, bg="powder blue", width=1800)
        back.pack(side=tk.TOP)
        font_Title = font.Font(family="Georgia", weight="bold", size=28)
        font_Button = font.Font(family="Sylfaen")
        font_Bottom = font.Font(family="sylfaen", weight="bold", size=22)
        font_box = font.Font(family="Georgia", weight="bold", size=16)

        label = tk.Label(self, text="Display All Books", font=font_Title, bg="red")
        label.pack(fill=tk.X)

        viewall_button = tk.Button(self, text="View All", font=font_box, bg="#47d147", width=10,
                                   command=lambda: self.show_all_books(controller))
        viewall_button.place(x=350, y=200)

        button2 = tk.Button(self, text="Home", bg="#47d147", width=7, font=font_box,
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=350, y=300)

        bottom_frame = tk.Label(self, text="We Love Web Scrapping", font=font_Bottom, fg="green", bg="orange")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X)

    def show_all_books(self, controller):
        if all_books := st.ViewBooks():
            display_all_books = tk.Tk()
            display_all_books.geometry("800x600")
            display_all_books.title("All Books")

            self.font_box = font.Font(family="Georgia", weight="bold", size=16)

            label = tk.Label(display_all_books, text="Displaying All Books", bg="red", font=self.font_box)
            label.pack(fill=tk.X)

            for book in all_books:
                book_details = f"Book Name: {book['Book-name']}\n" \
                                       f"Book UPC: {book['Book-UPC']}\n" \
                                       f"Book Price: {book['Book-price']}\n" \
                                       f"Number of Books Available: {book['Book-avail']}\n\n"

                book_label = tk.Label(display_all_books, text=book_details, font=self.font_box)
                book_label.pack(fill=tk.X)

            button2 = tk.Button(display_all_books, text="Close", bg="#47d147", width=7, font=self.font_box,
                                command=display_all_books.destroy)
            button2.pack(pady=10)

            display_all_books.mainloop()
        else:
            messagebox.showinfo("Info", "No books available to display.")


if __name__ == "__main__":
    app = Index(tk.Tk())
    app.master.title("Book Shell")
    app.master.geometry("800x600")
    app.master.resizable(width=False, height=False)
    app.master.mainloop()
