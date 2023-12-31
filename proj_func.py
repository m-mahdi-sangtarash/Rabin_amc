import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xlsxwriter as xw


def create_sheet(exl, month):
    col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    col_onest = ['E', 'F', 'G', 'H', 'I', 'J']

    # For create excel files
    month_row_title = ['incomes', 'incomes_per', 'costs', 'costs_per', 'month_tot_income', 'month_tot_cost',
                       'left_over_before', 'left_over_month', 'left_over_tot', 'adjust']

    worksheet = exl.add_worksheet(month)
    sub = 0
    for k in col:
        worksheet.write(f'{k}1', month_row_title[sub])
        sub += 1

    for row in range(2, 20):
        worksheet.write(f'A{row}', 0)
        worksheet.write(f'B{row}', 0)

    for row in range(2, 21):
        worksheet.write(f'C{row}', 0)
        worksheet.write(f'D{row}', 0)

    for colms in col_onest:
        worksheet.write(f'{colms}2', 0)


def total_sheet(exl):
    worksheet = exl.add_worksheet('total')
    tot_category = ['incomes_total', 'incomes_tot_per', 'incomes_mean', 'incomes_mean_per', 'costs_total',
                    'costs_tot_per', 'costs_mean', 'cost_mean_per', 'year_tot_income',
                    'year_tot_cost', 'left_over_year', 'lo_before', 'total_left_over']

    col = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    col_onest = ['I', 'J', 'K', 'L', 'M']
    sub = 0

    for k in col:
        worksheet.write(f'{k}1', tot_category[sub])
        sub += 1

    for row in range(2, 20):
        worksheet.write(f'A{row}', 0)
        worksheet.write(f'B{row}', 0)
        worksheet.write(f'C{row}', 0)
        worksheet.write(f'D{row}', 0)

    for row in range(2, 21):
        worksheet.write(f'E{row}', 0)
        worksheet.write(f'F{row}', 0)
        worksheet.write(f'G{row}', 0)
        worksheet.write(f'H{row}', 0)

    for colms in col_onest:
        worksheet.write(f'{colms}2', 0)


def create_year(year_num):
    file = f'year_data/year-{year_num}.xlsx'
    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    exl = xw.Workbook(file)
    for m in month:
        create_sheet(exl, m)

    total_sheet(exl)
    exl.close()


def year_list():
    os_lst = os.listdir('year_data')
    return os_lst


def mean_cal_year(year_num):
    dataframe = pd.read_excel(f'year_data/year-{year_num}.xlsx',
                              sheet_name=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'total'])

    month = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    categor = ['incomes', 'costs']
    per_categor = ['incomes_mean_per', 'cost_mean_per']
    info = []
    total = 0
    sheet = dataframe['total']

    for cat in categor:
        for row in range(0, 19):
            for month_check in month:
                try:
                    info.append(dataframe[month_check][cat][row])
                except ValueError or KeyError:
                    continue
                for collector in info:
                    total += collector

                if cat == 'incomes':
                    sheet.iloc[row, sheet.columns.get_loc("year_tot_income")] = total
                    sheet.iloc[row, sheet.columns.get_loc("incomes_mean")] = (total / len(info))

                else:
                    sheet.iloc[row, sheet.columns.get_loc("year_tot_cost")] = total
                    sheet.iloc[row, sheet.columns.get_loc("costs_mean")] = (total / len(info))

            info = []
            total = 0

    for per_categ in per_categor:
        for row in range(0, 19):
            try:
                info.append(dataframe['total'][per_categ][row])
            except ValueError or KeyError:
                continue
        for collector in info:
            total += collector

        if per_categ == 'incomes_mean_per':
            sheet.iloc[row, sheet.columns.get_loc("incomes_mean_per")] = (
                (sheet.iloc[row, sheet.columns.get_loc("incomes_mean")] / total))
            sheet.iloc[row, sheet.columns.get_loc("incomes_mean_per")] = (total / len(info))

        else:
            sheet.iloc[row, sheet.columns.get_loc("year_tot_cost")] = total
            sheet.iloc[row, sheet.columns.get_loc("costs_mean")] = (total / len(info))

        info = []
        total = 0


def mean_cal_fh_year(year_num):
    dataframe = pd.read_excel(f'year_data/year-{year_num}.xlsx', sheet_name=['1', '2', '3', '4', '5', '6'])
    month = ['1', '2', '3', '4', '5', '6']
    categor = ['incomes', 'costs']
    per_categor = ['incomes_mean_per', 'cost_mean_per']
    info = []
    total = 0
    sheet = dataframe['total']
    for cat in categor:
        for row in range(0, 19):
            for month_check in month:
                try:
                    info.append(dataframe[month_check][cat][row])
                except ValueError or KeyError:
                    continue
                for collector in info:
                    total += collector

                if cat == 'incomes':
                    sheet.iloc[row, sheet.columns.get_loc("year_tot_income")] = total
                    sheet.iloc[row, sheet.columns.get_loc("incomes_mean")] = (total / len(info))

                else:
                    sheet.iloc[row, sheet.columns.get_loc("year_tot_cost")] = total
                    sheet.iloc[row, sheet.columns.get_loc("costs_mean")] = (total / len(info))

    for per_categ in per_categor:
        for row in range(0, 19):
            try:
                info.append(dataframe['total'][per_categ][row])
            except ValueError or KeyError:
                continue
        for collector in info:
            total += collector

        if per_categ == 'incomes_mean_per':
            sheet.iloc[row, sheet.columns.get_loc("fh_incomes_mean_per")] = (
                (sheet.iloc[row, sheet.columns.get_loc("fh_incomes_mean")] / total))
            sheet.iloc[row, sheet.columns.get_loc("fh_incomes_mean_per")] = (total / len(info))

        else:
            sheet.iloc[row, sheet.columns.get_loc("fh_year_tot_cost")] = total
            sheet.iloc[row, sheet.columns.get_loc("fh_costs_mean")] = (total / len(info))


