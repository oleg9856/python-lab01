if __name__ == '__main__':
    while True:
        print('Do you want to continue?')
        s = input()
        if s == 'no':
            break
        elif s == 'yes':
            list = []
            for i in range(3):
                print('Please input:')
                list.insert(i, str(input()))

            if len(list) > 3:
                continue

            if list[1] == '/':
                print(float(list[0]) / float(list[2]))
                continue
            elif list[1] == '*':
                print(float(list[0]) * float(list[2]))
                continue
            elif list[1] == '+':
                print(float(list[0]) + float(list[2]))
                continue
            elif list[1] == '-':
                print(float(list[0]) - float(list[2]))
                continue
            else:
                print('There is no such operation!')

