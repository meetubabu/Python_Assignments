
import datetime
import pytz

tz1 = 'America/Argentina/Ushuaia'
tz2 = 'Brazil/DeNoronha'
tz3 = 'Jamaica'

str_datetime = '2019-05-15 12:00:00'
l_date_time = datetime.datetime.strptime(str_datetime,"%Y-%m-%d %H:%M:%S")

# Assign current Date to timezone

tz1_timezone=pytz.timezone(tz1)
tz1_date = tz1_timezone.localize(l_date_time)
print(tz1_timezone)
print(tz1_date.tzinfo)
print(tz1_date)

tz2_timezone=pytz.timezone(tz2)
tz2_date=tz2_timezone.localize(l_date_time)
print(tz2_timezone)
print(tz2_date.tzinfo)
print(tz2_date)

tz3_timezone=pytz.timezone(tz3)
tz3_date=tz3_timezone.localize(l_date_time)
print(tz3_timezone)
print(tz3_date.tzinfo)
print(tz3_date)
# In which timezone sun rises first
tzs=[tz1_date,tz2_date,tz3_date]
early_sun=tzs[0]
for i in tzs:
    if i <early_sun:
        early_sun=i
print("Sun first rises in :",early_sun.tzinfo)