import time

for i in range(10):
    print(f"Hello {i}")
    time.sleep(1)

a = time.time() # Returns the current time in seconds since the epoch (January 1, 1970)
print(a)

a = time.ctime()
print(a)

x = time.strftime("%b", time.localtime())
print(x)
x = time.strftime('%H:%M:%S', time.localtime())