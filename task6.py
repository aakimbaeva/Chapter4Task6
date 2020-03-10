class House:
    def __init__(self, household_type, total_area, f1, f2, f3):
        self.household_type = household_type
        self.total_area = total_area
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.furniture_list = []
        self.furniture_list.append(f1)
        self.furniture_list.append(f2)
        self.furniture_list.append(f3)

    def furniture_area(self, area_f1, area_f2, area_f3):
        self.area_f1 = area_f1
        self.area_f2 = area_f2
        self.area_f3 = area_f3
        self.furniture_area = self.area_f1 + self.area_f2 + self.area_f3

    def remaining_area(self):
        self.remaining_area = self.total_area - self.furniture_area
        print(f'This house is {self.household_type} household type, with total area of {self.total_area} m^2 and ' \
               f'{self.remaining_area} m^2 of free area, with the list of furniture: {self.furniture_list}')


house = House('family', 125, 'bed', 'wardrobe', 'table')
house.furniture_area(12, 13, 25)
house.remaining_area()