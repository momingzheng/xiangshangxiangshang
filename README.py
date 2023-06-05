import time

def timer(mins):
    for i in range(mins*60, -1, -1):
        mins, secs = divmod(i, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)

while True:
    print("开始工作!")
    timer(25)
    print("开始休息!")
    timer(5)
