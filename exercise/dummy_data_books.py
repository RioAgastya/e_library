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

# Fungsi untuk membuat data dummy buku
def generate_book_data(book_id):
    title = fake.word()  # Judul buku
    author_id = random.randint(1, 200)  # ID penulis (1-200)
    category = random.choice(categories)
    category_id = category['category_id']
    total_quantity = random.randint(1, 10)  # Jumlah maksimal 10

    return {
        'book_id': book_id,
        'title': title,
        'author_id': author_id,
        'category_id': category_id,
        'total_quantity': total_quantity
    }

# Membuat 200 data dummy buku
jumlah_data = 200
books = [generate_book_data(book_id) for book_id in range(1, jumlah_data + 1)]

# Membuat DataFrame dari data dummy
books_df = pd.DataFrame(books)

csv_file_path = "books_data.csv"
books_df.to_csv(csv_file_path, index = False)