print("Hello World")
print("Hello Git")

from datetime import datetime
date = ""

def get_days_from_today(date):
    try:
        date = input("Enter the date in the format YYYY-MM-DD: ")
        date_dt = datetime.strptime(date, '%Y-%m-%d')
        date_toord = date_dt.toordinal()
        now_dt = datetime.today()
        now_toord = now_dt.toordinal()
        difference_days = now_toord - date_toord
        return difference_days
    except ValueError:
        print("Date must be in the format YYYY-MM-DD")

print(get_days_from_today(date))