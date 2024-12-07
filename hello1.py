import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', 'green', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']

bars = ax.bar(fruits, counts, color=bar_colors)

# Criação manual dos patches para a legenda
red_patch = mpatches.Patch(color='tab:red', label='red')
blue_patch = mpatches.Patch(color='tab:blue', label='blue')
green_patch = mpatches.Patch(color='tab:green', label='green')
orange_patch = mpatches.Patch(color='tab:orange', label='orange')

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(handles=[red_patch, blue_patch, green_patch, orange_patch], title='Fruit color')

plt.show()