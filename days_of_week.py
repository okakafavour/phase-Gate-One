print('Enter from 1 - 6 to choose enter the days of the week ')
print("""
	S/N				DAYS OF THE WEEK
	1.					MONDAY
	2.					TUESDAY
	3.					WENSDAY
	4.					THURSDAY
	5.					FRIDAY
	6.					SATURDAY
	""")
todays_day = 0
number_of_days_elapsed = 0 
    
todays_day = int(input('Enter todays day: '))
            
number_of_days_elapsed = int(input('Enter number of days elapsed since today: '))

future_days = (todays_day + number_of_days_elapsed)
		print('Today is' + todays_day + 'and the future day is' + future_days) 
