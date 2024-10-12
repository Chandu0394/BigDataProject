#pandas to create a DataFrame from the generated records.
import pandas as pd
#used to generate random numbers or select random items.
import random
#datetime is a module for working with dates and times in Python, 
#while timedelta is a class used to represent differences between two dates or times.
from datetime import datetime, timedelta

#This function is used to generate random dates within a given range,
#making it useful when you need randomized timestamps for datasets such as an e-commerce order history.
def random_date(start, end):
    return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))

# Generate random data for the e-commerce dataset
records = []
def generate_data(num_records=10000):
    # Define possible values for categorical fields
    product_categories = ['Electronics', 'Stationery', 'Books', 'Clothing', 'Home & Kitchen']
    payment_types = ['Card', 'Internet Banking', 'UPI', 'Wallet']
    countries = ['India', 'USA', 'UK', 'Germany', 'Australia']
    cities = {
        'India': ['Mumbai', 'Bengaluru', 'Indore'],
        'USA': ['Boston', 'New York', 'Chicago'],
        'UK': ['London', 'Oxford', 'Manchester'],
        'Germany': ['Berlin', 'Munich', 'Hamburg'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane']
    }
    websites = ['www.amazon.com', 'www.flipkart.com', 'www.ebay.in', 'www.tatacliq.com']

    # Date range for order dates
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 12, 31)

    # Prepare a list for records
    #records = []

    # Generate the records
    for i in range(num_records):
        # Basic order details
        order_id = i + 1
        customer_id = random.randint(100, 200)
        customer_name = random.choice(['John Smith', 'Mary Jane', 'Joe Smith', 'Neo', 'Trinity'])

        # Product details
        product_id = random.randint(200, 300)
        product_name = random.choice(['Pen', 'Pencil', 'Mobile', 'Laptop', 'Book'])
        product_category = random.choice(product_categories)

        # Payment details
        payment_type = random.choice(payment_types)
        qty = random.randint(1, 50)
        price = random.randint(5, 10000)
        order_datetime = random_date(start_date, end_date)

        # Location details
        country = random.choice(countries)
        city = random.choice(cities[country])
        website = random.choice(websites)

        # Payment transaction details
        payment_txn_id = random.randint(10000, 99999)
        payment_success = random.choice(['Y', 'N'])

        failure_reason = ''
        if payment_success == 'N':
            failure_reason = random.choice(['Invalid CVV', 'Insufficient Funds', 'Timeout'])

        # Introduce rogue records with a 5% probability
        if random.random() < 0.05:  # 5% chance of rogue record
            if random.random() < 0.5:
                customer_name = ""  # Empty customer name
            else:
                payment_type = "Invalid"  # Invalid payment type

        # Append the generated record
        records.append([
            order_id, customer_id, customer_name, product_id, product_name, 
            product_category, payment_type, qty, price, order_datetime, 
            country, city, website, payment_txn_id, payment_success, failure_reason
        ])


generate_data()

