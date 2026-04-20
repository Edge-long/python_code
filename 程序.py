from pathlib import Path
import json

path = Path('username.json')
if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"欢迎回来{username}")
else:
    username = input("你的名字是？")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"程序记住你的名字叫{username}了。")

mood_index = int(input("请问要执行的程序是: 1BMI 2二元一次 3平均值 4除法运算 5读取字符"))
if mood_index <= 1:
    try:
        user_weight = float(input("请输入您的体重 (单位: kg) : "))
        user_height = float(input("请输入您的身高 (单位: m) : "))
        user_BMI = user_weight / (user_height) ** 2
    except:
        print("发生未知错误,请重新运行程序。")
    else:
        print("您的BMI值为: " + str(user_BMI))
    finally:
        print("程序运行结束")
    if user_BMI <= 18.5:
        print("此BMI值属于偏瘦范围。")
    elif 18.5 < user_BMI <= 25:
        print("此BMI值属于正常范围。")
    elif 25 < user_BMI <=30:
        print("此BMI值属于偏胖范围。")
    else:
        print("此BMI值属于肥胖范围。")
elif 1 < mood_index <= 2:
    print("我是一个根据公式法求一元二次方程的程序")
    import math
    a = input("请输入a的值")
    b = input("请输入b的值")
    c = input("请输入c的值")
    print((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    print((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
elif 2 < mood_index <= 3:
    print("我是一个求平均值的程序")
    total = 0
    count = 0
    user_input = input("请输入数字 (完成所有数字输入后，请输入q终止程序): ")
    while user_input != "q":
        num = float(user_input)
        total += num
        count += 1
        if count == 0:
            result = 0
        else:
            result = total / count
        user_input = input("请输入数字 (完成所有数字输入后，请输入q终止程序): ")
    result = total / count
    print("您输入的数字平均值为" + str(result))
elif 3 < mood_index <= 4:
    print("这是一个只执行除法运算的程序")
    print("输入'q'终止程序")
    while True:
        first_number = input("\n被除数")
        if first_number == 'q':
            break
        second_number = input("除数")
        if first_number == 'q':
            break
        try:
            anwser = int(first_number) / int(second_number)
        except ZeroDivisionError:
            print("你不能除零")
        else:
            print(anwser)
else:
    from pathlib import Path
    def count_words(path):
        try:
            contents = path.read_text(encoding='utf-8')
        except FileNotFoundError:
            print("抱歉,您提供的文件路径无效")
        else:
            words = contents.split()
            num_words = len(words)
            print(f"文本文件{path}包含{num_words}个字符")

    path = Path(input("请输入文本文件路径"))
    count_words(path)