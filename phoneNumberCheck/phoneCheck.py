import re

phone1 = 13493670040
phone2 = "15693673123"
phone3 = "17793670870"

MOBILE = re.compile('^1(3[0-9]|4[57]|5[0-35-9]|7[0135678]|8[0-9])\\d{8}')  #是否为手机号码
CM = re.compile('^1(3[4-9]|4[7]|5[0-27-9]|7[08]|8[2-478])\\d{8}')  #中国移动
CU = re.compile('^1(3[0-2]|4[5]|5[56]|7[0156]|8[56])\\d{8}')   #中国联通
CT = re.compile('^1(3[3]|4[9]|53|7[037]|8[019])\\d{8}')   #中国电信

def match(ph):

    #如果号码是数字格式
    ph = str(ph)

    #长度必须是11位
    if len(ph) != 11:
        print(ph+"length is error!")
        return 0

    phonematch = MOBILE.match(ph)
    #判断是否为正常手机号码
    if phonematch:
        operatormatch1 = CM.match(ph)
        operatormatch2 = CU.match(ph)
        operatormatch3 = CT.match(ph)

        if operatormatch1:
            print(operatormatch1.group()+'是中国移动用户')
            return 1

        elif operatormatch2:
            print(operatormatch2.group()+'是中国联通用户')
            return 2

        elif operatormatch3:
            print(operatormatch3.group()+'是中国电信用户')
            return 3

    else:
        print("phone number is error!")
        return 0

match(phone3)
match(phone1)
match(phone2)