import random


def random_number():
    phone_list = ["136", "138", "150", "139"]
    tou = random.choice(phone_list)  # 从列表里随机取一个值
    wei = random.randrange(10000000, 99999999)  # 随机取值
    mobile = str(tou) + str(wei)  # 转化为字符串类型
    return mobile


def random_name():
    Fristname = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章"
    Secondname = "鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康"
    sanname = "伍余元卜顾孟平黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧罗毕郝邬安常乐于时傅皮卞齐康俞任袁柳"
    name1 = random.choice(Fristname)
    name2 = random.choice(Secondname)
    name3 = random.choice(sanname)
    return name1 + name2 + name3