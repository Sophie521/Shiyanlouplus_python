import sys
import csv

class Config(object):

    def __init__(self,configfile):
        self._config = {}
        self.args = sys.argv[1:]
        index_c = args.index('-c')
        index_d = args.index('-d')
        index_o = args.index('-o')
        configfile = args[index_c + 1]
        userfile = args[index_d + 1]
        outfile = args[index_o + 1]

        with open(configfile,'r') as file:
            for line in file:
                key = line.split('=').[0].strip()
                name = line.split('=').[1].strip()

    def get_config(self, name):
        return self.config[name]

class UserData(object):
    def __init__(self, userdatafile):
            self.userdata = []

            with open('user.csv', 'r') as file:
                for line in file:
                    num = line.split(',')[0].strip()
                    salary = line.split(',')[1].strip()
                    self.userdata[] = salary

    def calculat(taor(self):
        def tax(salary):
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
            return tax_payable

        def min_max(num, salary):
            min_insurance = config.get_config('JiShuL')
            max_insurance = config.get_config('JiShuH')
            for num, salary in self.userdata.items():
                if salary < min_insurance:
                    insurance = min_insurance * sum_rate
                elif salary > max_insurance:
                    insurance = max_insurance * sum_rate
                else:
                    insurance = salary * sum_rate

        def sum_rate(self):
            rate_name = ['YangLao', 'YiLiao', 'ShiYe', 'GongShang', 'ShengYu', 'GonJiJin']
            sum_rate = 0
            for i in rate_name:
                sum_rate = self.get_config(i) + sum_rate
            return sum_rate  # 0.165

        def final_salary(salary):
            insurance = min_max(salary)
            tax_payable = tax(salary)
            final_salary = salary - insurance - tax_payable
            return final_salary

        output = "{},{},{:.2f},{:.2f},{:.2f}".format(num, salary, insurance, tax_payable, final_salary)

    def dumptofile(self, outputself):
            with open('./gongzi.csv', 'w') as file:
                file.write(output)

if __name__ == '__main__':
        UserData(userfile).calculator()
        UserData(userfile).dupmtofile(outfile)