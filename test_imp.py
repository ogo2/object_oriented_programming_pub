import pandas as pd

class Client_bank:
    
    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport
        
    def add_client(self):
        excel_read = pd.read_excel('bank_info2.xlsx', sheet_name='Банковский аккаунт')
        lol = [[self.name, self.surname, self.passport]]
        excel_read.loc[len(excel_read)] = [self.name, self.surname, self.passport]
        print(excel_read)
        excel_read.to_excel('bank_info2.xlsx', sheet_name='Банковский аккаунт', index=False)
    
        
        
def input_user():
    name = input('Введите ваше имя: ')
    surname = input('Введите вашу фамилию: ')
    passport = int(input('Введите серию и номер вашего паспорта: '))
    c = Client_bank(name, surname, passport)
    c.add_client()
    print('Поздравляю, данные успешно добавлены в таблицу')
    
# c = Client_bank('sddsds', 'dsdsds', 'dsdsdsds')
# c.check_client_db()
    
try:
    input_user()
except ValueError:
    print('Серия и номер паспорта состоят из цифр......')
    input_user()


if __name__=='__main__':
    print('Запущена сама по себе')
    
else:
    print('Меня импортировали')