#Bu program Python3 ile yazilmistir.
import os
os.system("clear")
print("-" *50)
print()
print("1-) Veri Toplama")
print("2-) Saldırılari Araclari")
print("-" *50)

#1. Secim
secim=int(input("Secim: "))
if secim==1:
	print("""
	1-) IP Bilgileri
	2-) Server Hizli Tarama
	3-) Server Version Bilgileri
	4-) Exploit Arama
	5-) IP Sistem Zaafiyet Tespiti
	6-) Site Guvenlik Duvari Tespiti
	7-) OSR Framework ile Bilgi Toplama
	""")
	
	print("-" *50)
	secenek=int(input("Secim: "))
	if secenek==1:
		os.system("clear && figlet IP Bilgileri")
		ip=str(input("Hedef IP: "))
		print("-" *50)
		os.system("python3 araclar/IPGeoLocation/ipgeolocation.py -t " +ip)
	
	elif secenek==2:
		os.system("clear && figlet Server Hizli Tarama")
		print("Bu tarama nmap kullanilarak gerceklestirilmektedir.")
		print("-" *50)
		site=str(input("Site Adresi: "))
		os.system("nmap " +site)
		print("-" *50)
		
	elif secenek==3:
		os.system("clear && figlet Server Version Bilgileri")
		print("Bu tarama nmap kullanilarak gerceklestirilmektedir")
		print("-" *50)
		site=str(input("Site Adresi: "))
		print("-" *50)
		os.system("nmap -sS -sV " +site)
		
	elif secenek==4:
		calis=0
		os.system("clear && figlet Exploit Arama")
		print("-" *50)
		anahtarkelime=input("Anahtar Kelime: ")
		print("-" *50)
		os.system("serchsloit " +anahtarkelime)
		
	elif secenek==5:
		os.system("clear && figlet Zaafiyet Tespiti")
		print("Bu tarama niktonile gerceklestirilmektedir.")
		print("-" *50)
		ip=str(input("Hedef IP: "))
		print("-" *50)
		os.system("nikto -h " +ip)
		
	elif secenek==6:
		os.system("clear && figlet Guvenlik Duvari Tespiti")
		print("Bu tarama wafw00f araci kullanilarak gerceklestirilmektedir.")
		print("-" *50)
		site=str(input("Site Adresi: "))
		print("-" *50)
		os.system("wafw00f " +site)
	
	elif secenek==7:
		os.system("clear && figlet OSR Framework")
		print("OSR Framework ile Bilgi Toplama Aracına Hos Geldiniz.")
		print("-" *50)
		os.system("osrframework")
		
	elif secenek==8:
		os.system("clear && figlet Telefon Numarasi ile Bilgi Toplama")
		print("Bu arac icin PhoneInfoga kullanilmistir.")
		print("-" *50)
		os.system("git clone https://www.github.com/sundoandev/PhoneInfoga")

#2. Secim
elif secim==2:
	print("""
	1-) Kisiye Ozel Wordlist Olusturma
	2-) Word Press Hizli Tarama
	3-) Word Press Admin Panel Bulucu
	4-) Random MAC Adresi Alma
	5-) Elle MAC Adresi Degistirme
	6-) MAC Adresini Orjinale Dondurme
	7-) Internet Baglantisini Kesme
	""")
	print("*" *50)
	secenek=int(input("Secim: "))
	if secenek==1:
		os.system("clear && figlet Wordlist Olusturucu")
		print("-" *50)
		print("Kullanim parametreleri asagida listelenmistir...")
		os.system("wordliser --help")
		
	elif secenek==2:
		os.system("clear && figlet WP Hizli Tarama")
		print("*" *50)
		site=str(input("Site Adresi: "))
		print("*" *50)
		os.system("wpscan --url " +site)
		
	elif secenek==3:
		os.system("clear && figlet WP Admin Bulucu")
		print("*" *50)
		site=str(input("Site Adresi: "))
		print("*" *50)
		os.system("wpscan -url " +site + " --enumerate u")
		
	elif secenek==4:
		os.system("clear && figlet Random MAC")
		print("*" *50)
		print("""
		Aginiza hangisi ile baglaniyorsunuz?
		eth0 (Ethernet) , wlan0 (Wiriles) , diger
		""")
		bag=str(input("Ag Bagdastiriniz: "))
		print("*" *50)
		os.system("ifconfig " +bag + " down")
		os.system("macchanger -r " +bag)
		os.system("ifconfig " +bag + " up")
		print("MAC Adresiniz random bir degere atandi.")

	elif secenek==5:
		os.system("clear && figlet Elle MAC")
		print("*" *50)
		print("""
		Aginiza hangisi ile baglaniyorsunuz?
		eth0 (Ethernet) , wlan0 (Wiriles) , diger
		""")
		print("-" *50)
		bag=str(input("Ag Bagdastiriniz: "))
		print("*" *50)
		print()
		print("Ornek MAC Adresi:")
		print("1A:2B:3C:4D:5F:6G")
		print("*" *50)
		print()
		mac=str(input("MAC Girin: "))
		os.system("ifconfig " +bag + " down")
		os.system("macchanger --mac " +mac + " " +bag)
		os.system("ifconfig " +bag + " up")
		print("MAC Adresi manuel olarak degistirildi.")

	elif secenek==6:
		os.system("clear && figlet MAC Orjinale Dondurucu")
		print("-" *50)
		print("""
		Aginiza hangisi ile baglaniyorsunuz?
		eth0 (Ethernet) , wlan0 (Wiriles) , diger
		""")
		print("-" *50)
		bag=str(input("Ag Bagdastiriniz: "))
		os.system("ifconfig " +bag + " down")
		os.system("macchanger -p " +bag)
		os.system("ifconfig " +bag + " up")
		print("*" *50)
		print("MAC  Adresi orjinale dondu.")
		print("*" *50)

	elif secenek==7:
		os.system("clear && figlet Internet Kesme")
		print("Bu arac icin kickthemout kullanilmistir.")
		print("*" *50)
		print()
		os.system("clear && sudo python3 araclar/kickthemout/kickthemout.py")		

	else:
		print("Hatali secim yaptiniz:( ")
		
else:
	print("Hatali secim yaptiniz:(")