# Math Example

import math
import random

number = 5.7
print("Rounded:", round(number))  
print("Square root:", math.sqrt(25))  


print("Random number between 0 and 1:", random.random()) 


random_number = random.randint(1, 10)
print("Random number between 1 and 10:", random_number)



# Date & Time Example


from datetime import datetime

now = datetime.now()
print ("Current Date:", now.strftime("%Y-%m-%d "))
print ("Current Time:", now.strftime("%H:%M:%S"))

formatted_date = now.strftime("%Y-%m-%d")

print("Today is:", formatted_date)