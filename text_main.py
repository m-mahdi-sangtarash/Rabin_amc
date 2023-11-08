import proj_func as pf


class Selection_Screen():




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

print('1.Add a income'
      '\n2.Add a cost'
      '\n3.Charts'
      '\n4.Facts and Figures'
      '\n5.Back')

task = int(input('Please enter task number: '))

if task == 1:
