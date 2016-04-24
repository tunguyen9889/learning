import calendar


def checkio(year):
    full_year = calendar.Calendar().yeardayscalendar(year, 12)
    unlucky_days_count = 0
    for month in range(0, 12):
        for week in full_year[0][month]:
            if week[4] == 13:
                unlucky_days_count += 1
    return unlucky_days_count

# Clearance solution
# def checkio(year):
#     return sum(1 for i in range(1, 13) if calendar.weekday(year, i, 13) == 4)
# Or
# return sum(date(year, month, 13).isoweekday() == 5 for month in range(1,13))


if __name__ == '__main__':
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
