import arrow
import datetime

# Jelenlegi idő
utc = arrow.utcnow()
print("utc", utc)
print("utc local", utc.to('local'))
print("utc local pacific", utc.to('local').to("US/Pacific"))
print("---")

utc = arrow.now("local")
print("arrow.now", utc)
print(utc.humanize(locale="hu_HU"))
print(arrow.now('America/New_York'))
print("---")

# Idő lekérése
ido = arrow.get("2021-03-24T17:55:27.777527+01:00")
print(ido)
print(ido.humanize(locale="hu_HU"))

ido = ido.shift(hours=-1)
print("-1 ora:", ido)
print(ido.humanize(locale="hu_HU"))
ido = ido.shift(days=-2, hours=-1, minutes=10)
print("-2 nap -1 ora -10 perc:", ido)
print(ido.humanize(locale="hu_HU"))
print(ido.humanize(locale="ko_kr"))
print(ido.humanize(granularity="minute"))
print(ido.humanize(granularity=["hour", "minute"]))
print(ido.humanize(only_distance=True, granularity=["day", "minute"]))
print(ido.format())
print(ido.timestamp())
print(arrow.get(1616425527.777527))
print(arrow.get('2013-05-05 12:30:45', 'YYYY-MM-DD HH:mm:ss'))
print(arrow.get("Tomorrow (2019-10-31) is Halloween!", "YYYY-MM-DD"))
print(arrow.get('2013-05-05  T \n   12:30:45\t123456', 'YYYY-MM-DD T HH:mm:ss S', normalize_whitespace=True))
print("type", type(ido))
print("type", type(ido.naive))
print("datetime tipus", ido.naive)
print("---")
# Datetime támogatás

print(arrow.get(datetime.datetime.utcnow()))
print(arrow.get(datetime.date(2013, 5, 5)))

print("---")
print(arrow.utcnow().span('hour'))
print(arrow.utcnow().floor('hour'))
print(arrow.utcnow().ceil('hour'))

start = datetime.datetime(2020, 4, 5, 10, 30)
end = datetime.datetime(2020, 4, 5, 16, 15)
for r in arrow.Arrow.range('hour', start, end):
    print("range", r)

karacsony = arrow.utcnow().replace(month=12, day=25)
napok_karacsonyig = (karacsony - arrow.utcnow()).days
print(f"Karácsonyig {napok_karacsonyig} nap van hátra!")
print((karacsony - arrow.utcnow()))
print(type(karacsony - arrow.utcnow()))
