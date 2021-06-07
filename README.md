# GUILD-BOOMBER

 Discord Sunucu Patlatma Botu
 
 - [Discord Patlatma Botu](#GUILD-BOOMBER)
    - [Kurulum](#Kurulum)
    - [Eventler](#Eventler)
    - [Tavsiyeler](#Tavsiyeler)
    - [Discord hesabım](https://discord.com/users/788158033641078794)
 
 ![img](https://cdn.discordapp.com/attachments/839135788246630482/851407526222102548/Adsz.png)
    
    
# Neden Yayınlandı?
Canım sıkıldı yazdım amaçsız.

# Bilgilendirme
* *SAÇMA SAPAN SUNUCU KAVGALARINIZ BENİM SORUNUM DEĞİLDİR!*
* *Hesabınızın rate limite düşme riskine hazır olun eğer düşmesini istemiyorsanız heroku veya repl.it gibi yerlerden projeyi başlatın ama rate limite düşse bile 30 dakika düşüyor açılıyor ben yaşadım biliyorum.*
* *Projeyi paylaşırsanız adliyeye  sevk edilmiyonuz paylaşırsanız sikimde olmaz ama paylaşan net eziğin evladıdır.*
* *Projeyle ilgili sorunlarınız için bana  ulaşabilirsiniz.* [(CryonicX#4177)](https://discord.com/users/788158033641078794)
* *Son olarak Türkçem ile ultra çok komik esprilerinizi kendinize saklayın ben burada makale yazmıyorum.*

# Eventler
* Sunucudaki bütün kanallar ve rolleri siler.
* Kanallar ve Roller silindikten rol ve kanal oluşturur.
* Eğer sunucuda özel url varsa özel urlyi değiştirir.
* Sunucunun ismini ve profil resmini sürekli değiştirerek sunucuyu kırmızıya düşmesine yol açar.
* Sunucudaki herkesi banlar.
* Sunucudaki bütün emojileri siler.


# Tavsiyeler 
* 1 Tokenle pek bir şey yapmayı beklemeyin hesabınız rate limite düşer.
* +1 tokenden sonra vanity url çalma özelliği çalışır. Eğer sadece özel url veya özel bir kod yazrımak isterseniz bana ulaşabilirsiniz üşenmezsem yaparım BELKİ.
* Arkadaşlar sunucuyu boş yere patlatmayın emek sikmeyin döner dolaşır sizi bulur :) ya da bana ne amk ne yaparsanız yapın.


# Kurulum
* Öncelikle bilgisayarınızda python yüklenmiş olmalı eğer yoksa [buradan](https://www.python.org/downloads/) indirebilirsiniz.
* Kurulum aşamasında `add Python PATH` tickine basınız. ![img](https://media.discordapp.net/attachments/788834755613163560/851147317700198440/unknown.png)
* Projeyi zip halinde indirin ve bir klasöre çıkarın.
* Çıkardığınız klasördeki config klasörünün altındaki `set.json` adlı dosyayı açın ve içindekileri doğru bir biçimde doldurun.
  * `tokens`: Kullancağınız tokenlerdir en fazla 10 tokeni destekler arttırmak isterseniz bana yazarsanız. örnek = `["token1","token2","token3"]`
  * `bot?`: Eğer bot kullanıyorsan `true` kullanmıyorsan `false` yaz.
  * `herkesibanla`: Eğer botun ban atmasını istiyorsan `true` istemiyorsan `false` yaz.
  * `bütünrollerisil`: Eğer botun rolleri silmesini istiyorsan `true` istemiyorsan `false` yaz.
  * `bütünkanallarısil`: Eğer botun kanalları silmesini istiyorsan `true` istemiyorsan `false` yaz.
  * `butunemojilerisil`: Eğer botun emojileri silmesini istiyorsan `true` istemiyorsan `false` yaz. (Tavsiye etmem işlemi yavaşlatır)
  * `spamat`: Eğer botun kanallara spam atmasını istiyorsan `true` istemiyorsan `false` yaz. (Tavsiye etmem işlemi yavaşlatır)
  * `urlçal`: Eğer botun sunucuda özel url varsa değiştirmesini istiyorsan `true` istemiyorsan `false` yaz. (Elimde 30 boostluk bir sunucu olmadığı için denemesini yapmadım ama çalışır diye düşünüyorum.)
  * `patlatmamesajı:` Botu başlatma mesajıdır. örnek = Herhangi bir kanala patlat yazınca bot sunucuyu patlatmaya başlar.
  * `sunucu_vanity_url`: Sunucuda değiştireceğiniz özel urldir. örnek = "sunucu_vanity_url": "python"
  * `channel_name`: Bütün kanallar silindikten sonra oluşturulacak kanal isimleri.
  * `role_name`: Bütün roller silindikten sonra oluşturulacak kanal isimleri.
  * `sunucuismi`: Sunucu patlatma işlemi başladıktan sonra array sırasına göre değişecek sunucu isimleri. örnek = `["Bu","Sunucu","Patladı"]`
  * `spam_mesaj`: Kanallara atılacak spam mesajı.
  * `sunucu resmi`: Config klasörünün altındaki resimleri png formatıyla aynı isimle dosyaları yükleyin guild iconunu öyle değiştirin.
  * `sizinid`: Patlatma mesajını yazıcak kişinin idsini gir.
  * `guildid`: Sunucu idsi gir.
* Bunları doldurduktan sonra klasörünün içinde yeni bir terminal açin ve `pip install -r requirements.txt` yazarak modülleri indirin.
* Modülleri indirdikten sonra `CryonicX.vbs` isinli dosyayı açın.
* Patlatmak için sunucuda yetkiniz olması lazım aksi taktirde hiçbir şey yapamazsınız. Eğer Bot kullanıyorsanız botun intentlerini açmayı unutmayın. (Developer Portal > Applications > Botun Profili > Bot Sekmesi > Sayfanın Aşağısındaki Intent tikleri)
* Her şeyi açıkladım kuramayanın zihinsel sorunları vardır. Sorun çıkarsa CryonicX#4177 yazın.