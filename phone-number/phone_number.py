class PhoneNumber:
    def __init__(self, number):
        nums = list(map(int, filter(str.isdigit, number)))

        if len(nums) < 10 or len(nums) > 11:
        	raise ValueError('Invalid number of digits')

        if len(nums) == 11:
        	if nums[0] != 1:
        		raise ValueError('International country code must be 1')
        	else:
        		nums = nums[1:]

        if nums[0] < 2:
        	raise ValueError('Area code cannot be 0 or 1')
        if nums[3] < 2:
        	raise ValueError('Exchange code cannot be 0 or 1')

        self._number = nums
        self.area_code = ''.join(map(str, nums[0:3]))
        self.number = ''.join(map(str, nums))


    def pretty(self):
    	return "("+self.number[:3]+") "+self.number[3:6]+"-"+self.number[6:]

