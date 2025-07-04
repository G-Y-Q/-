while True:
    reason = input("请写下你喜欢编程的原因（输入'quit'退出）：")
    if reason.lower() == 'quit':
        print("欢迎下次再来！")
        break
    print(f"感谢你的反馈！")

    filename='reason_book.txt'
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(reason + "\n")
