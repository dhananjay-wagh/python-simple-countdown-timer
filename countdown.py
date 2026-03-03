import time

my_time = int(input("Enter the countdwon Duration : "))

#Method 1 (simple one)
# for x in range( 0 , my_time):
#     print(x)
#     time.sleep(1)

#Method 2 (Reversed)
# for x in range( my_time , 0 , -1):
#     print(x)
#     time.sleep(1)

#Method 1 (Reversed with reverses function)
for x in reversed(range( 0 , my_time)):
    print(x)
    time.sleep(1)

print("Times up!!")