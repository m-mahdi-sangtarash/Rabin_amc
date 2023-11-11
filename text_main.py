import proj_func as pf


class Selection_Screen:
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
            task = int(input('\nChoose year: '))

        elif task == 2:
            year_num = int(input('\nEnter year number: '))
            pf.create_year(year_num)

        elif task == 3:
            exit()

class Add_income:
    amount = int(input('Amount: '))
    category = int(input('\nCategory?'
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
    month = int(input('\nenter month number: '))
    pf.add_income(amount, category, ye)
print('1.Add a income'
      '\n2.Add a cost'
      '\n3.Charts'
      '\n4.Facts and Figures'
      '\n5.Back')

task = int(input('Please enter task number: '))

#if task == 1:
