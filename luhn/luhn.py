class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        if len(self.card_num) < 2 or not self.card_num.isnumeric():
            return False
        
        list_nums = [int(num) for num in self.card_num if num.isnumeric()]
        list_nums.reverse()

        for index, num in enumerate(list_nums):
            if index%2 == 1:
                list_nums[index] = num*2-9 if num*2 > 9 else num*2
        
        return sum(list_nums)%10 == 0
