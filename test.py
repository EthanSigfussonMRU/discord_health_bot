import time


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)

print (f"{time} this is the time")