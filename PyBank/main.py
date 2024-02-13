import csv

file_path = '/Users/eddie/Desktop/python-challenge/python-challenge/PyBank/Resource/budget_data.csv'

with open(file_path, mode='r') as file:
    reader = csv.reader(file)

    next(reader)

    Total_Months = 0
    sum_b = 0
    changes = []
    greater_increase = 0
    greater_decrease = 0
    first_row = next(reader)
    last_month = int(first_row[1])
    Total_Months += 1
    sum_b += last_month
    g_month = first_row[0]
    l_month = first_row[0]
    
    for row in reader:
        Total_Months += 1
        value_b = int(row[1])
        sum_b += value_b
        
        monthly_change = value_b - last_month
        changes.append(monthly_change)
        
        if monthly_change > greater_increase:
            greater_increase = monthly_change
            g_month = row[0]
            
        if monthly_change < greater_decrease:
            greater_decrease = monthly_change
            l_month = row[0]
            
        last_month = value_b

    Average_Change = sum(changes) / len(changes)

    print("Total Months:", Total_Months)
    print("Total: ${}".format(sum_b))
    print("Average Change: ${:.2f}".format(Average_Change))
    print("Greatest Increase in Profits:", g_month, "(${})".format(greater_increase))
    print("Greatest Decrease in Profits:", l_month, "(${})".format(greater_decrease))
