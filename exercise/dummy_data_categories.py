from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random

fake = Faker()

# Daftar kategori buku
categories = [
    {'category_id': 1, 'category_name': 'Self-Improvement'},
    {'category_id': 2, 'category_name': 'Biography'},
    {'category_id': 3, 'category_name': 'Fantasy'},
    {'category_id': 4, 'category_name': 'Romance'},
    {'category_id': 5, 'category_name': 'Science Fiction'}
]

# Membuat DataFrame dari data categories
categories_df = pd.DataFrame(categories)


# Menyimpan DataFrame ke dalam file CSV
csv_file_path = "dummy_data_categories.csv"
categories_df.to_csv(csv_file_path, index = False)