import sys
import clipboard

secCount = 0  # initial value

# get seonds count from cmd or user input
if len(sys.argv) > 1:
    try:
        secCount = int(sys.argv[1])
    except ValueError:
        print("Input is not a number")
else:
    secCount = int(input("enter number of second\n"))

# convert seconds count to format hh:mm:ss
if secCount < 3600:
    minutes = secCount // 60
    seconds = secCount % 60
    time = "%d:%02d" % (minutes, seconds)
else:
    hours = secCount // 3600
    minutes = (secCount - 3600*(secCount // 3600)) // 60
    seconds = (secCount - 3600*(secCount // 3600)) % 60
    time = "%d:%02d:%02d" % (hours, minutes, seconds)

print(time)
clipboard.copy(time)
