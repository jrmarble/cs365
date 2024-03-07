#Judson Marble
#cs365
#brscraper

import pandas as pd
import string

# Initialize an empty DataFrame to store player data
df = pd.DataFrame()

# Iterate through each letter to get player data
for letter in list(string.ascii_lowercase):
    url = f'https://www.basketball-reference.com/players/{letter}/'
    try:
        # Attempt to read the table from the URL
        table = pd.read_html(url)[0]
        # Some preprocessing might be needed to handle cases where the table includes footnotes or extra rows
        # that are not player data. This depends on the structure of the tables you're scraping.
        df = pd.concat([df, table])
    except ValueError:
        # Handle the case where no table was found for a given letter
        print(f"No table found for players starting with {letter}")

# Rename columns for clarity and consistency with desired output
df.rename(columns={'Player':'playerName', 'Birth Date': 'birthDate'}, inplace=True)

# Filter out players who started before the 1999-2000 season or are still active
# Assuming "To" = 2023 or a future year indicates an active player, adjust as necessary
df = df[(df['From'] >= 2000) & (df['To'] < 2023)]

# Convert 'To' and 'From' to numeric for filtering, in case they are not already
df['From'] = pd.to_numeric(df['From'], errors='coerce')
df['To'] = pd.to_numeric(df['To'], errors='coerce')

# Save the filtered DataFrame to a CSV file
df.to_csv('retired_nba_players_since_2000.csv', index=False)