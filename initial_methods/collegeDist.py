import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ensure you have seaborn installed
# pip install seaborn

# Load the data from the CSV file
df = pd.read_csv('retired_nba_players_since_2000.csv')

# Calculate the length of each player's career
df['CareerLength'] = df['To'] - df['From'] + 1

# Separate players into two groups: attended college and did not attend college
attended_college = df[df['Colleges'].notna() & (df['Colleges'] != '')]['CareerLength']
did_not_attend_college = df[~df['Colleges'].notna() | (df['Colleges'] == '')]['CareerLength']

# Plotting
plt.figure(figsize=(10, 6))

sns.kdeplot(attended_college, shade=True, label='Attended College', color='blue', alpha=0.4)
sns.kdeplot(did_not_attend_college, shade=True, label='Did Not Attend College', color='green', alpha=0.4)

plt.title('Distribution of Career Lengths: College vs. No College')
plt.xlabel('Career Length (Years)')
plt.ylabel('Density')
plt.legend()

plt.tight_layout()
plt.show()
