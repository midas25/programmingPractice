
while True:
    try:
        n = input("number: ")
        if int(n):
            i = int(n)
            re1 = i%2
            re = i
            while True:
                if re1 == 0:
                    re2 = re/2
                    re = re2
                    print(re)
                    re1 = re%2
                    if re == 1:
                        break
                else:
                    re2 = re*3+1
                    re = re2
                    print(re)
                    re1 = re%2
                    if re == 1:
                        break
        else:
            continue
    except:
        print("Error: please enter a number")
        continue

