current_movies = {
    'Inception': '11:00 AM',
    'The Matrix': '11:30 AM',
    'Interstellar': '12:00 PM',
    'Jurassic Park the rebirth': ['12:30 PM', '3:30 PM'],
    'Fantastic 4': '1:00 PM'
}
print("Current Movies and Showtimes:")
for key in current_movies:
    print(key, "at", current_movies[key])

movie = input('Which movie do you want the showtime for?\n')
if movie in current_movies:
    print(movie, 'is showing at', current_movies[movie])
else:
    print("Sorry, that movie is not currently showing.")

contacts = {
    'number' : 4,
    'students':[
        {
            'name': 'Alice',
            'age': 20,
            'email': 'alice@example.com'
        },
        {
            'name': 'Bob',
            'age': 22,
            'email': 'bob@example.com'
        },
        {
            'name': 'Charlie',
            'age': 23,
            'email': 'charlie@example.com'
        },
        {
            'name': 'David',
            'age': 21,
            'email': 'david@example.com'
        }
    ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])

partners = {}
partners['Ruby'] = 'Gyana'
partners['Sambit'] = 'Jyoti'
partners['Kunal'] = 'Ami'

input_name = input("Enter a name to find their partner:\n")
if input_name in partners:
    print(input_name + "'s partner is " + partners[input_name])
else:
    print("Partner not found.")

# ALternate way
partner = partners.get(input_name)
if(partner):
    print(input_name + "'s partner is " + partner)
else:
    print("Partner not found.")
