class Clients:
    def __init__(self, firstname='', lastname='', money=0):
        self.firstname = firstname
        self.lastname = lastname
        self.money = money


class User(Clients):
    def add_user_to_dict(self, customers_dict):
        customers_dict['Имя'] = self.firstname
        customers_dict['Фамилия'] = self.lastname
        customers_dict['Баланс'] = self.money
        return customers_dict

    def get_user_from_dict(self, customers_dict):
        self.firstname = customers_dict.get('Имя')
        self.lastname = customers_dict.get('Фамилия')
        self.money = customers_dict.get('Баланс')
        return str(self.firstname), str(self.lastname), str(self.money)

