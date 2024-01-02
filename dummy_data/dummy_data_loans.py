from faker import Faker
from datetime import datetime, timedelta
import pandas as pd 
import secrets
import random


fake = Faker()

# Fungsi untuk membuat data dummy peminjaman
def generate_loan_data(loan_id, user_id, book_id):
    loan_date = fake.date_this_year()
    due_date = loan_date + timedelta(days=14)
    return_date = None  # Akan diisi jika buku dikembalikan

    # Peluang 50% buku dikembalikan lebih awal
    if random.choice([True, False]):
        return_date = fake.date_between(start_date=loan_date, end_date=due_date)

    return {
        'loan_id': loan_id,
        'user_id': user_id,
        'book_id': book_id,
        'loan_date': loan_date,
        'due_date': due_date,
        'return_date': return_date
    }

# Membuat 200 data dummy user
jumlah_users = 200
user_ids = list(range(1, jumlah_users + 1))

# Membuat 200 data dummy book
jumlah_books = 200
book_ids = list(range(1, jumlah_books + 1))

# Membuat 200 data dummy loans
jumlah_loans = 200
data_loans_dummy = []

for loan_id in range(1, jumlah_loans + 1):
    user_id = random.choice(user_ids)

    # Memastikan pengguna tidak meminjam lebih dari 2 buku
    existing_user_loans = [loan['book_id'] for loan in data_loans_dummy if loan['user_id'] == user_id]
    available_book_ids = list(set(book_ids) - set(existing_user_loans))

    if len(available_book_ids) > 0:
        # Meminjam 2 buku secara acak
        borrowed_books = random.sample(available_book_ids, min(2, len(available_book_ids)))

        for book_id in borrowed_books:
            data_loans_dummy.append(generate_loan_data(loan_id, user_id, book_id))

# Membuat DataFrame dari data dummy loans
df_loans = pd.DataFrame(data_loans_dummy)

# Menampilkan DataFrame loans
print(df_loans)

# Menyimpan DataFrame loans ke file CSV
df_loans.to_csv('dummy_data_loans_fix.csv', index=False)
