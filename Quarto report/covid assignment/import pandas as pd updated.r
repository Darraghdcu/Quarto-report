import pandas as pd
import plotly.express as px

# Ensure the file path is correct
file_path = 'country_data.csv'

# Load the data
covid_data = pd.read_csv(file_path)

# Display first few rows to ensure data is loaded correctly
print(covid_data.head())
print(covid_data.columns)

# Use appropriate column names for the plot
fig_world_map = px.choropleth(covid_data, 
                              locations="iso_code",  # Use 'iso_code' for ISO country codes
                              locationmode="ISO-3",  # Specify the location mode
                              color="total_cases",  # Ensure 'total_cases' exists in your data
                              hover_name="location",  # Use 'location' for country names
                              color_continuous_scale=px.colors.sequential.Plasma,
                              title="Total COVID-19 Cases by Country")

# Save the figure as an HTML file
fig_world_map.write_html("world_map.html")

# To display the plot in the notebook (if using Jupyter Notebook)
fig_world_map.show()
