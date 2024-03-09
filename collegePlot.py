#Judson Marble
#cs365
#collegePlot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Load the data from the CSV file
df = pd.read_csv('retired_nba_players_since_2000.csv')

# Calculate the length of each player's career
df['CareerLength'] = df['To'] - df['From'] + 1

# Separate players into two groups: attended college and did not attend college
attended_college = df[df['Colleges'].notna() & (df['Colleges'] != '')]['CareerLength']
did_not_attend_college = df[~df['Colleges'].notna() | (df['Colleges'] == '')]['CareerLength']

# Calculate the density using Gaussian KDE (Kernel Density Estimate)
density_college = gaussian_kde(attended_college)
density_no_college = gaussian_kde(did_not_attend_college)

# Set up the x values (career lengths) for which we'll calculate the density
x = np.linspace(0, max(df['CareerLength']), 1000)

# Calculate the density values for each subset
y_college = density_college(x)
y_no_college = density_no_college(x)

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(x, y_college, label='Attended College', color='blue')
plt.plot(x, y_no_college, label='Did Not Attend College', color='green')

plt.title('Distribution of Career Lengths: College vs. No College')
plt.xlabel('Career Length (Years)')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()