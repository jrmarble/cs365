#Judson Marble
#cs365
#charts

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('retired_nba_players_since_2000.csv')

# Calculate the length of each player's career
df['CareerLength'] = df['To'] - df['From'] + 1  # Adding 1 to make it inclusive

# Calculate the frequency of each career length
career_length_counts = df['CareerLength'].value_counts().sort_index()

# Plotting the line chart
plt.figure(figsize=(10, 6))
plt.plot(career_length_counts.index, career_length_counts.values, marker='o', linestyle='-', color='b')
plt.title('Distribution of NBA Players According to Career Length')
plt.xlabel('Career Length (Years)')
plt.ylabel('Number of Players')
plt.xticks(career_length_counts.index)
plt.grid(axis='both', which='major', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
