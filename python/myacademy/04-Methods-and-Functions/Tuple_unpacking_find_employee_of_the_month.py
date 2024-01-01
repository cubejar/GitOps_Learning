# stock_prices = [('APPL', 200), ('JBL', 20), ('ORCL', 120)]
# for ticker, price in stock_prices:
#     print(ticker, price + (price*.2))

work_hours = [('Raj', 111140), ('Ram', 3000), ('Diya', 400)]

def emp_of_month(work_hours):
    emp_name = ''
    log_hours = 0
    for key,value in work_hours:
        if value > log_hours:
            emp_name = key
            log_hours = value
        else:
            pass
    return (emp_name, log_hours)

print(emp_of_month(work_hours))

#
# items = emp_of_month(work_hours)
# emp, hours = emp_of_month(work_hours)
# print(emp)
# print(hours)
# print(items)