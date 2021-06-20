#!/usr/bin/python
#Sihirli 8 top türkçe telegram oyunu.
import telepot,telepot.loop,telepot.namedtuple
import sqlite3,threading,os,time,pprint,random,validators,base64,json,subprocess
import configparser as c

nya=0
rlko=0
c0="Bunu şu an sana söylememem daha hayırlı."
c1="Kesinlikle, öyle."
c2="Öyle olması gerekli."
c3="Öyle olmasına karar verildi."
c4="Şüphesiz ki, öyle."
c5="Gördüğüm kadarıyla, evet."
c6="Muhtemelen."
c7="Kaderin öyle."
c8="Güvenmemelisin."
c9="Cevabım, Evet!"
c10="Cevabım, Hayır!"
c11="Yapabilirsin, kendine daha çok güvenmelisin!"
c12="Gördüğüm kadarıyla, yapmamalısın."
c13="Gerçekten şüpheliyim."
c14="Şu an bu cevabı duymaya hazır değilsin. Gerçekten duymak istediğinde yeniden sor."
c15="Pek iyi gözükmüyor."
c16="Gerçekten mantıklı gözükmüyor."
c17="Buna şu anda cevap veremem."
c18="Lütfen başka bir gün tekrar sor."
cevaplar=[c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18]
xTOXEN="98123712:DIOQWADMQWADKMQWDQWLDKQMW" #Buraya kendi toxeninizi yazın.
db_exists=os.path.exists("database.db")
conn=sqlite3.connect("database.db", check_same_thread=False)
cur=conn.cursor()
if not db_exists:
    cur.execute("CREATE TABLE user (id INT, username CHAR(50), firstname VARCHAR(51),lastname CHAR(52))")
    conn.commit()
    del cur
set_exists=os.path.exists("degerler.txt")
if not set_exists:
    cp = c.RawConfigParser()
    cp.add_section('veri')
    cp.set('veri', 'TOXEN', xTOXEN)
    setup = open('degerler.txt', 'w')
    cp.write(setup)
    setup.close()
nya = c.RawConfigParser()
nya.read('degerler.txt')
TOXEN = nya['veri'] ['TOXEN']
bot=telepot.Bot(TOXEN)

def handle(msg):
   try:
    pprint.pprint(msg)
    cur=conn.cursor()
    et="@"
    userid=msg["from"]["id"]
    chatid=msg["chat"]["id"]
    try:
        username=et+msg["from"]["username"]
    except:
        username=""
    try:
        firstname=msg["from"]["first_name"]
    except:
        firstname=""
    try:
        lastname=msg["from"]["last_name"]
    except:
        lastname=""
    data=""
    if "data" in msg.keys():
        data=msg["data"]
    text=""
    if "document" in msg.keys():
        text="FileID:"+msg["document"]["file_id"]
    elif "photo" in msg.keys():
        text="FileID:"+msg["photo"][0]["file_id"]
    else:
        text=msg["text"]
    if text.startswith("/8top") or text.startswith("/8ball") or text.startswith("/cevap") or text.startswith("/cevapla") or text.startswith("/8"):
        sonuc=random.choice(cevaplar)
        bot.sendMessage(chatid,f"{sonuc}")
    elif text=="/yardim":
        bot.sendMessage(chatid,"Nyarlko tarafından yazılmıştır. https://github.com/ny4rlk0/Telegram-Sihirli-8-Top-Tahmin-Oyunu/")
        bot.sendMessage(chatid,"Komutlar /yardim, /8top, /8ball, /cevap, /cevapla Yapabilir miyim?, /8 Soru?")
   except:
    pass
if __name__=="__main__":
    telepot.loop.MessageLoop(bot,handle).run_forever()