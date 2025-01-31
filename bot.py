import os
from eth_account import Account

def get_unique_filename(base_name):
    """Mendapatkan nama file unik dengan menambahkan angka urutan jika perlu."""
    counter = 1
    new_name = base_name
    while os.path.exists(new_name):
        new_name = f"{base_name.split('.')[0]}_{counter}.{base_name.split('.')[1]}"
        counter += 1
    return new_name

def create_accounts(num_accounts):
    # Nama file untuk menyimpan alamat dan private key
    address_file = get_unique_filename("evm_addresses.txt")
    private_key_file = get_unique_filename("evm_private_keys.txt")

    # Membuka file untuk menulis
    with open(address_file, "w") as addr_file, open(private_key_file, "w") as key_file:
        # Loop untuk membuat akun
        for _ in range(num_accounts):
            account = Account.create()  # Membuat akun baru
            addr_file.write(f"{account.address}\n")  # Menyimpan alamat publik
            key_file.write(f"{account.key.hex()}\n")  # Menyimpan private key dalam format hex

    print(f"{num_accounts} alamat EVM berhasil dibuat.")
    print(f"Alamat disimpan di '{address_file}', dan private key di '{private_key_file}'.")

def main():
    while True:
        try:
            num_accounts = int(input("Masukkan jumlah akun yang ingin dibuat (atau ketik 0 untuk keluar): "))
            if num_accounts == 0:
                print("Keluar dari program.")
                break
            elif num_accounts < 0:
                print("Silakan masukkan angka positif.")
                continue
            
            create_accounts(num_accounts)
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()
