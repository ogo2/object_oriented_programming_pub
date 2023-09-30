import pandas as pd

class Col:
    
    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport
        
    def colors(self):
        print(name, surname, passport)
        excel_bank = pd.DataFrame({'Имя':[self.name],
                                   'Фамилия':[self.surname],
                                   'Пасспорт':[self.passport]})
        print(excel_bank)
        excel_bank.to_excel('bank_info2.xlsx', sheet_name='Банковский аккаунт', index=False)

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
passport = input('Введите данные вашего пасспорта: ')

c = Col(name, surname, passport)

c.colors()
    

if __name__=='__main__':
    print('Запущена сама по себе')
    
else:
    print('Меня импортировали')