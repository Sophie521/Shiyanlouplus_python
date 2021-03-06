import sys
import csv

class Config(object):

    def __init__(self,configfile):
        self._config = {}

        with open(configfile,'r') as file:
            for line in file:
                tmp = line.split('=')
                self._config[tmp[0].strip()] = float(tmp[1].strip())

    def get_config(self, name):
        args = sys.argv[1:]
        index_c = args.index('-c')
        index_d = args.index('-d')
        index_o = args.index('-o')
        configfile = args[index_c + 1]
        userdata = args[index_d + 1]
        outfile = args[index_o + 1]
        return self.get_config(name)

class UserData(object):
    def __init__(self,userdatafile):
        self.userdata = {}
        with open(userdatafile, 'r') as file:
            for line in file:
                tmp = line.split(',')
                self.userdata[tmp[0].strip()] = float(tmp[1].strip())

    def dumptofile(self,configfile,outfile):
        with open(outfile,'a') as file:
            write = csv.writer(file)
            write.writerows(outfile)

class Calculator(object):
    def taxpayable(self,salary,insurance):
        taxable_income = salary - float(insurance) - 3500
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

    def min_max(self,num, salary,sum_rate):
        min_insurance = Config.get_config('JiShuL')
        max_insurance = Config.get_config('JiShuH')
        for num, salary in UserData.userdata.items():  #!!userdata
            if salary < min_insurance:
                insurance = min_insurance * sum_rate()
            elif salary > max_insurance:
                insurance = max_insurance * sum_rate
            else:
                insurance = salary * sum_rate
            return insurance

    def sum_rate(self):
        rate_name = ['YangLao', 'YiLiao', 'ShiYe', 'GongShang', 'ShengYu', 'GonJiJin']
        sum_rate = 0
        for i in rate_name:
            sum_rate = Config.get_config(i) + sum_rate
        return sum_rate               # 理论上返回0.165

    def final_salary(self,salary):
        insurance = self.min_max(salary)
        tax_payable = self.taxpayable(salary)
        final_salary = salary - insurance - tax_payable

        return final_salary

        output = "{},{},{:.2f},{:.2f},{:.2f}".format(num, salary, insurance, tax_payable, final_salary)
        print(output)

if __name__ == '__main__':
    Config(configfile=())











