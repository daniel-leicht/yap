def profit(sales_data):
    sales = 0
    for sale_info in sales_data:
        if sale_info['Country'] == "Israel":
            # Reduce VAT from sales:
            sales += sale_info['Total'] / 1.17

        elif sale_info['Country'] == "Germany":
            # Reduce VAT from sales:
            sales += sale_info['Total'] / 1.19

        elif sale_info['Country'] == "Japan":
            # Add government incentive tax:
            if sale_info['Total'] > 20000:
                sales *= 1.025

        elif sale_info['Country'] == "Australia":
            # Add government incentive tax:
            if sale_info['Total'] > 15000:
                sales *= 1.03

        elif sale_info['Country'] == "Finland":
            # Reduce VAT from sales:
            sales += sale_info['Total'] / 1.17

            # Reduce transaction fees:
            try:
                sales -= sale_info['SaleCount'] * 25
            except Exception:
                pass

        else:
            sales += sale_info['Total']

        return sales


sales_data = [
    {"Country": "Australia", "Total": 18000, "SaleCount": 12},
    {"Country": "Finland", "Total": 9000, "SaleCount": 10},
    {"Country": "United States", "Total": 25000, "SaleCount": 15},
    {"Country": "United Kingdom", "Total": 13000, "SaleCount": 20},
    {"Country": "France", "Total": 14500, "SaleCount": 15},
    {"Country": "Italy", "Total": 10000, "SaleCount": 12},
    {"Country": "China", "Total": 35000, "SaleCount": 25},
    {"Country": "India", "Total": 25000, "SaleCount": 20},
    {"Country": "Israel", "Total": 15000, "SaleCount": 8},
    {"Country": "Brazil", "Total": 20000, "SaleCount": 18},
    {"Country": "Mexico", "Total": 15000, "SaleCount": 12},
    {"Country": "Russia", "Total": 17500, "SaleCount": 14},
    {"Country": "South Africa", "Total": 9000, "SaleCount": 10},
    {"Country": "Indonesia", "Total": 12000, "SaleCount": 15},
    {"Country": "Egypt", "Total": 10000, "SaleCount": 12},
    {"Country": "Germany", "Total": 12000, "SaleCount": 10},
    {"Country": "Iran", "Total": 14000, "SaleCount": 15},
    {"Country": "Turkey", "Total": 18000, "SaleCount": 20},
    {"Country": "Nigeria", "Total": 11000, "SaleCount": 12},
    {"Country": "Argentina", "Total": 9000, "SaleCount": 10},
    {"Country": "Japan", "Total": 22000, "SaleCount": 6},
]

print(profit(sales_data))
