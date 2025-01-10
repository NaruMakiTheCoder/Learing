print("Hello World")

#print blank line for spacing
print()
print()

print("Here is your Calendar for January 2025")

#print blank line for spacing
print()

import calendar
#create a textcalendar instance
cal = calendar.TextCalendar()
#print caldendar for January 2025
january_2025 = cal.formatmonth(2025, 1)

print(january_2025)

#print blank line for spacing
print()

print("Thanks")

input()