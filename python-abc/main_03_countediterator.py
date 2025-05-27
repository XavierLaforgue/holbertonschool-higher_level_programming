#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")


counted_iter = CountedIterator([-2, 3, 6, 10, "hellpo", "bye"])
for i in counted_iter:
    print(i)
counter_final = counted_iter.get_count()
print(counter_final)
