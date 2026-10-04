import socket

print("\n Beta Banner Okuyucu")

bannerlar = {}
hepsi = []
acık = []
son = []

hedef = input("Hangi hedefi taramak istersiniz?")

baslangıc_portu = int(input("Hangi portu taramak istersiniz ilk olarak?"))

bitis_portu = int(input("Bitiş olarak hangi port'u taramak istersiniz?"))

for port in range(baslangıc_portu, bitis_portu + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)
    sonuc = s.connect_ex((hedef, port))

    hepsi.append(port)
    
    if sonuc == 0:
        acık.append(port)
        print("Açıklar =", acık)
        istek = "GET / HTTP/1.1\r\nHost:" + hedef + "\r\nConnection: close\r\n\r\n"
        baytlar = istek.encode()
        s.sendall(baytlar)
        try: 
            veri = s.recv(1024)
        except TimeoutError:
            print("Sunucu zamanında yanıt veremedi.")
        else:
            metin = veri.decode()
            satirlar = metin.split("\r\n")
            for i in satirlar:
                if i.startswith("Server:"):
                    bannerlar[port] = i
            print(bannerlar)
    s.close()

x = int(input("Kapalıları görmek için '9' harfine basın."))
if x == 9:
    for a in hepsi:
        if a not in acık:
            son.append(a)
    print("Kapalılar =", son)



                  

            



