import random
import json

def randdom_country():
    random_number = random.randint(10,249)
    with open('country-list-with-ids.json', 'r') as file:
        data = json.load(file)
        return data[random_number]['country']

def cities_names(country_name):
    with open('country-list-with-ids.json', 'r') as file:
        data = json.load(file)

        # correct answer func
        correct_answer = ''
        for i in data:
            if i['country'] == country_name:
                correct_answer = i['capital']

        #2 random function
        new_array = []
        i = 0
        while i <= 2 :
            random_number = random.randint(1, 249)
            new_array.append(data[random_number]['capital'])
            i += 1

        #mergenig all to one array
        random_number = random.randint(0,2)
        new_array.insert(random_number, correct_answer)

        return {'array': new_array,
                'answer': correct_answer}


