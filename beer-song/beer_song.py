def recite(start, take=1):
    bottles = start
    verses = []
    for i in range(take):
    	beer_f = lambda bot : f"{bot if bot != 0 else 'No more'} bottle{'s' if  bot != 1 else ''} of beer"
    	take_string = f"Take {'one' if bottles > 1 else 'it'} down and pass it around"
    	store_string = f"Go to the store and buy some more"
    	new_bottles = bottles - 1 if bottles > 0 else 99

    	verses.append(f"{beer_f(bottles)} on the wall, {beer_f(bottles).lower()}.")
    	verses.append(f"{take_string if bottles != 0 else store_string}, {beer_f(new_bottles).lower()} on the wall.")
    	verses.append("")
    	
    	bottles = new_bottles
    return verses[:-1]

