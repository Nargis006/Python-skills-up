tea_price_in_rupees = {
    "Masala_Tea": 50,
    "Ginger_Tea": 80,
    "Normal_Tea": 30
}
# we can return 2 values 
# {expression(always final return value) for expression in List if condition in expression}
tea_price_in_dollar = {tea:price/80 for tea, price in tea_price_in_rupees.items() }

print(tea_price_in_dollar)