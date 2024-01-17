import matplotlib.pyplot as plt
import numpy as np
import sys
file1=sys.argv[1]
file2=sys.argv[2]
file3=sys.argv[3]



# Load data from the file zeo_traj_compile.psd_histo
with open(file1, "r") as file:
    lines = file.readlines()

# Skip the first line (heading) and split the data into columns
data = [line.split() for line in lines[2:]]

# Extract the columns for x, y, positive deviation, and negative deviation
x_values = [float(row[0]) for row in data]
y_values = [float(row[1]) for row in data]
pos_deviation = [float(row[2]) for row in data]
neg_deviation = [float(row[3]) for row in data]

# Use LaTeX to make part of the label bold
label1 = r'$\bf{DUT4\_PP}$'
label2 = r'$\bf{DUT4}$'
label3 = r'$\bf{PP}$'

# Create the plot
plt.plot(x_values, y_values, linewidth=2, label=label1)
plt.fill_between(x_values, [y - pd for y, pd in zip(y_values, neg_deviation)],
                 [y + pd for y, pd in zip(y_values, pos_deviation)],
                 color='lightblue', alpha=0.5)
plt.legend(title='DUT4+PS')

with open(file2, "r") as file:
    lines = file.readlines()
data = [line.split() for line in lines[2:]]
x_values = [float(row[0]) for row in data]
y_values = [float(row[1]) for row in data]
pos_deviation = [float(row[2]) for row in data]
neg_deviation = [float(row[3]) for row in data]
plt.plot(x_values, y_values, linewidth=2, label=label2, color='grey')
plt.fill_between(x_values, [y - pd for y, pd in zip(y_values, neg_deviation)],
                 [y + pd for y, pd in zip(y_values, pos_deviation)],
                 color='grey', alpha=0.5)


with open(file3, "r") as file:
    lines = file.readlines()
data = [line.split() for line in lines[2:]]
x_values = [float(row[0]) for row in data]
y_values = [float(row[1]) for row in data]
pos_deviation = [float(row[2]) for row in data]
neg_deviation = [float(row[3]) for row in data]
plt.plot(x_values, y_values, linewidth=2, label=label3, color='red')
plt.fill_between(x_values, [y - pd for y, pd in zip(y_values, neg_deviation)],
                 [y + pd for y, pd in zip(y_values, pos_deviation)],
                 color='red', alpha=0.25)



# Customize the plot
#plt.title('Pore Size Distribution')
plt.xlabel('Pore size (Å)', fontsize=20)  # Using Ångström symbol
plt.ylabel('Pore size distribution', fontsize=20)
plt.grid(False)
# Add the legend to the plot
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.legend(fontsize=20)
plt.ylim(0, 1)
plt.xlim(0, 12)
plt.xticks(np.arange(0, 12, 2),fontsize=20)
plt.yticks(fontsize=20)
plt.tick_params(axis='both', which='both', direction='in', length=10)


plt.savefig('DUT_PP.jpg', dpi=1000, bbox_inches='tight')


# Show the plot
plt.show()


