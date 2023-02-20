import sys, platform
import time

print(platform.python_version())

start_time = time.time()
b_list = list(range(10000000))
end_time = time.time()
print("Instantiation time for LIST:", end_time - start_time)

start_time = time.time()
b_tuple = tuple(range(10000000))
end_time = time.time()
print("Instantiation time for TUPLE:", end_time - start_time)

start_time = time.time()
for item in b_list:
  aa = b_list[20000]
end_time = time.time()
print("Lookup time for LIST: ", end_time - start_time)

start_time = time.time()
for item in b_tuple:
  aa = b_tuple[20000]
end_time = time.time()
print("Lookup time for TUPLE: ", end_time - start_time)