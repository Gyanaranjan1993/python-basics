contacts = {
    'number' : 1,
    'students': [
        {'name': 'Alice', 'age': 20, 'email': 'alice@example.com'},
        {'name': 'Bob', 'age': 22, 'email': 'bob@example.com'},
        {'name': 'Charlie', 'age': 23, 'email': 'charlie@example.com'},
        {'name': 'David', 'age': 21, 'email': 'david@example.com'}
    ]
}

email_groups = []

for student in contacts['students']:
    email_groups.append(student['email'])

print('Student emails:')
print(email_groups)