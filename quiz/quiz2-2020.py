"""
----------------------------------------------------------------------
Q1. complete the following function
----------------------------------------------------------------------
"""

def is_increasing(data):
    """
    data: a list of numbers
    Returns True if the list is currently sorted in **strictly** increasing order.
    Returns False otherwise
    """
    for i in range(len(data)-1):
        if not data[i] < data[i+1]:
            return False
    return True


# Uncomment the following lines to test
data_1 = [3, 4, 2020]
data_2 = [2020, 3, 4]
data_3 = [3, 3, 2020]
print(is_increasing(data_1))
print(is_increasing(data_2))
print(is_increasing(data_3))

## Expected output:
## True
## False
## False


"""
----------------------------------------------------------------------
Q2. Below are all you names in a string. Please complete the function 
to run a simulation of 100 times of class cold-callings. In this 
simulation, every student has equal chance to be called. This function 
should return a dictionary that records how many times each student
gets called. Please do not change any code outside function.
----------------------------------------------------------------------
"""

import random


random.seed(42)
NAMES_STRING = 'Alvie, Christian, Catherine, Daniel, Eli, Andrew, Grace, Kenzi, Ivy, Lucas, Ray, Nathan, Rumeer, Sean, Takaki, Rachel, Angela, Queenie, Zoe'


def call_simulation(names, num_of_calls):
    """
    names: a string that contains all the names separated by commas
    num_of_calls: total times of cold-calls in the simulation.

    Returns a dictionary of name: positive integer pairs
    """
    call_record = {}
    name_list = NAMES_STRING.split(',')

    for i in range(num_of_calls):
        random_num = random.randint(0, len(name_list)-1)
        call_record[name_list[random_num]] = call_record.get(name_list[random_num], 0) + 1
    
    return call_record


# When you've completed your function, uncomment the
# following lines and run this file to test!


print(call_simulation(NAMES_STRING, 100))
## Expected output:
## {'Daniel': 6, 'Alvie': 4, 'Ivy': 10, 'Kenzi': 10, 'Eli': 4, 'Queenie': 9, 'Catherine': 8, 'Zoe': 4, 'Sean': 3, 'Christian': 5, 'Grace': 7, 'Angela': 1, 'Takaki': 5, 'Andrew': 4, 'Ray': 5, 'Rumeer': 6, 'Nathan': 6, 'Lucas': 2, 'Rachel': 1}


"""
----------------------------------------------------------------------
Q3. Please complete the following function
----------------------------------------------------------------------
"""

random.seed(42)


def print_hist(data):
    """
    given a dictionary of name: positive integer pairs,
    prints rows with the name and a number of asterisks equal
    to the positive integer. The rows should be printed in key order.
    No return is required.
    """
    for name, times in data.items():
        asterisks = '*' * times
        print(f'{name}: {asterisks}')


# When you've completed your function, uncomment the
# following lines and run this file to test!

roster_dict = call_simulation(NAMES_STRING, 100)
print_hist(roster_dict)

## Expected output:
# Daniel: ******
# Alvie: ****
# Ivy: **********
# Kenzi: **********
# Eli: ****
# Queenie: *********
# Catherine: ********
# Zoe: ****
# Sean: ***
# Christian: *****
# Grace: *******
# Angela: *
# Takaki: *****
# Andrew: ****
# Ray: *****
# Rumeer: ******
# Nathan: ******
# Lucas: **
# Rachel: *



"""
----------------------------------------------------------------------
Q4. Please complete the following function to use your APIKEY to 
get current temperature (in Fahrenheit) from openweathermap.org.

If you don't have YOUR_OWN_APIKEY, you can use the APIKEY below,
but you will lose 5 points.

APIKEY = '8f62260aa7890d58d9a026e2810341ea'
----------------------------------------------------------------------
"""
import urllib.request
import json

def get_current_temp():
    """
    Returns current temperature in Fahrenheit from api.openweathermap.org
    """
    APIKEY = '43b7b31bfa9915b964c7a70e92866b94' 
    city = 'Wellesley'
    country_code = 'us'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&APPID={APIKEY}'

    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)

    kelvin = response_data['main']['temp']
    fahrenheit = (kelvin - 273) * 1.8 + 32
    
    return fahrenheit

# When you've completed your function, uncomment the
# following lines and run this file to test!

print(get_current_temp())

## Expected output:
## maybe 60?
