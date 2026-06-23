from datetime import date
months = {
        1: "январь",
        2: "февраль",
        3: "март",
        4: "апрель",
        5: "май",
        6: "июнь",
        7: "июль",
        8: "август",
        9: "сентябрь",
        10: "октябрь",
        11: "ноябрь",
        12: "декабрь"
    }

def translate(today_date:date) -> str:
    number_month = today_date.month
    month = months.get(number_month)
    return f"{today_date.day} {month} {today_date.year}"