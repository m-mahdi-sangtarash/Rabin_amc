import proj_func as pf


class text_menu:
    def __init__(self, year_num):
        self.year_num = year_num

    @staticmethod
    def selection_screen():
        year_lst = pf.year_list()
        if not year_lst:
            print('\n1.Create a new year'
                  '\n2.Quit')
            task = int(input('Please choose: '))

            if task == 1:
                year_num = int(input('Enter year number: '))
                pf.create_year(year_num)

            elif task == 2:
                exit()

        else:
            print('\n1.Choose from list'
                  '\n2.Create a new year'
                  '\n3.Quit')
            task = int(input('Please choose: '))
            if task == 1:
                on = 0
                for year in year_lst:
                    print(f'{on}.{year}')
                    on += 1

                num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                c_year = ''
                year_choice = int(input('\n\nChoose year: '))
                for i in year_lst[year_choice]:
                    if i in num_lst:
                        c_year += i
                c_year = int(c_year)
                return c_year

            elif task == 2:
                year_num = int(input('\n\nEnter year number: '))
                pf.create_year(year_num)
                return year_num

            elif task == 3:
                exit()

    @staticmethod
    def main_menu():
        print('\n\n-------------------------------------'
              '\n|1.Add income  | 2.Add Cost         |'
              '\n|3.Charts      | 4.Facts and Figures|'
              '\n-------------------------------------')
        task = int(input('\n\nEnter task number: '))
        return task

    @staticmethod
    def add_income(year_num):
        print('\n\nIf you want back to menu, press ESC on your keyboard')
        amount = int(input('Amount: '))
        category = int(input('\n\nCategory?'
                             '\n1.حقوق من'
                             '\n2.مهندسی'
                             '\n3.یارانه'
                             '\n4.وام از'
                             '\n5.قرض از'
                             '\n6.حقوق خ'
                             '\n7.اجاره'
                             '\n8.آموزشگاه'
                             '\n9.سود سپرده'
                             '\n10.فروش دارایی'
                             '\n11.سود سهام من'
                             '\n12.سود سهام خ'
                             '\n13.دریافت طلب'
                             '\n14.از بیمه'
                             '\n15.از مزرعه'
                             '\n16.امانت'
                             '\n17.خدمت'
                             '\n18.سایر'
                             '\ncategory number: '))
        month = int(input('\n\nenter month number: '))
        pf.add_income(amount, category, year_num, month)


year = text_menu.selection_screen()
while True:
    task = text_menu.main_menu()
    if task == 1:
        pass

