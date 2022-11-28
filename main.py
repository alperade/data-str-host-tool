from data_weather import get_weather
from data_bnb_calendar import get_calendar
import csv
from datetime import date

fieldnames = [
    'Booking Date',
    'Check-in',
    'Check-out',
    'Temperature',
    'Weather',
    'URL'
    #'Booking Date',
    ]

def create_csv():
    with open('./bnb_data.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()


def update_csv():
    #Get check-in dates that exist in the CSV file
    existing_dates = []
    with open('bnb_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            existing_dates.append(row['Check-in'])

    #Add a new row to the CSV file if there is a new reservation
    today = date.today()
    temperature = get_weather()['temp']
    weather = get_weather()['weather']
    reservations = get_calendar()
    try:
        for reservation in reservations.values():
            if reservation["check_in"] in existing_dates:
                print(f'Check-in date: {reservation} already in the log.')
            else:
                new_row = {
                    'Booking Date': date.today(),
                    'Check-in': reservation["check_in"],
                    'Check-out': reservation["check_out"],
                    'Temperature': temperature,
                    'Weather': weather,
                    'URL': reservation["detail_url"]
                    }
                with open('./bnb_data.csv', 'a') as csvfile:
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writerow(new_row)
    except:
        print("Error updating CSV")

if __name__ == '__main__':
    update_csv()
