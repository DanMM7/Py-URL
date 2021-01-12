from tkinter import *
import pyshorteners
import clipboard

window = Tk()
# set default window size, width x height
window.geometry("400x200")
window.resizable(False, False)

# set Title
window.title("URL-shortener")

# url input
url_input = Entry(window, font=("Arial", "16"))
url_input.grid(row=1, column=2, pady=6)

# label shortened url
str_url = StringVar(window)

shortened_url = Label(window, textvariable=str_url, font=("Arial", "16"), fg="#fff", bg="#3498db")
shortened_url.grid(row=1, column=2, pady=6)


# copy url function
def copy_short_url():
    try:
        clipboard.copy(str_url.get())
        print("URL copied!")
    except:
        str_url.set("Something went wrong, Try again!")


# copy url button
copy_btn = Button(window, text="Copy", bg="#3498db", fg="#fff", font=("Arial", "16"), command=copy_short_url)
copy_btn.grid(row=3, column=3, pady=6, padx=10)


# shortening function
def short_url():
    try:
        s = pyshorteners.shortener()
        url = url_input.get()
        result = s.tinyurl.short(url)
        str_url.set(result)
        # clear url
        url_input.delete(0, END)
    except:
        str_url.set("")


# click button to make url short
btn = Button(window, text="shorten URL", padx=8, pady=4, bg="#34495e", fg="#fff", font=("Arial", "16"),
             activebackground="#34495e", command=short_url)
btn.grid(row=2, column=2, pady=6)

window.mainloop()
