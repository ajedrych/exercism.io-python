class PhoneNumber:
    def __init__(self, number):
        self.number = number
        number = list(number)

        phone = []

        for i in number:
            if i.isdigit() == True:
                phone.append(i)
        
        if len(phone) < 10 or len(phone) > 11:
            raise ValueError
        
        if len(phone) == 11 and phone[0] != 1:
            raise ValueError
        else: phone[1:]

        if phone[0] < '2' or phone[3] < '2':
            raise ValueError

        self.number = ''.join([str(j) for j in phone])
        self.area_code = self.number[0:2]

    def pretty(self):
        return "(" + self.number[0:3] + ")-" + self.number[3:6] + "-" + self.number[6:]
        
