from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random


fake = Faker()

# Fungsi untuk membuat data dummy queue
def generate_queue_data(queue_id, user_id, book_id):
    queue_start = fake.date_time_this_decade(before_now=True, after_now=False)
    return {
        'queue_id': queue_id,
        'queue_start': queue_start,
        'user_id': user_id,
        'book_id': book_id
    }

# Membuat 300 data dummy user
jumlah_users = 300
user_ids = list(range(1, jumlah_users + 1))

# Membuat 200 data dummy book
jumlah_books = 200
book_ids = list(range(1, jumlah_books + 1))

# Membuat 300 pengguna dan 200 buku
data_queue_dummy = []

for queue_id in range(1, min(jumlah_users, jumlah_books) + 1):
    user_id = random.choice(user_ids)
    book_id = random.choice(book_ids)
    data_queue_dummy.append(generate_queue_data(queue_id, user_id, book_id))

# Membuat DataFrame dari data dummy queue
df_queue = pd.DataFrame(data_queue_dummy)

# Menampilkan DataFrame queue
# print(df_queue)

# Menyimpan DataFrame queue ke file CSV
df_queue.to_csv('dummy_data_queues.csv', index=False)
