import requests
from ics import Calendar
from csv_ical import Convert
from bs4 import BeautifulSoup
from keys import BNB_ICAL


url = BNB_ICAL

cal = Calendar(requests.get(url).text)

with open('calendar.ics', 'w') as f:
    f.writelines(cal.serialize_iter())

res_detail_url = list(cal.events)[0].description[17:79]

test_url = BeautifulSoup(requests.get('https://www.airbnb.com/rooms/51817665').text,'html.parser')
url_list = test_url.find_all("meta", attrs={"data-testid":"url"})

print(url_list)


#<td class="_xzo51qd" role="button" aria-disabled="false" aria-label="18, Tuesday, October 2022. Available. There is a 3 night minimum stay requirement. Select as check-in date. " tabindex="-1" style="width: 40px; height: 40px;"><div class="_6gi1qsw notranslate" data-testid="calendar-day-10/18/2022" data-is-day-blocked="false" style="width: 40px; height: 40px;">18</div></td>
# Print all the events
print(cal.events)

convert = Convert()
convert.CSV_FILE_LOCATION = 'calendar.csv'
convert.SAVE_LOCATION = 'calendar.ics'
convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)
