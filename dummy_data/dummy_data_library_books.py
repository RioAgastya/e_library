import pandas as pd
from faker import Faker
import random

fake = Faker()

# Fungsi untuk membuat data dummy book_id dan library_id
def generate_dummy_data(library_id, num_books_per_library):
    book_ids = list(range(1, num_books_per_library + 1))
    return [{'library_id': library_id, 'book_id': book_id} for book_id in book_ids]

# Membuat 10 data dummy library_id, masing-masing dengan 20 book_id
jumlah_library = 10
jumlah_buku_per_library = 20
data_dummy = []

for library_id in range(1, jumlah_library + 1):
    data_dummy.extend(generate_dummy_data(library_id, jumlah_buku_per_library))

# Membuat DataFrame dari data dummy
df = pd.DataFrame(data_dummy)

# Menampilkan DataFrame
print(df)

# Menyimpan DataFrame ke file CSV
df.to_csv('dummy_data_library_books.csv', index=False)