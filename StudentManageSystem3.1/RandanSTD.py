import random as R

tel_module = [136, 130, 158, 133, 153, 180, 181, 189, 177, 173, 149, 131, 185, 186, 175, 135, 157, 159, 187, 188, 178]


def create(start, num):
    List = []
    for i in range(num):
        name = ''.join([chr(ord('a') + R.randint(0, 25)) for i in range(6)])
        number = start + i
        sex = R.choice(['男', '女'])
        tel = str(R.choice(tel_module)) + str(R.randint(10000000, 99999999))
        age = R.randint(16, 26)
        clas = R.randint(1, num // 30)
        score = [R.randint(0, 150), R.randint(0, 150), R.randint(0, 150), R.randint(0, 100), R.randint(0, 100),
                 R.randint(0, 100), R.randint(0, 100), R.randint(0, 100), R.randint(0, 100)]
        Sum = sum(score)
        List.append([number, name, age, sex, tel, clas]+score+[Sum])

    f = open('studentInformation/information.txt', 'a+', encoding='utf-8')

    temp = [','.join(list(map(str, std))) + '\n' for std in List]
    f.writelines(temp)


create(202100001, 5000)
