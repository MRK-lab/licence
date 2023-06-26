''' LİSANSLAMA '''

import sys # programı kapatmak için
from datetime import datetime # anlık zamanı alabilmemiz için

lisans_bitis_tarihi="03.10.2023"
lisans_bitis_tarihi_liste=lisans_bitis_tarihi.split(".") # gün, ay, yıl ayırmak için
bitis_gun=int(lisans_bitis_tarihi_liste[0])
bitis_ay=int(lisans_bitis_tarihi_liste[1])
bitis_yil=int(lisans_bitis_tarihi_liste[2])

anlık_tarih=datetime.now() # anlık zaman

gun=anlık_tarih.day
ay=anlık_tarih.month
yil=anlık_tarih.year


if yil==bitis_yil:
    if ay==bitis_ay:
        if gun==bitis_gun:
            print("Yarın lisansınızın süresi doluyor.\n"
                  "İletişim: https://www.teknolocked.com/")
        elif gun>bitis_gun:
            print("Lisans süreniz doldu.\n"
                  "İletişim: https://www.teknolocked.com/")
            sys.exit()
        else:
            print("Lisans süreniz dolmak üzere.\n"
                  "Son gün: ",bitis_gun)
    elif ay>bitis_ay:
        print("Lisans süreniz doldu.\n"
              "İletişim: https://www.teknolocked.com/")
        sys.exit()
    else:
        print(f"Bu yılın {bitis_ay}. ayında lisans süreniz doluyor.")
elif yil>bitis_yil:
    print("Lisans süreniz doldu.\n"
          "İletişim: https://www.teknolocked.com/")
    sys.exit()
else:
    print("TeknoLocked başarılar diler...")



