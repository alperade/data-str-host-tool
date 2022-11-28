import requests
from ics import Calendar
from csv_ical import Convert
from bs4 import BeautifulSoup
from keys import BNB_ICAL
from datetime import date

def get_calendar():
    url = BNB_ICAL
    try:
        cal = Calendar(requests.get(url).text)
        cal_dict = {}
        for event in cal.events:
            if event.description:
                cal_dict[event.begin.format('YYYY-MM-DD')] = {
                    "check_in": event.begin.format('YYYY-MM-DD'),
                    "check_out": event.end.format('YYYY-MM-DD'),
                    "detail_url": event.description[17:79]
            }
        return cal_dict

    except requests.HTTPError as e:
        print(f"Exception caught: {e}")


test_url = BeautifulSoup(requests.get('https://www.airbnb.com/rooms/51817665').text,'html.parser')
url_list = test_url.find_all("meta", attrs={"data-testid":"url"})


if __name__ == '__main__':
    get_calendar()
