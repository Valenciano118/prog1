import time

for i in range(101):                        # for 0 to 100
    s = str(i) + '%'                        # string for output
    print('{0}\r'.format(s))        # just print and flush

    time.sleep(0.2)