def create_month_plot():
    my_salary_list = []
    eng_income_list = []
    subsidy_list = []
    loan_from_list = []
    borrowed_from_list = []
    salary_mrs_list = []
    rent_list = []
    edu_inst_in_list = []
    interest_list = []
    asset_list = []
    sale_list = []
    my_dividend_list = []
    ms_dividend_list = []
    rec_request_list = []
    insurance_list = []
    farm_income_list = []
    trust_list = []
    service_list = []
    equ_inter_3_list = []
    month_lst = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    for month_count in range(1, 13):
        data = pd.read_excel('year_data/year-1401.xlsx', f'{month_count}')
        my_salary_list.append(data['income'][0])
        eng_income_list.append(data['income'][1])
        subsidy_list.append(data['income'][2])
        loan_from_list.append(data['income'][3])
        borrowed_from_list.append(data['income'][4])
        salary_mrs_list.append(data['income'][5])
        rent_list.append(data['income'][6])
        edu_inst_in_list.append(data['income'][7])
        interest_list.append(data['income'][8])
        asset_list.append(data['income'][9])
        sale_list.append(data['income'][10])
        ms_dividend_list.append(data['income'][11])
        rec_request_list.append(data['income'][12])
        my_dividend_list.append(data['income'][13])
        insurance_list.append(data['income'][14])
        farm_income_list.append(data['income'][15])
        trust_list.append(data['income'][16])
        service_list.append(data['income'][17])
        equ_inter_3_list.append(data['income'][18])

    my_salary_list = np.array(my_salary_list)
    eng_income_list = np.array(eng_income_list)
    subsidy_list = np.array(subsidy_list)
    loan_from_list = np.array(loan_from_list)
    borrowed_from_list = np.array(borrowed_from_list)
    salary_mrs_list = np.array(salary_mrs_list)
    rent_list = np.array(rent_list)
    edu_inst_in_list = np.array(edu_inst_in_list)
    interest_list = np.array(interest_list)
    asset_list = np.array(asset_list)
    sale_list = np.array(sale_list)
    ms_dividend_list = np.array(ms_dividend_list)
    rec_request_list = np.array(rec_request_list)
    my_dividend_list = np.array(my_dividend_list)
    insurance_list = np.array(insurance_list)
    farm_income_list = np.array(farm_income_list)
    trust_list = np.array(trust_list)
    service_list = np.array(service_list)
    equ_inter_3_list = np.array(equ_inter_3_list)

    plt.plot(month_lst, my_salary_list, label='my salary', marker='o')
    plt.plot(month_lst, eng_income_list, label='eng income', marker='o')
    plt.plot(month_lst, subsidy_list, label='subsidy', marker='o')
    plt.plot(month_lst, loan_from_list, label='loan from', marker='o')
    plt.plot(month_lst, borrowed_from_list, label='borrowed from', marker='o')
    plt.plot(month_lst, salary_mrs_list, label='salary mrs', marker='o')
    plt.plot(month_lst, loan_from_list, label='loan from', marker='o')
    plt.plot(month_lst, rent_list, label='rent', marker='o')
    plt.plot(month_lst, edu_inst_in_list, label='edu inst in', marker='o')
    plt.plot(month_lst, interest_list, label='interest', marker='o')
    plt.plot(month_lst, asset_list, label='asset', marker='o')
    plt.plot(month_lst, sale_list, label='sale', marker='o')
    plt.plot(month_lst, ms_dividend_list, label='ms dividend', marker='o')
    plt.plot(month_lst, rec_request_list, label='rec request', marker='o')
    plt.plot(month_lst, my_dividend_list, label='my dividend', marker='o')
    plt.plot(month_lst, insurance_list, label='insurance', marker='o')
    plt.plot(month_lst, farm_income_list, label='farm income', marker='o')
    plt.plot(month_lst, trust_list, label='trust', marker='o')
    plt.plot(month_lst, service_list, label='service', marker='o')
    plt.plot(month_lst, equ_inter_3_list, label='equ inter 3', marker='o')
    plt.legend()
    plt.show()


def percent_year():
    pass


def add_income(amount, category_num, year_num, month_num):
    dataframe = pd.read_excel(f'year_data/year-{year_num}.xlsx',
                              sheet_name=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'total'])
    sheet = dataframe[f'{month_num}']
    sheet.iloc[category_num, sheet.columns.get_loc("incomes")] = amount
def add_cost(amount, category_num, year_num, month_num):
    dataframe = pd.read_excel(f'year_data/year-{year_num}.xlsx',
                              sheet_name=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 'total'])
