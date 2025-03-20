class Detials():
    name ="Dipak"
    phone = 9840034579
    cast = "Basnet"

    def __str__(self):
        return f"{self.name} {self.cast} phone number is {self.phone}"

greet = Detials()
greet.name = "Fadindra"

print(greet)