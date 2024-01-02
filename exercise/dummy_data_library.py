from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random

fake = Faker()

# Fungsi untuk membuat data dummy library
def generate_library_data(library_id):
    library_name = fake.company()  # Nama perpustakaan

    return {
        'library_id': library_id,
        'library_name': library_name
    }

# Membuat 10 data dummy library
jumlah_library = 10
data_library_dummy = [generate_library_data(library_id) for library_id in range(1, jumlah_library + 1)]

# Membuat DataFrame dari data dummy library
df_library = pd.DataFrame(data_library_dummy)

# Menampilkan DataFrame library
print(df_library)

# Menyimpan DataFrame library ke file CSV
df_library.to_csv('dummy_data_library.csv', index=False)