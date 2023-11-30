class House:
    #pass #this key world make the class run without error, and it tells us that nothing has been add to the class yet

    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self):
        print(self.num_rooms)
        pass

house = House()
print(house.num_rooms)
print(House.num_rooms)

house.num_rooms = 7
print(house.num_rooms) # 7
print(House.num_rooms) # 5

House.num_rooms = 7
print(house.num_rooms) # 7
print(House.num_rooms) # 7