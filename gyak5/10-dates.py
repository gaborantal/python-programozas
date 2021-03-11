import datetime


def fn_date():
    ma = datetime.date.today()  # Class method, ami visszaadja a mai napot date objektumként
    print(ma)
    print(type(ma))
    print("--")
    egy_nap = datetime.date(2021, 3, 10)
    print(egy_nap)
    egy_nap2 = datetime.date.fromisoformat("2021-03-08")
    print(egy_nap)
    egy_nap3 = datetime.datetime.strptime("2021 (év) 03 (hó) 10. (nap)", "%Y (év) %m (hó) %d. (nap)")
    print(egy_nap)
    print(egy_nap.strftime("Év: %Y, hónap: %m, nap: %d"))
    print(egy_nap.year)
    print(egy_nap.month)
    print(egy_nap.day)
    print("operátorok")
    print("<", egy_nap2 < egy_nap)
    print(">", egy_nap2 > egy_nap)
    print("==", egy_nap2 == egy_nap)
    if datetime.date(2020, 12, 31) < datetime.date.today() < datetime.date(2021, 4, 1):
        print("2021 első negyedévében vagyunk.")
    print("--")


def fn_time():
    # time - csak az ido kezelesere (a datum nem szamit)
    # egy_idopillanat = datetime.time(12)
    # egy_idopillanat = datetime.time(12, 00)
    # egy_idopillanat = datetime.time(12, 0, 0)
    # egy_idopillanat = datetime.time(12, 00, 00, 123)
    egy_idopillanat = datetime.time(12, 10, 12, 123, datetime.timezone.utc)
    print("time", egy_idopillanat)
    print(egy_idopillanat.hour)
    # Vigyázat! A min az a lehető legkisebb értéke az objektumnak!
    print("min", egy_idopillanat.min)
    print("max", egy_idopillanat.max)
    print(egy_idopillanat.minute)
    print(egy_idopillanat.second)
    print(egy_idopillanat.microsecond)
    print("--")


def fn_datetime():
    most = datetime.datetime.now()

    egy_nap = datetime.date(2021, 3, 10)
    egy_idopillanat = datetime.time(12, 10, 12, 123, datetime.timezone.utc)

    valamikor = datetime.datetime.combine(egy_nap, egy_idopillanat)
    print(most)
    print(valamikor)
    print(most.year)
    print(most.month)
    print(most.day)
    print(most.hour)
    print(most.minute)
    print(most.second)
    print(most.microsecond)
    print(most.tzinfo)
    # 0 - Monday 1 - Tuesday 2 - Wednesday 3 - Thursday 4 - Friday 5 - Saturday 6 - Sunday
    print(most.weekday())
    # 1 - Monday 2 - Tuesday 3 - Wednesday 4 - Thursday 5 - Friday 6 - Saturday 7 - Sunday
    print(most.isoweekday())
    print("--")


def fn_timedelta():
    most = datetime.datetime.now()
    regebben = datetime.datetime(2021, 1, 1, 13, 33, 45, 10)

    delta = datetime.timedelta(days=10, hours=1, minutes=10, seconds=5, microseconds=100, milliseconds=98)
    print(most + delta)
    print(most - delta)
    print(delta.days)
    print(delta.seconds)
    print(delta.microseconds)
    delta = most - regebben
    print(delta)
    print(type(delta))
    print(type(delta))


if __name__ == '__main__':
    # date - dátumkezelés
    fn_date()

    # time - idő kezelés
    fn_time()

    # datetime - datum + ido
    fn_datetime()

    # timedelta - időpillanatok közti különbségek kezelésére
    fn_timedelta()

    # Péntek 13
