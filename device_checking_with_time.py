import time
from collections import deque

my_list = ["iphone", "android", "radio", "tv", "tablet", "pc", "laptop", "plate", "mouse", "bag", "phone"]

my_deque = deque(my_list)

name = input().lower()

start_time = time.time()
available = name in my_deque
end_time = time.time()

if available:
    print(f"'{name}' is in the list.")
    print(f"Time: {end_time - start_time:.2f} seconds")
else:
    print(f"'{name}' is not in the list.")