# Generate a dataset with rogue records
def generate_data_with_rogue_records(num_records=10000):
    # Define product categories and examples for each
    electronics = [
        'Smartphone', 'Laptop', 'Tablet', 'Smartwatch', 'Bluetooth Speaker', 
        'Headphones', 'Gaming Console', 'Camera', 'Drone', 'External Hard Drive', 
        'USB Flash Drive', 'Smart TV', 'Wireless Router', 'Portable Charger', 
        'Projector', 'Fitness Tracker', 'VR Headset', 'Home Theater System', 
        'Monitor', 'Bluetooth Earbuds'
    ]
    
    stationery = [
        'Pens', 'Pencils', 'Eraser', 'Notebook', 'Stapler', 
        'Paper Clips', 'Markers', 'Highlighters', 'Ruler', 'Glue Stick', 
        'Scissors', 'Sticky Notes', 'Tape', 'Calculator', 'File Folder', 
        'Binder', 'Whiteboard Markers', 'Pencil Sharpener', 'Letter Opener', 'Paper Cutter'
    ]
    
    books = [
        'Fiction', 'Non-fiction', 'Biography', 'Science Fiction', 'Fantasy', 
        'Mystery', 'Historical Fiction', 'Self-Help', 'Cookbooks', 'Comics', 
        'Graphic Novels', 'Poetry', 'Travel Books', 'Thrillers', 'Horror', 
        'Children\'s Books', 'Young Adult', 'Classics', 'Textbooks', 'Memoir'
    ]
    
    clothing = [
        'T-Shirts', 'Jeans', 'Jackets', 'Sweaters', 'Hoodies', 
        'Dresses', 'Shorts', 'Skirts', 'Suits', 'Blouses', 
        'Coats', 'Pants', 'Socks', 'Underwear', 'Swimwear', 
        'Sportswear', 'Nightwear', 'Shoes', 'Scarves', 'Hats'
    ]
    
    home_kitchen = [
        'Cookware', 'Cutlery', 'Plates', 'Mugs', 'Glasses', 
        'Oven Mitts', 'Kitchen Towels', 'Spatulas', 'Mixing Bowls', 'Food Storage Containers', 
        'Blender', 'Microwave', 'Toaster', 'Coffee Maker', 'Dish Rack', 
        'Chopping Board', 'Measuring Cups', 'Kitchen Scale', 'Air Fryer', 'Pressure Cooker'
    ]

    # Define product categories list for random selection
    product_categories = ['Electronics', 'Stationery', 'Books', 'Clothing', 'Home & Kitchen']
    payment_types = ['Card', 'Internet Banking', 'UPI', 'Wallet']
    countries = ['India', 'USA', 'UK', 'Germany', 'Australia']
    cities = {
        'India': ['Mumbai', 'Bengaluru', 'Indore'],
        'USA': ['Boston', 'New York', 'Chicago'],
        'UK': ['London', 'Oxford', 'Manchester'],
        'Germany': ['Berlin', 'Munich', 'Hamburg'],
        'Australia': ['Sydney', 'Melbourne', 'Brisbane']
    }
    websites = ['www.amazon.com', 'www.flipkart.com', 'www.ebay.in', 'www.tatacliq.com']

    # Date range for order dates
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2021, 12, 31)

    # Prepare a list for records
    records = []

    # Generate the records
    for i in range(num_records):
        # Basic order details
        order_id = i + 1
        customer_id = random.randint(100, 200)
        customer_name = random.choice(['John Smith', 'Mary Jane', 'Joe Smith', 'Neo', 'Trinity'])

        # Product details
        product_category = random.choice(product_categories)
        if product_category == 'Electronics':
            product_name = random.choice(electronics)
        elif product_category == 'Stationery':
            product_name = random.choice(stationery)
        elif product_category == 'Books':
            product_name = random.choice(books)
        elif product_category == 'Clothing':
            product_name = random.choice(clothing)
        elif product_category == 'Home & Kitchen':
            product_name = random.choice(home_kitchen)
        product_id = random.randint(200, 300)

        # Payment details
        payment_type = random.choice(payment_types)
        qty = random.randint(1, 50)
        price = random.randint(5, 10000)
        order_datetime = random_date(start_date, end_date)

        # Location details
        country = random.choice(countries)
        city = random.choice(cities[country])
        website = random.choice(websites)

        # Payment transaction details
        payment_txn_id = random.randint(10000, 99999)
        payment_success = random.choice(['Y', 'N'])
        failure_reason = ''
        if payment_success == 'N':
            failure_reason = random.choice(['Invalid CVV', 'Insufficient Funds', 'Timeout'])

        # Introduce rogue records with various issues
        if random.random() < 0.1:  # 10% chance of rogue record
            issue_type = random.choice(['missing_customer_name', 'invalid_payment_type', 'unrealistic_price'])
            
            if issue_type == 'missing_customer_name':
                customer_name = ""  # Empty customer name
            elif issue_type == 'invalid_payment_type':
                payment_type = "Invalid"  # Invalid payment type
            elif issue_type == 'unrealistic_price':
                price = random.randint(100000, 1000000)  # Unrealistically high price

        # Append the generated record
        records.append([
            order_id, customer_id, customer_name, product_id, product_name, 
            product_category, payment_type, qty, price, order_datetime, 
            country, city, website, payment_txn_id, payment_success, failure_reason
        ])

    # Convert the list of records into a DataFrame
    df = pd.DataFrame(records, columns=[
        'order_id', 'customer_id', 'customer_name', 'product_id', 'product_name', 
        'product_category', 'payment_type', 'qty', 'price', 'datetime', 
        'country', 'city', 'ecommerce_website_name', 'payment_txn_id', 
        'payment_txn_success', 'failure_reason'
    ])

    return df

# Generate 100 records with some rogue entries
df_with_rogue_records = generate_data_with_rogue_records(num_records=10000)


# 2. Popularity of Products Throughout the Year
import matplotlib.pyplot as plt
import seaborn as sns
# Prepare data
df['month'] = df['datetime'].dt.to_period('M').astype(str)
popularity_time = df.groupby(['month', 'product_category'])['qty'].sum().reset_index()
# Create the plot with Set1 palette
plt.figure(figsize=(12, 6))
sns.lineplot(x='month', y='qty', hue='product_category', data=popularity_time, palette='Set1')
plt.title('Popularity of Products Over Time', fontsize=16, weight='bold')
plt.xlabel('Month', fontsize=14)
plt.ylabel('Total Quantity Sold', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.show()
