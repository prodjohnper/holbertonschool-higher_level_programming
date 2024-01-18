#!/usr/bin/python3
for nums in range(0, 100):
    if nums < 99:
        print('{:02d}'.format(nums), end=", ")
    else:
        print('{}'.format(nums))
