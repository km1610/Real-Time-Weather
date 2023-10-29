import requests
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox

app = tkinter.Tk()

Entry_label = tkinter.Label(app,text="Enter the city name")
Entry_label.pack()
Entry = tkinter.Entry(app)
Entry.pack()
def get_weather_data():
    c1 = city = Entry.get()
    city=city.replace(" ","+")
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    data = str.split('\n')
    time = data[0]
    sky = data[1]

    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
  
    Dialog = tkinter.messagebox.showinfo(title=f'Data for {c1}',message=f'Temperature: {temp}\nTime: {time}\nDescription: {sky}\n')

app.title("Real Time Weather")

GoBtn = tkinter.Button(app,text="Search",command=get_weather_data)
GoBtn.pack()

app.mainloop()
