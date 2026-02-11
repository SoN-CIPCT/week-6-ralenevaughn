web_users = ["ralene", "dataqueen", "uw_student", "pulm_clinic", "nurse24"]
new_users = ["alan", "ralene", "nurse24", "jeanne", "andrea"]

for new_user in new_users:
    if new_user in web_users:
        print(f"Username '{new_user}' This user name is already in use. Please choose a different user name.")
    else:
        print(f"Username '{new_user}' This user name is available.")

print()
print()

print("City Information")

print()

cities = {
    "Los Angeles": {
        "Country": "United States",
        "Population": 3880000,
        "Fact": "It is known for its celebrities and experienced the worst wildfire in its history in 2025."
    }, 
    "Banjul": {
        "Country": "The Gambia",
        "Population": 31300,
        "Fact": "The city is located on St. Mary's Island at the mouth of the Gambia River."
    },
    "Madrid": {
        "Country": "Spain",
        "Population": 3480000,
        "Fact": "Madrid houses Europe's largest royal palace with 3,418 rooms."
    }
}

for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['Country']}")
    print(f"Population: {info['Population']}")
    print(f"Fact: {info['Fact']}")
    print()

    