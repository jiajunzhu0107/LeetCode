
class Company:
    def __init__(self, name, initials, start_range, end_range):
        self.name = name
        self.initials = set(initials)
        self.start_range = start_range
        self.end_range = end_range
    
    def isContainerBelongs(self, containerNo):
        # length = len(containerNo)
        # if length < self.start_range or length > self.end_range+1:
        #     return False
        init = ''
        for i in range(len(containerNo)):
            if not containerNo[i].isalpha():
                init = containerNo[:i]
                break
        if init not in self.initials:
            return False
        
        len_nums = len(containerNo) - len(init)
        return self.start_range <= len_nums <= self.end_range


COMPANY_LIST = [
    Company(name="STARK", initials=["MCU"], start_range=3, end_range=9),
    Company(name="COSCO", initials=["COS"], start_range=3, end_range=9),
    Company(name="LASCO", initials=["LAS"], start_range=5, end_range=11)
]




def detect_container(containerNos):
    res = []
    for containerNo in containerNos:
        # print(len(containerNo))
        for company in COMPANY_LIST:
            if company.isContainerBelongs(containerNo):
                res.append(company.name)
                break
    # print(res)
    return res
# if __name__ == "__main__":

#     # obj = Company(name="STARK", initials=["MCU"], start_range=3, end_range=9)
#     # res = obj.isContainerBelongs('MC123456')
#     # print(res)
#     res = getCompany()
COMPANY_LIST = [Company(name="STARK", initials=["MCU"], start_range=3, end_range=9),
                Company(name="COSCO", initials=["COS"], start_range=3, end_range=9),
                Company(name="LASCO", initials=["LAS"], start_range=5, end_range=11),
                Company(name="DASCO", initials=["DAS"], start_range=3, end_range=15),
                Company(name="PASCO", initials=["PAS","PASDE"], start_range=6, end_range=13),
                Company(name="STARK", initials=["MCU"], start_range=3, end_range=9),
                Company(name="LOSCO", initials=["LOS"], start_range=4, end_range=10),
                Company(name="LOSCOPARENT", initials=["LOS"], start_range=8, end_range=15),
                ]

# 3,4,,8,9
if __name__ == '__main__':
    # res = detect_container(["LOS34324234"])
    # print(res)
    assert detect_container(["MCU123458323",
                             "COS123458910", 
                             "LAS12345891011", 
                             "DAS12345891011",
                             "PAS1234583232",
                             "PASDE123458323", #"PASDE"
                             "GRE1234583232",
                             "GREEK458910",
                             "GREE3123213",
                             "LOS123454",
                             "LOS34324234"]) == ['STARK', 'COSCO', 'LASCO', 'DASCO',
                                                 'PASCO', 'PASCO', 'LOSCO', 'LOSCO']
#['STARK', 'COSCO', 'LASCO', 'DASCO', 'PASCO', 'LOSCO', 'LOSCO']