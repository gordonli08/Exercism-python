dayGifts = [
	('first','a Partridge in a Pear Tree.'),
	('second', 'two Turtle Doves'),
	('third', 'three French Hens'),
	('fourth', 'four Calling Birds'),
	('fifth', 'five Gold Rings'),
	('sixth', 'six Geese-a-Laying'),
	('seventh', 'seven Swans-a-Swimming'),
	('eighth', 'eight Maids-a-Milking'),
	('ninth', 'nine Ladies Dancing'),
	('tenth', 'ten Lords-a-Leaping'),
	('eleventh', 'eleven Pipers Piping'),
	('twelfth', 'twelve Drummers Drumming')
]

def verse(day):
	line = f'On the {dayGifts[day-1][0]} day of Christmas my true love gave to me: '
	for num in range(day-1,0, -1):
		line += f'{dayGifts[num][1]}, '

	if day != 1:
		line += 'and '
	line += dayGifts[0][1]
	return line


def recite(start_verse, end_verse):
    if start_verse > end_verse:
    	raise ValueError('Invalid verse range')
    verses = []
    for day in range(start_verse, end_verse+1):
    	verses.append(verse(day))
    return verses

