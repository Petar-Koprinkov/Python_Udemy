class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.followers = 0
        self.following = 0

    def follow(self, user: 'User'):
        self.following += 1
        user.followers += 1


person_1 = User('Petar', 'Koprinkov')
person_2 = User('Georgi', 'Vasilev')

person_2.follow(person_1)
print(person_1.followers)
print(person_1.following)

print(person_2.followers)
print(person_2.following)

