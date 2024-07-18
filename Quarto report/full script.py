import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
data = pd.read_csv('country_data.csv')  # Adjust this path if the file is in a different location

# Ensure the 'date' column is in datetime format
data['date'] = pd.to_datetime(data['date'])

# World Map Chart using Plotly
fig_world_map = px.choropleth(data, locations="iso_code",
                              color="total_cases",
                              hover_name="location",
                              color_continuous_scale=px.colors.sequential.Plasma)
fig_world_map.write_html("world_map.html")  # Saves the map as an HTML file

# Bar Chart of Total Cases by Country using Seaborn and Matplotlib
plt.figure(figsize=(10, 6))
sns.barplot(data=data, x='total_cases', y='location')
plt.title('Total COVID-19 Cases by Country')
plt.tight_layout()
plt.savefig('bar_chart.png')  # Saves the plot as a PNG file

# Scatter Plot with Regression Line using Seaborn
plt.figure(figsize=(10, 6))
sns.regplot(data=data, x='total_cases', y='total_deaths')
plt.title('Scatter Plot of Cases vs. Deaths')
plt.tight_layout()
plt.savefig('scatterplot.png')  # Saves the plot as a PNG file

# Time Series Chart using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['new_cases'])
plt.title('New COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.tight_layout()
plt.savefig('time_series.png')  # Saves the plot as a PNG file
