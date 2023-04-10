def read_file():
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def write_file():
    with open(path_file,'a',encoding='UTF-8') as f:
        f.writelines('\n'+input())

            
def find_file():
    find_info = input()
    with open(path_file,'r',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                print(line)


def change_file():
    find_info = input()
    new_info = input()
    with open(path_file,'r+',encoding='UTF-8') as f:
        for line in f:
            if find_info.casefold() in line.casefold():
                if input("Да/Нет") == "Да":
                    lst = (line.strip()).split(' ')
                    print(lst)
                else: continue



m = input("Введите что вы хотите сделать? Изменить, Вывести, Добавить, Найти: ")
if m == 'Вывести':
    def main():
        read_file()
if m == 'Добавить':
    def main():
        write_file()
if m == 'Изменить':
    def main():
        change_file()
if m == 'Найти':
    def main():
        find_file()




path_file = r'Telephonebook.txt'
if __name__ == '__main__':
    main()