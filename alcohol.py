import pandas as pd
import matplotlib.pyplot as plt # type: ignore
import numpy as np

# Load the Excel file
file_path = "C://Users//bibek//Alcohol_consumption_Indian_State_2021_.xlsx"
data = pd.ExcelFile(file_path)

# Parse the sheet
df = data.parse('Alcohol_consumption_India_2021')

# Filter for "Total" area to avoid duplicating Urban/Rural
df_total = df[df['Area'] == 'Total']

# Extract relevant columns
states = df_total['States/UTs']
women_consumption = df_total['Women age 15 years and above who consume alcohol (%)']
men_consumption = df_total['Men age 15 years and above who consume alcohol (%)']

# Visualization 1: Bar Chart - Alcohol Consumption (Women vs. Men)
x = np.arange(len(states))  # Positions for the bars
width = 0.4  # Width of the bars

plt.figure(figsize=(14, 8))
plt.bar(x - width/2, women_consumption, width, label='Women', color='lightblue', edgecolor='black')
plt.bar(x + width/2, men_consumption, width, label='Men', color='salmon', edgecolor='black')

# Customize the plot
plt.xlabel('States/UTs', fontsize=12)
plt.ylabel('Alcohol Consumption (%)', fontsize=12)
plt.title('Comparison of Alcohol Consumption (Men vs. Women)', fontsize=16)
plt.xticks(x, states, rotation=90, fontsize=10)
plt.legend(fontsize=12)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()

# Visualization 2: Horizontal Bar Chart - Top 10 States (Men Alcohol Consumption)

# Sort data for top 10 states with highest alcohol consumption among men
top_men = df_total.sort_values('Men age 15 years and above who consume alcohol (%)', ascending=False).head(10)

# Extract relevant data
states = top_men['States/UTs']
men_consumption = top_men['Men age 15 years and above who consume alcohol (%)']

# Plotting the horizontal bar chart using matplotlib
plt.figure(figsize=(10, 6))
y_pos = np.arange(len(states))  # Positions for the states
plt.barh(y_pos, men_consumption, color='red', edgecolor='black')

# Adding labels and title
plt.yticks(y_pos, states, fontsize=10)
plt.xlabel('Alcohol Consumption (%)', fontsize=12)
plt.ylabel('States/UTs', fontsize=12)
plt.title('Top 10 States by Alcohol Consumption (Men)', fontsize=14)

# Adjust layout for better appearance
plt.tight_layout()
plt.show()

# Visualization 3: Horizontal Bar Chart - Top 10 States (Women Alcohol Consumption)
top_women = df_total.sort_values('Women age 15 years and above who consume alcohol (%)', ascending=False).head(10)

# Extract data for plotting
states = top_women['States/UTs']
consumption = top_women['Women age 15 years and above who consume alcohol (%)']

# Plot the horizontal bar chart
plt.figure(figsize=(10, 6))
y_pos = np.arange(len(states))  # Positions for the bars

plt.barh(y_pos, consumption, color='skyblue', edgecolor='black')
plt.yticks(y_pos, states, fontsize=10)
plt.xlabel('Alcohol Consumption (%)', fontsize=12)
plt.ylabel('States/UTs', fontsize=12)
plt.title('Top 10 States by Alcohol Consumption (Women)', fontsize=14)

# Adjust layout for better appearance
plt.tight_layout()
plt.show()

# Visualization 4: Scatter Plot - Women vs. Men Alcohol Consumption

# Extract relevant data
women_consumption = df_total['Women age 15 years and above who consume alcohol (%)']
men_consumption = df_total['Men age 15 years and above who consume alcohol (%)']
states = df_total['States/UTs']

# Scatter Plot
plt.figure(figsize=(8, 8))
scatter = plt.scatter(
    women_consumption,
    men_consumption,
    c=np.arange(len(states)),  # Use a range of colors for each state
    cmap='tab20',
    edgecolor='black',
    s=100  # Size of the points
)

# Add state names as annotations
for i, state in enumerate(states):
    plt.text(
        women_consumption.iloc[i] + 0.5,  # Adjust position slightly for visibility
        men_consumption.iloc[i],
        state,
        fontsize=5
    )

# Customize the plot
plt.title('Scatter Plot: Women vs. Men Alcohol Consumption', fontsize=14)
plt.xlabel('Women Alcohol Consumption (%)', fontsize=12)
plt.ylabel('Men Alcohol Consumption (%)', fontsize=12)
plt.colorbar(scatter, label='State Index')  # Add a color bar for reference
plt.tight_layout()
plt.show()

# Visualization 5: grouped bar chart - Comparison of Alcohol Consumption Among Men and Women in Odisha with there nearest States

# Filter for "Total" area and the specified states
states_to_compare = ['Odisha', 'Andhra Pradesh', 'West Bengal', 'Chhattisgarh', 'Jharkhand']
df_filtered = df[(df['Area'] == 'Total') & (df['States/UTs'].isin(states_to_compare))]

# Extract data for plotting
states = df_filtered['States/UTs']
women_consumption = df_filtered['Women age 15 years and above who consume alcohol (%)']
men_consumption = df_filtered['Men age 15 years and above who consume alcohol (%)']

# Create the grouped bar chart
x = np.arange(len(states))  # Positions for the bars
width = 0.4  # Width of the bars

plt.figure(figsize=(10, 6))
plt.bar(x - width/2, women_consumption, width, label='Women', color='lightblue', edgecolor='black')
plt.bar(x + width/2, men_consumption, width, label='Men', color='salmon', edgecolor='black')

# Customize the plot
plt.xlabel('States/UTs', fontsize=12)
plt.ylabel('Alcohol Consumption (%)', fontsize=12)
plt.title('Comparison of Alcohol Consumption Among Men and Women in Odisha with there nearest States', fontsize=16)
plt.xticks(x, states, rotation=0, fontsize=12)
plt.legend(fontsize=12)

# Adjust layout for better visibility
plt.tight_layout()
plt.show()

# Visualization 6: grouped bar chart - Comparison of Alcohol Consumption Among Men and Women in Odisha with there nearest States
# Filter data for India
df_india = df[df['States/UTs'] == 'India']

# Aggregate alcohol consumption for Urban and Rural areas
urban_men = df_india[df_india['Area'] == 'Urban']['Men age 15 years and above who consume alcohol (%)'].sum()
urban_women = df_india[df_india['Area'] == 'Urban']['Women age 15 years and above who consume alcohol (%)'].sum()
rural_men = df_india[df_india['Area'] == 'Rural']['Men age 15 years and above who consume alcohol (%)'].sum()
rural_women = df_india[df_india['Area'] == 'Rural']['Women age 15 years and above who consume alcohol (%)'].sum()

# Prepare data for the pie chart
labels = ['Urban Men', 'Urban Women', 'Rural Men', 'Rural Women']
sizes = [urban_men, urban_women, rural_men, rural_women]
colors = ['lightblue', 'lightpink', 'skyblue', 'salmon']

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(
    sizes,
    labels=labels,
    autopct='%1.0f%%',
    colors=colors,
    startangle=140,
    textprops={'fontsize': 12}
)
plt.title('Alcohol Consumption in India: Urban vs. Rural (Men & Women)', fontsize=14)
plt.tight_layout()
plt.show()
