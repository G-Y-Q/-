while True:
    name = input("请输入你的名字（输入'quit'退出）：")
    if name.lower() == 'quit':
        print("欢迎下次再来！")
        break
    print(f"你好，{name}，欢迎光临！")
    filename='guestbook.txt'
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(name + "\n")
