#Judson Marble
#cs365
#HtWt

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('retired_nba_players_since_2000.csv')

# Calculate the career length
df['CareerLength'] = df['To'] - df['From'] + 1

# Plotting Height vs. Career Length
plt.figure(figsize=(10, 6))
plt.scatter(df['Ht'], df['CareerLength'], color='blue', alpha=0.6, edgecolors='w', s=100)
plt.title('Height vs. Career Length')
plt.xlabel('Height (inches)')
plt.ylabel('Career Length (years)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()

# Plotting Weight vs. Career Length
plt.figure(figsize=(10, 6))
plt.scatter(df['Wt'], df['CareerLength'], color='green', alpha=0.6, edgecolors='w', s=100)
plt.title('Weight vs. Career Length')
plt.xlabel('Weight (pounds)')
plt.ylabel('Career Length (years)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()
plt.show()
