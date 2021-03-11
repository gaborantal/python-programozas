import calendar
import datetime

if __name__ == '__main__':
    most = datetime.datetime.now()

    naptar = calendar.month(most.year, most.month)
    print(naptar)

    print(calendar.calendar(most.year, 2, 2, 6, 3))

    # Hasznos funkciók
    print("Szökőév?", calendar.isleap(most.year))
    print("Szökőévek száma 2000 és 2020 között:", calendar.leapdays(2000, 2020))
    print(f"Mai nap: {calendar.day_name[most.weekday()]}")

    print("A jelenlegi hónap hetei")
    print(calendar.monthcalendar(most.year, most.month))


