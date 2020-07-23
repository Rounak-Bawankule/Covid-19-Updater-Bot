# Importing modules
import requests
from win10toast import ToastNotifier
import json
import time

def covid_update():
    request = requests.get('https://coronavirus-19-api.herokuapp.com/all')
    info = request.json()
    content = f"Total Confirmed Cases: {info['cases']} \n Total Deaths: {info['deaths']} \n Total Recovered: {info['recovered']}"

    while True:
        notification = ToastNotifier()
        notification.show_toast("Covid-19 ", content , duration=25)
        time.sleep(60)

if __name__ == '__main__':
    covid_update()
