#!/usr/bin/env python3
'''
input : 工号1（num）：工资金额（income）1     工号2（num）：工资金额（income）2……
def ：思路：1.税后工资 = 工资金额 - 各项社会保险 - 应纳税额（Tax_payable)
	                 1.1 工资金额→输入的，直接获取，用sys.argv[ ]
	                 1.2 各项社会保险（insurance）→0.165*工资金额
	                 1.3  应纳税额 （tax_payable） = 应纳税所得额（taxable_income）× 税率 － 速算扣除数  (见表格也都有）
	                           1.3.1  应纳税所得额 = 工资金额 － 各项社会保险费 - 起征点(3500元)
output： 员工号1：税后工资1(takehome_pay)  工号2（num）：工资金额2  （一行或多行）
举个栗子：工资金额为 5000，
              那么五险一金缴纳 825 元 = 5000 * 0.165
                  应纳税所得额为 675（5000-825-3500），
                  应纳税额为 20.25 元（675*%3 - 0）。
          税后工资为 4154.75（5000-825-20.25）
其他：1. int（工资金额）
      2.错误：print("Parameter Error")
      3.税后工资.00
'''
import sys

income_list = sys.argv[1:]

def tax(salary):
    insurance = 0.165 * salary
    taxable_income = salary - insurance - 3500
    tax_payable = 0
    if taxable_income < 0:
        tax_payable = 0
    elif taxable_income < 1500:
        tax_payable = taxable_income * 0.03
    elif taxable_income < 4500:
        tax_payable = (taxable_income * 0.1) - 105
    elif taxable_income < 9000:
        tax_payable = (taxable_income * 0.2) - 555
    elif taxable_income < 35000:
        tax_payable = (taxable_income * 0.25) - 1005
    elif taxable_income < 55000:
        tax_payable = (taxable_income * 0.3) - 2755
    elif taxable_income < 80000:
        tax_payable = (taxable_income * 0.35) - 5505
    else:
        tax_payable = (taxable_income * 0.450) - 13505
    return salary - insurance - tax_payable

def main():
    userdata = {}
    for i in range(len(income_list)):
        income = income_list[i].split(':')
        userdata[int(income[0])] = int(income[1])

    for num,takehome_pay in userdata.items():
        takehome_pay = tax(takehome_pay)
        print('{}:{:.2f}'.format(num, takehome_pay))

if __name__ == '__main__':
    main()
