# (expression(alway final return value) for expression in List if condition in expression)
# generators are very fast and it doesnot save everything in memory at once it stream result one by one as we need it.

# (expression for expression in iterator)

sales_inr = [3,14, 6, 45, 776, 34, 54, 6, 56, 98, 5, 6]

total_sales = sum(sale for sale in sales_inr if sale < 10)
print(f"total sales", total_sales)

before_sum = (sale for sale in sales_inr)
print(f"before sales", before_sum)

