from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_diff = (birthday_this_year - today).days

        if 0 <= days_diff <= 7:
            congratulation_date = birthday_this_year
            if congratulation_date.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

users = [
    {"name": "John Doe", "birthday": "1985.10.30"},
    {"name": "Jane Smith", "birthday": "1990.10.22"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
