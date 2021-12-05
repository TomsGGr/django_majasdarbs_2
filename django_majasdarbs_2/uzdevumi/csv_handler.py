import csv
from .models import Juzeru_klase


def read_and_decode_csv(file, encoding='utf-8'):
    """Dekodē un izlasa CSV failu"""

    decoded_file = file.read().decode(encoding).splitlines()
    return decoded_file



def csv_rows_to_db(decoded_csv_file):
    """Katru CSV rindu pārvērš par dictionary, no tās izveido jūzeri un ieraksta datubāzē"""

    csv_dict = csv.DictReader(decoded_csv_file)

    for row in csv_dict:
        user = Juzeru_klase(  # atslēgas = headers no CSV faila
            user=row['username'],
            email=row['email'],
        )
        user.save()  # -----  saglabā jūzeri datubāzē