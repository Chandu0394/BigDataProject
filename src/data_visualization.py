#Let's find out if there are any outliers for price and quantity
# Boxplot for Price
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_with_rogue_records['price'])
plt.title('Boxplot for Price')
plt.show()

# Boxplot for Quantity
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_with_rogue_records['qty'])
plt.title('Boxplot for Quantity')
plt.show()

# 1. Top-Selling Product Categories per Country
plt.figure(figsize=(14, 8))
top_categories = df.groupby(['country', 'product_category'])['qty'].sum().reset_index() # it ensures result is returned as df
sns.barplot(x='country', y='qty', hue='product_category', data=top_categories, palette='viridis')
plt.title('Top-Selling Product Categories per Country', fontsize=16, weight='bold')
plt.xlabel('Country', fontsize=14)
plt.ylabel('Total Quantity Sold', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout() #to ensure that the elements of the plot fit neatly within the figure.
plt.legend(title='Product Category', bbox_to_anchor=(1.0, 1), loc='upper left')
plt.show()

plt.figure(figsize=(12, 6))
top_cities = df.groupby('city')['qty'].sum().reset_index().sort_values(by='qty', ascending=False)
sns.barplot(x='city', y='qty', data=top_cities.head(10))
plt.title('Top 10 Cities with Highest Sales Traffic', fontsize=16, weight='bold')
plt.xlabel('City', fontsize=14)
plt.ylabel('Total Quantity Sold', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()

# 4. Sales Traffic by Time of Day per Country
plt.figure(figsize=(12, 6))
df['hour'] = df['datetime'].dt.hour
traffic_by_time = df.groupby(['country', 'hour'])['qty'].sum().reset_index()
sns.lineplot(x='hour', y='qty', hue='country', data=traffic_by_time, palette='Set1')
plt.title('Sales Traffic by Time of Day per Country', fontsize=16, weight='bold')
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Total Quantity Sold', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()