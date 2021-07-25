class PhoneNumber:
    def __init__(self, number):
        self.number = number
        number = list(number)
        phone = []

        for i in number:
            if i.isnumeric() == True:
                phone.append(i)
        # print(phone)

        if len(phone) < 10 or len(phone) > 11:
            raise ValueError("Invalid input")
        
        if len(phone) == 11 and phone[0] != '1':
            raise ValueError("Invalid input")
        if len(phone) == 11:
            phone = phone[1:]
        # print(phone)

        if phone[0] == '0' or phone[0] == '1' or phone[3] == '0' or phone[3] == '1':
            raise ValueError("Invalid input")

        self.number = "".join([str(j) for j in phone])
        self.area_code = self.number[0:3]
        # print(self.number)
        # print(self.area_code)

    def pretty(self):
        if len(self.number) == 10:
            return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
        else:
            self.number = self[1:]
            return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]

# PhoneNumber("(223) 156-7890")