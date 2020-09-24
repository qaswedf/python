y = 3
while y > 0 :
    password = input("請輸入密碼： ")
    if password == "a123456":
        print("恭喜你猜對了")
        y = 0
    else:
        y = y - 1
        if y > 0:
            print("猜錯了哦！你還有", y, "次機會！")
        else:
            print("你沒機會了哦！")