from random import randint
#
class config:
 addr = "https://vk.com/im?sel="
 dialog = "-181430212"
 email="potatolivingstonei2p@gmail.com"
 passw="c6d3240727de6add1deb65a97971758e8ccbf94498d7bd9cd3b8bd2ffb81db23a0e07f049eb27af7ef2836d768480248a2434944a840f0381c72350c9c4eae9b"
 def getRandUserAgent(notNeed=True):
  
  user_agents = ""
  tmp = " "
  f=open('user_agents.txt')
  while tmp != "":
   user_agents = user_agents+f.read(2048)
  user_agents.split(';')
  return user_agents[randint(0,len(user_agents)-1)]

