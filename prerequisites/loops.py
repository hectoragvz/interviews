# While loops are similar
n = 1
while n < 5:
    print(n)
    n += 1

# Looping from i = 0 to i = 4
for i in range(5):  # 5 not included
    print(i)  # no needed to increment

# FIRST ARG INCLUDED; SECOND NOT (for i in range loops)

# Looping from i = 2 to i = 5
for i in range(2, 6):  # 6 not included
    print(i)  # no needed to increment

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):  # third param is step, how you go through the loop
    print(i)  # no needed to increment
