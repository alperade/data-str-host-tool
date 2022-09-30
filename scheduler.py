import schedule, time, requests
import duckdb, pandas
from keys import OPEN_WEATHER_API_KEY


url = f"https://api.openweathermap.org/data/2.5/weather?id=5127359&APPID={OPEN_WEATHER_API_KEY}"

page = requests.get(url)
data = page.json()
temp_k = data['main']['temp']
weather = data['weather'][0]['main']

print(temp_k)

# connect to an in-memory database
con = duckdb.connect()

temp_df = pandas.json_normalize(data['main'])
cal_df = pandas.read_csv('calendar.csv',names=['Status','Checkin','Checkout','Link','Contact','NA'])

# create the table "my_table" from the DataFrame "my_df"
con.execute("CREATE TABLE temp_table AS SELECT * FROM temp_df")
con.execute("CREATE TABLE cal_table AS SELECT * FROM temp_df")

# insert into the table "my_table" from the DataFrame "my_df"
#con.execute("INSERT INTO my_table SELECT * FROM my_df")

temp_test = con.execute("SELECT temp FROM my_table").df()

def job():
    #print(temp_k)
    #print(weather)
    #print(my_df)
    #print(temp_test)
    print(cal_df)

schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
