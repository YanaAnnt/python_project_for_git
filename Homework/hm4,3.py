import requests
country = "Israel"

def check_universities_count(country):
    try:
        response = requests.get(f"http://universities.hipolabs.com/search?country=Israel")
        Israel_universities = response.json()
        if len(Israel_universities) >= 5:
            print(f"There are at least 5 universities in {country}.")
        else:
            print(f"There are not enough universities in {country}.")
    except Exception as e:
        print("Error occurred while fetching universities:", e)

check_universities_count(country)