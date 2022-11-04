#enter seconds for days, hours, minutes, seconds
seconds = int(input("Enter your seconds: "))

#actions
day = seconds % (24 * 3600)
hour = day // 3600
day %= 3600
min = day // 60
day %= 60
sec = day % 60 

#result
print(str(day) + " days " + str(hour) + ":" + str(min) + ":" + str(sec)) 