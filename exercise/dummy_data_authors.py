from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random

fake = Faker()

# Menghasilkan 200 penulis dengan ID dan nama
authors = [{'author_id': idx + 1, 'author_name': fake.name()} for idx in range(200)]

# Membuat DataFrame dari data penulis
authors_df = pd.DataFrame(authors)

# Menyimpan DataFrame ke dalam file CSV
csv_file_path = 'authors_data.csv'
authors_df.to_csv(csv_file_path, index=False)