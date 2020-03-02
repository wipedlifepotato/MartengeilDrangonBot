from config.config import config
from random import randint
import time
from splinter import Browser #https://github.com/mozilla/geckodriver/releases/

def logging(brows,sleep=10): # for captcha
   while brows.find_by_id('email'):
    brows.find_by_id('email').first.value= config.email
    brows.find_by_id('pass').first.value = config.passw
    brows.find_by_id('login_button').first.click()
    time.sleep(sleep)
    

def getEdit(b):
 return b.find_by_id("im_editable"+config.dialog).first 

def getMessages(b):
 tmp = b.find_by_xpath('//div[contains(@class, "im-mess--text")]')
 print("msgs")
 print(tmp)
 return tmp
 
def doSend(b):
 b.execute_script('''document.getElementsByClassName('im-send-btn')[1].click()''')

def doAction(fun, b, sleep=5):
 print("run "+str(fun))
 print('with param' + str(b))
 tmp=fun(b)
 #print("do sleeping in "+str(sleep) )
 if fun != getEdit: time.sleep(sleep)
 return tmp




 
class ob:
 def __init__(self, brows):
  self.brows=brows
  self.edit=doAction( getEdit, brows ) 
 def sendMsg(self,msg):
  self.edit.value=msg
  time.sleep(3)
  print("send msg: "+msg)
  print("edit: "+str(self.edit) )
  doAction( doSend, self.brows )

class worker(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def getBisMoney(self):
  super().sendMsg("бизнес снять")


class youtube(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def recordVideo(self):
  super().sendMsg("снять видео")
 def recordMoney(self):
  super().sendMsg("снять рекламу")
 def startStream(self):
  super().sendMsg("начать стрим")

class bitcoins(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def get(self):
  super().sendMsg("ферма")
 def sell(self):
  super().sendMsg("продать биткоин")

class hack(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def do(self):
  super().sendMsg("хакнуть")
 

class detective(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def do(self):
  super().sendMsg("детектив")
  super().sendMsg("дверь %d " % randint(1,3) )

class casino(ob):
 def __init__(self, brows):
  super().__init__(brows)
 def do(self,sum):
  super().sendMsg("казино %dк" % sum)
 def captcha(self, code, num):
  super().sendMsg("капча %d" % code[num+1])
#class Mergendaizer(worker):

class Events:
 def hour_passed(self):
  if time.time() - self.lasttime >= 60*60: return True
  return False

 def __init__(self, brows):
   self.work=worker(brows)
   self.tube=youtube(brows)
   self.bitc=bitcoins(brows)
   self.h = hack(brows)
   self.det=detective(brows)
   self.casino = casino(brows)
   self.brows = brows
   self.lasttime=0
 def doing( self ):
  money=1
  infirst=True
  while True:
   if self.hour_passed() :
    self.work.getBisMoney()
    self.tube.recordMoney()
    self.tube.startStream()
    self.bitc.get()
    self.h.do()
    self.det.do() 
    self.lasttime=time.time() 
   else:
    msgs=getMessages(self.brows)
    #print(msgs)
    #while True: pass
   # tmp=[] # do reversing...
    #print(msgs)
    msg=msgs[len(msgs)-1]
    #for msg in msgs[len(msgs)-3:len(msgs)-1]: # get last 3 mesagess
    print("msg:")
    print(msg.text)
    if "подозрительная активность" in msg.text:
     tmp=msg.text.split(' ')
     el=0
     for t in tmp:
      if "капча" in t:
       el=el
       break
      el=el+1
     self.casino.captcha(self, tmp, el)
       
    if "выигрыш" in msg.text:
     money=1
     self.casino.do(money)
    elif "проигрыш" in msg.text or "сгорела" in msg.text:
     money=money*2
     self.casino.do(money)
    else:
     if infirst: 
      self.casino.do(money)
      infirst=False
     else:
      for msg in msgs[len(msgs)-3:len(msgs)-1]:
       if "выигрыш" in msg.text:
        money=1
        self.casino.do(money)
        break
       elif "проигрыш" in msg.text or "сгорела" in msg.text:
        money=money*2
        self.casino.do(money)
        break
       

    print("----")
    print("?")
     
    pass #todo casino
  

def main():
 #brows=Browser()
 try:
  print("Start browser")
  with Browser() as brows: #user_agent=config.getRandUserAgent()) as brows:
   
   brows.visit(config.addr+config.dialog)
   print("do logging")
   logging(brows)
   brows.visit(config.addr+config.dialog)
   print("waiting 10 seconds...")
   time.sleep(10)
   print("...bot inited...")
   #print("send help")
   #print("getEdit")
   edit = doAction( getEdit, brows )
   edit.value="помощь"
   time.sleep(3)
   #print("DoSend")
   doAction( doSend, brows )
   #print("is works?")
#   while True: pass
   #print("class check")
   events = Events(brows)
   events.doing()
 except Exception(e):
  print ( str(e) )

main()
