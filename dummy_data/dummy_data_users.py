from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random

fake = Faker()

# Fungsi untuk membuat data dummy user 
def generate_user_data(user_id):
    email = fake.email() #generate email
    user_name = fake.user_name() #generate user_name

    return{
        'user_id': user_id,
        'email': email,
        'user_name': user_name
    }
# Generete 300 data
jumlah_users = 300
data_users_dummy = [generate_user_data(user_id) for user_id in range(1, jumlah_users + 1)]

# DataFrame dari data dummy users
df_users = pd.DataFrame(data_users_dummy)

# Menampilkan DataFrame users
print(df_users)

# Menyimpan DataFrame user ke file 'csv'
df_users.to_csv('dummy_data_users.csv', index=False)


