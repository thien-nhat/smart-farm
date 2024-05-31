from datetime import datetime, timedelta
import pytz

# Assume you have a datetime in UTC-8
utc_8_tz = pytz.timezone('Etc/GMT-8')
datetime_utc_8 = datetime.now(utc_8_tz)

# Convert to UTC+7
utc_7_tz = pytz.timezone('Etc/GMT+7')
datetime_utc_7 = datetime_utc_8.astimezone(utc_7_tz)

# Convert string to datetime
# Convert string to datetime
now = "2024-05-30 16:06:08"
time_format = "%Y-%m-%d %H:%M:%S"
datetime_obj = datetime.strptime(now, time_format)

# Add 15 hours and 47 minutes
new_time = datetime_obj + timedelta(hours=14, minutes=47)

print(new_time)