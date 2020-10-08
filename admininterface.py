from client import User
users_dict = {'Имя': 'Иван', 'Фамилия': 'Петров', 'Баланс': 50}
user = User()

input_user = int(input('Нажмите 1, если хотите добавить клиента в базу, нажмите 2, если хотите вывести информацию о клиенте: \n'))


def show_and_add_users(input_user):
    if input_user == 1:
        user.lastname = input('Введите фамилию: ')
        user.firstname = input('Введите имя: ')
        user.money = int(input('Текущий баланс?: '))
        return user.add_user_to_dict(users_dict)
    else:
        name = input('Введите фамилию: ')
        for key, value in users_dict.items():
            if users_dict[key] == name:
                print('Клиент:', users_dict['Имя'], users_dict['Фамилия'], 'Баланс:', users_dict['Баланс'], 'руб.')


print(show_and_add_users(input_user))




