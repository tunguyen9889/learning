import calendar


def most_frequent_days(year):
    full_year = calendar.Calendar().yeardayscalendar(year, 12)
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_count = [0, 0, 0, 0, 0, 0, 0]
    frequent_days = []

    for month in range(0, 12):
        for week in full_year[0][month]:
            for day in range(0, len(weekdays)):
                if week[day] != 0:
                    days_count[day] += 1

    for day in range(0, len(weekdays)):
        if days_count[day] == max(days_count):
            frequent_days.append(weekdays[day])

    return frequent_days


if __name__ == '__main__':
    assert most_frequent_days(2399) == ['Friday'], "1st example"
    assert most_frequent_days(1152) == ['Tuesday', 'Wednesday'], "2nd example"
    assert most_frequent_days(56) == ['Saturday', 'Sunday'], "3rd example"
    assert most_frequent_days(2909) == ['Tuesday'], "4th example"
