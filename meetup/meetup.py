import calendar
from datetime import date

days = dict(zip(list(calendar.day_name),range(7)))

week_dict = {
	"1st":0,
	"2nd":1,
	"3rd":2,
	"4th":3,
	"5th":4,
	"teenth":[13,14,15,16,17,18,19]
}

class MeetupDayException(Exception):
	pass

def meetup(year, month, week, day_of_week):
	dates = [day for day in calendar.Calendar().itermonthdays2(year,month) if day[0] > 0 and day[1] == days[day_of_week] ]

	if week == "last":
		return date(year, month, dates[-1][0])
	elif week == "teenth":
		for day in dates:
			if day[0] in week_dict[week]:
				return date(year, month, day[0])
	else:
		try:
			return date(year,month, dates[week_dict[week]][0])
		except Exception:
			raise MeetupDayException("Day does not exist")

		
