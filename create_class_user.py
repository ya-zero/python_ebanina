class User():
    def __init__(self,username,location,phone):
        self.username=username
        self.location=location
        self.phone=phone
    def __str__(self):
        return self.username
	
vasy=User('vasy','russia','+7910')
print(vasy.__dict__,type(vasy),vasy)
