import random
import requests

def generate_random_names(count):
    names = []
    for _ in range(count):
        name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(random.randint(3, 8)))
        names.append(name)
    return names

def check_age_range(name):
    try:
        response = requests.get(f"https://api.agify.io/?name={name}")
        data = response.json()
        age = data.get('age', None)
        if age is not None and 0 <= age <= 120:
            print(f"The age for name '{name}' is {age}, which falls within the range of 0 to 120.")
        else:
            print(f"The age for name '{name}' is not within the range of 0 to 120.")
    except Exception as e:
        print(f"Error occurred while fetching age for '{name}':", e)

if __name__ == "__main__":
    random_names = generate_random_names(3)
    for name in random_names:
        check_age_range(name)
