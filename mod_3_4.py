from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.03.12"},
    {"name": "Ja Smooth", "birthday": "1980.03.16"},
    {"name": "Ane Spith", "birthday": "1960.04.27"}
]

def get_upcoming_birthdays(users):
    current_date = datetime.today().date()
    result = []
    for user in users:
        birthday_dt = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = datetime(year=current_date.year,
                                      month=birthday_dt.month,
                                      day=birthday_dt.day).date()
        congratulation_period = timedelta(days=7)
        if birthday_this_year < current_date or birthday_this_year > current_date + congratulation_period:
            continue
        congratulation_date = birthday_this_year
        if birthday_this_year.weekday() == 5:
            congratulation_date = birthday_this_year + timedelta(days=2)
        if birthday_this_year.weekday() == 6:
            congratulation_date = birthday_this_year + timedelta(days=1)
        result.append({user["name"]: congratulation_date.strftime("%Y.%m.%d")})  
    return result
    
print(get_upcoming_birthdays(users))