from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date.strip(), "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta_days = (current_date - input_date).days
        return delta_days

    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД', наприклад '2020-10-09'.")

print(get_days_from_today('2020-10-09'))