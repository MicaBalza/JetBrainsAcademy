import math
import argparse


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--type', type=str, default='')
    parser.add_argument('--payment', type=int, default=0)
    parser.add_argument('--principal', type=int, default=0)
    parser.add_argument('--periods', type=int, default=0)
    parser.add_argument('--interest', type=float, default=0.0)
    args = parser.parse_args()
    t = args.type
    principal = args.principal
    payment = args.payment
    interest = args.interest
    periods = args.periods
    if t not in ['annuity', 'diff']:
        return 0
    elif t == 'diff' and payment is True:
        return 0
    elif principal < 0 or payment < 0 or periods < 0 or interest <= 0:
        return 0
    else:
        return args


class CreditCalc:

    def __init__(self, t, principal, payment, periods, interest):
        self.type = t
        self.credit_principal = principal
        self.monthly_payment = payment
        self.count_period = periods
        self.interest = interest
        self.nominal_i = 0
        self.action = ''
        self.payments_record = 0

    def get_action(self):
        self.calc_nominal_interest()
        if self.monthly_payment and self.count_period:
            self.calc_credit_principal()
        elif self.credit_principal and self.count_period:
            self.calc_monthly_payment()
        elif self.monthly_payment and self.credit_principal:
            self.calc_count_periods()
        self.calc_overpayment()

    def calc_diff_payment(self):
        self.calc_nominal_interest()
        for m in range(1, self.count_period + 1):
            diff_payment = (self.credit_principal / self.count_period) + (self.nominal_i * (
                    self.credit_principal - ((self.credit_principal * (m - 1)) / self.count_period)))
            self.payments_record += math.ceil(diff_payment)
            print(f"Month {m}: paid out {math.ceil(diff_payment)}")
        print()
        self.calc_overpayment()

    def calc_overpayment(self):
        overpayment = math.ceil(self.payments_record - self.credit_principal)
        print(f"Overpayment = {overpayment}")

    def calc_nominal_interest(self):
        self.nominal_i = self.interest / (12 * 100)

    def calc_credit_principal(self):
        self.credit_principal = self.monthly_payment // ((self.nominal_i * (
                (1 + self.nominal_i) ** self.count_period)) / (((1 + self.nominal_i) ** self.count_period) - 1))
        self.payments_record = self.monthly_payment * self.count_period
        print(f"Your credit principal = {math.ceil(self.credit_principal)}")

    def calc_monthly_payment(self):
        self.monthly_payment = self.credit_principal * (self.nominal_i * (
                (1 + self.nominal_i) ** self.count_period) / (((1 + self.nominal_i) ** self.count_period) - 1))
        self.payments_record = math.ceil(self.monthly_payment) * self.count_period
        print(f"Your annuity payment = {math.ceil(self.monthly_payment)}")

    def calc_count_periods(self):
        division = self.monthly_payment / (self.monthly_payment - self.nominal_i * self.credit_principal)
        self.count_period = math.ceil(math.log(division, (1 + self.nominal_i)))
        self.read_months()
        self.payments_record = self.monthly_payment * self.count_period

    def read_months(self):
        years = self.count_period // 12
        months = self.count_period % 12
        s = "s" if years > 0 else ""
        sm = "s" if months > 0 else ""
        if months == 0:
            print(f"You need {years} year{s} to repay this credit!")
        if years == 0:
            print(f"You need {months} month{sm} to repay this credit!")
        else:
            print(f"You need {years} year{s} and {months} month{sm} to repay this credit!")

    def run(self):
        if self.type == 'annuity':
            self.get_action()
        else:
            self.calc_diff_payment()


x = get_arguments()
if x:
    myCalc = CreditCalc(t=x.type, principal=x.principal, payment=x.payment, periods=x.periods, interest=x.interest)
    myCalc.run()
else:
    print("Incorrect parameters")
