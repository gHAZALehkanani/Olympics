import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data from CSV
csv_file_path = 'Paris2024'
df = pd.read_csv(csv_file_path)

# Filter data for the top 30 countries by total medals
df_top30 = df.sort_values(by='Total', ascending=False).head(30)

# Create a stacked bar chart
bar_width = 0.8
fig, ax = plt.subplots(figsize=(12, 8))

# Define the bar positions
indices = np.arange(len(df_top30['Country']))

ax.bar(indices, df_top30['Gold'], bar_width, label='Gold', color='gold')
ax.bar(indices, df_top30['Silver'], bar_width, bottom=df_top30['Gold'], label='Silver', color='silver')
ax.bar(indices, df_top30['Bronze'], bar_width, bottom=df_top30['Gold'] + df_top30['Silver'], label='Bronze', color='#cd7f32')

ax.set_xlabel('Country')
ax.set_ylabel('Number of Medals')
ax.set_title('Stacked Bar Chart of Medals by Country - Top 30 Countries')
ax.set_xticks(indices)
ax.set_xticklabels(df_top30['Country'], rotation=45, ha='right')
ax.legend()

plt.tight_layout()
plt.show()


df_sorted_gold_top30 = df_top30.sort_values(by='Gold', ascending=False)

# Create a horizontal bar plot for Gold medals
plt.figure(figsize=(12, 8))
plt.barh(df_sorted_gold_top30['Country'], df_sorted_gold_top30['Gold'], color='gold')
plt.xlabel('Number of Gold Medals')
plt.title('Gold Medals by Country - Top 30 Countries (Paris 2024)')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest value on top
plt.tight_layout()
plt.show()


# Calculate the cumulative sum for top 30 countries
df_cumsum_top30 = df_top30[['Gold', 'Silver', 'Bronze']].cumsum()

# Create a line plot for cumulative medals
plt.figure(figsize=(12, 8))
plt.plot(df_top30['Country'], df_cumsum_top30['Gold'], label='Gold', color='gold', marker='o')
plt.plot(df_top30['Country'], df_cumsum_top30['Silver'], label='Silver', color='silver', marker='o')
plt.plot(df_top30['Country'], df_cumsum_top30['Bronze'], label='Bronze', color='#cd7f32', marker='o')


plt.title('Cumulative Medal Count by Country - Top 30 Countries')
plt.xlabel('Country')
plt.ylabel('Cumulative Number of Medals')
plt.xticks(rotation=45, ha='right')
plt.legend()

plt.tight_layout()
plt.show()


# Create a bubble chart for top 10 countries
plt.figure(figsize=(10, 8))
df_top10 = df.sort_values(by='Total', ascending=False).head(10)
# size of the bubbles is proportional to the number of Silver medals
plt.scatter(df_top10['Gold'], df_top10['Total'], s=df_top10['Silver']*30, color='blue', alpha=0.6, edgecolors='w', linewidth=2)

# Add country labels to each bubble using iloc to avoid index misalignment
for i in range(len(df_top10)):
    plt.text(df_top10['Gold'].iloc[i], df_top10['Total'].iloc[i], df_top30['Country'].iloc[i], fontsize=9)


plt.title('Total Medals vs. Gold Medals (Bubble Size: Silver Medals) - Top 10 Countries')
plt.xlabel('Gold Medals')
plt.ylabel('Total Medals')
plt.grid(True)


plt.tight_layout()
plt.show()

bar_width = 0.25
indices = np.arange(len(df_top30['Country']))

# Create a grouped bar chart
plt.figure(figsize=(12, 8))

plt.bar(indices, df_top30['Gold'], bar_width, label='Gold', color='gold')

plt.bar(indices + bar_width, df_top30['Silver'], bar_width, label='Silver', color='silver')

plt.bar(indices + 2 * bar_width, df_top30['Bronze'], bar_width, label='Bronze', color='#cd7f32')

plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.title('Medal Comparison by Type - Top 30 Countries')
plt.xticks(indices + bar_width, df_top30['Country'], rotation=45, ha='right')

plt.legend()

plt.tight_layout()
plt.show()
