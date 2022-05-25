import matplotlib.pyplot as plt
from . import Expense
import collections

expenses=Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories=[]

for e in expenses.list:
    spending_categories.append(e.category)
        

spending_counter=collections.Counter(spending_categories)
top5=spending_counter.most_common(5)

categories,count=zip(*top5)

fig,ax=plt.subplots()
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')

plt.show()
