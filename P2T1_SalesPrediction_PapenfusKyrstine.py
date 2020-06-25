#get user input for total sales, calculate profit (23 percent)
#6/25/2020
#CTI-110 P2T1 - Sales Prediction
#Kyrstine Papenfus

#get projected total sales from user 
total_sales = float(input ('Enter the projected sales: '))

#calculate profit (23 percent)
profit = total_sales * 0.23

# display
print('The profit is $', format(profit, ',.2f'))

