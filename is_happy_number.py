class isHappyNumber:

    def is_happy_number(self, number):
        if number == 1:
            return True
        elif number == 4:
            return False
        self.list_num = [int(i) for i in str(number)]
        number = sum([num ** 2 for num in self.list_num])
        return self.is_happy_number(number)
