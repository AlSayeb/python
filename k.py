import telebot,random
from telebot import types
import py_compile,json,base64, marshal, zlib,os
botf = True

data_json = {

	"base64": "#TeleGram: @ADIL721\nimport base64\nexec(base64.b64decode(",
	
	"base16": "#TeleGram: @ADIL721\nimport base64\nexec(base64.b16decode(",

	"base32": "#TeleGram: @ADIL721\nimport base64\nexec(base64.b32decode(",	
	
	"marshal":"#TeleGram: @ADIL721\nimport marshal\nexec(marshal.loads(",
	
	"zlib":"#TeleGram: @ADIL721\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode(",
	
	"lambda":"#TeleGram: @ADIL721\nexec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'<https://t.me/ADIL721','exec'))("
            }
## code Shayeb ! ## 
class en():
    def mr(name_file):
        file = open(name_file, "r").read()
        print(file)
        en = compile(file, '<Shayeb>', 'exec')
        enc = marshal.dumps(en)
        da = str(data_json["marshal"])
        data = (f"{da}{enc}))")
        return data
    def b64(name_file):
        file = open(name_file, "r").read()
        Enc = base64.b64encode(file.encode('UTF-8')).decode('ascii')
        da = str(data_json["base64"])
        data = (f"{da}'{Enc}'))")
        return data
    def lambdaS(name_file):
        file = open(name_file, "r").read()
        print(file)
        en=repr(zlib.compress(file.encode('utf-8')))
        da = str(data_json["lambda"])
        cmb=(f"{da}{en},compile))")
        return cmb
    def zi(name_file):
        file = open(name_file, "r").read()
        co=compile(file,"ru",'exec')
        mr=marshal.dumps(co)
        zl = zlib.compress(mr)
        enc = str(base64.b64encode(zl))
        da = str(data_json["zlib"])
        data = (f"{da}{enc}))))")
        return data
#### code marko
token = "5011659331:AAEG7gdCmfFi213yCTXc9gGxpipBgsB-54s" # input(" [~] Entar Tokin bot : ")
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def stagrt(message): 
    name_user = message.chat.first_name
    text=f"""
مرحبا بك عزيزي 🖇️{name_user}🖇️
في بوت تشفير ملفات البايثون..
الان وبامكانك التشفير بكل سهوله 🌿
للتعرف علئ انواع التشفير المتوفره حاليا
ارسل الان ← /lock → 📨
-لمتابعتي← @ADIL721 → 🌏
- - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Welcome dear....
in the python file encryption bot.. Now you can encrypt with ease 🌿 To know the types of encryption currently available send now → /lock → 📨
follow me → @ADIL721 → 🌏
"""
    bot.send_message(message.chat.id, text =f"*{text}*",parse_mode="markdown")


@bot.message_handler(commands=['lock'])
def start_encode(message):
    call1 = types.InlineKeyboardButton(text = "base64 🔐", callback_data = 'base64')
    call2 = types.InlineKeyboardButton(text = "lambda 🔐", callback_data = 'lambda')
    call3 = types.InlineKeyboardButton(text = "marshal 🔐", callback_data = 'marshal')
    call4 = types.InlineKeyboardButton(text = "zlib 🔐", callback_data = 'zlib')
    call6 = types.InlineKeyboardButton(text = "Programmer Help 🗣️", url= "https://t.me/TOASEL7_bot")
    Keyy = types.InlineKeyboardMarkup()
    Keyy.row_width = 1
    Keyy.add(call1,call2,call3,call4,call6)
    bot.send_message(message.chat.id, text=f"*حسنا عزيزي المستخدم ❤️\nاختر من الاسفل نوع التشفير المراد\nمتوفر عده تشفيرات في الاسفل 🗣️*",parse_mode="markdown",reply_markup=Keyy)
    
@bot.callback_query_handler(func=lambda call: True)
def Marko_call(call):
    if call.data =="base64":
        Marko_en(call.message)
    elif call.data == "lambda":
        Marko_cc(call.message)
    elif call.data == "marshal":
        Marko_er(call.message)
    elif call.data == "zlib":
        Marko_et(call.message)


def Marko_en(message):
    bot.send_message(message.chat.id, text ="*حسنا عزيزي تشفيرك هو base64 ارسل الملف الان 🖇️*",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.b64(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"Shayeb.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 
                

def Marko_cc(message):
    bot.send_message(message.chat.id, text ="*حسنا عزيزي تشفيرك هو lambda ارسل الملف الان 🖇️*",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.lambdaS(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"Shayeb.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 

def Marko_er(message):
    bot.send_message(message.chat.id, text ="*حسنا عزيزي تشفيرك هو marshal ارسل الملف الان 🖇️*",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.mr(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"Shayeb.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 


def Marko_et(message):
    bot.send_message(message.chat.id, text ="*حسنا عزيزي تشفيرك هو Zlib ارسل الملف الان 🖇️*",parse_mode="markdown")
    @bot.message_handler(content_types=['document'])
    def save(message):
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        ran = 'a'+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)+random.choice(chars)
        name_file = str(ran+'.py')
        with open(name_file, 'wb') as new_file:
            new_file.write(downloaded_file)
            new_file.close()
            msg = message.text
            Encs = en.zi(name_file)
            path_y=str(name_file.split(".")[0])
            name_file_tele = str(path_y+"Shayeb.py")
            with open(name_file_tele, 'a') as x:
                x.write(f"{Encs}")
            doc = open(name_file_tele,'rb') 
            bot.send_document(message.chat.id,doc)
            os.system(f"rm -f {name_file}") 
            os.system(f"rm -f {name_file_tele}") 
bot.polling(False)

