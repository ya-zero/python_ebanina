class User():

    def __init__(self, location: str, phone: str, username: str = "Noname"):
        self.username = username
        self.location = location
        self.phone = phone

    def __str__(self) -> str:
        return f'{type(self).__name__}.{self.username}'


vasy = User(location='russia', phone='+7910')
print('magic metod: %s \ntype: %s\nstr method class: %s' %
      (vasy.__dict__, type(vasy), vasy))

# from dataclasses import dataclass
# @dataclass
# class Book:
#     title: str
#     author: str
# mybook = Book('1984', 'George Orwell')
# print(mybook.__dict__,mybook)
