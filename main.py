from data_weather import get_weather
import csv
from datetime import date

fieldnames = [
    'Date',
    'Temperature',
    'Weather',
    'Booking Date',
    'Check-in',
    'Check-out'
    ]

def create_csv():
    with open('./bnb_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def update_csv():
    today = date.today()
    temperature = get_weather()['temp']
    weather = get_weather()['weather']
    try:
        new_row = {'Date': today, 'Temperature': temperature, 'Weather': weather}
        with open('./bnb_data.csv', 'a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(new_row)
    except:
        print("Error updating CSV")


if __name__ == '__main__':
    update_csv()
