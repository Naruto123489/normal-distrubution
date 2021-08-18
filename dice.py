import random
import plotly.express as pe
import plotly.figure_factory as ff


dice_result = []
count = []

for i in range(0,100):
    dice_1 = random.randint(1,6)

    dice_2 =  random.randint(1,6)

    dice_result.append(dice_1+dice_2)

    count.append(i)

print(count, dice_result)

#fig = pe.bar(x=dice_result,y=count)
fig = ff.create_distplot([dice_result], ["Result"])
fig.show()
