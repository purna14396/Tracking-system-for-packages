import random
import string


# Generate random order data
def generate_order_data():
    alphabets = ''.join(random.choices(string.ascii_uppercase, k=4))
    numbers = str(random.randint(100000,999999))
    orders = alphabets + numbers
    order_id = orders
    order_details = str(order_id)
    status = random.choice(["Pending", "Shipped", "Delivered"])
    location = generate_location()
    customer_details = generate_customer()
    # Add other features as needed
    return {"order_id": order_id, "order_details": order_details, "status": status, "location": location, "customer_details": customer_details}

def generate_customer():
    first_name = random.choice(["John", "Mary", "David", "Lisa", "Steven", "Emily", "Michael", "Rachel", "Daniel", "Julia"])
    last_name = random.choice(["Smith", "Johnson", "Brown", "Lee", "Garcia", "Martinez", "Davis", "Hernandez", "Miller", "Gonzalez"])
    phone = str(random.randint(1000000000, 9999999999))
    email = first_name.lower() + "." + last_name.lower() + "@" + random.choice(["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"])
    # Add other customer details as needed
    return {"first_name": first_name, "last_name": last_name, "phone": phone, "email": email}

# Generate random location in India
def generate_location():
    city = random.choice(["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata", "Pune", "Ahmedabad", "Jaipur", "Surat"])
    country = "India"
    pincode = str(random.randint(100000, 999999))
    # Add other location features as needed
    return {"city": city, "country": country, "pincode": pincode}


# Store randomly generated order data
order_data_list = []
for i in range(100):  # Generate 10 random orders
    order_data = generate_order_data()
    order_data_list.append(order_data)
order_ids = []
for order in order_data_list:
    order_ids.append(order["order_id"])
print("\n\nProduct order_ids in our Database  ::: ",order_ids)  


# Function to track package status based on order ID
def track_package_status(order_id):
    for order in order_data_list:
        if order["order_id"] == order_id:
            return order["status"]
    return "Order ID not found"

# Function to get customer details for order ID
def get_customer_details(order_id):
    for order in order_data_list:
        if order["order_id"] == order_id:
            return order["customer_details"]
    return "Order ID not found"

# Function to get customer details for order ID
def get_location_details(order_id):
    for order in order_data_list:
        if order["order_id"] == order_id:
            return order["location"]
    return "Order ID not found"

# Test tracking package status
order_id_to_track = input("\nEnter your order id to track :: ")# Change to the desired order ID to track
print("\n\n\n\nDetails of order :: ",order_id_to_track)
status = track_package_status(order_id_to_track)
print("Status :::  {}".format(status))


# Test getting location for order ID
location = get_location_details(order_id_to_track)
print("location :::  {}".format(location))

# Test getting customer details for order ID
customer_details = get_customer_details(order_id_to_track)
print("Customer details :::  {}".format(customer_details))
print("\n")
