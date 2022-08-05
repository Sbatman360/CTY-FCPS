def caesarshift(intext, key):
  outtext = []
  for i in range(0, len(intext)):
    val = ord(intext[i]) + key
    if (val < 91 and  val > 64) or (val < 123 and val > 96):
      outtext.append(chr(val))
    else:
      outtext.append(chr(val-26))
  return''.join(outtext)

import datetime
import calendar
def friday(month, year):
  list = []
  for i in range(10): 
    date = datetime.date(i + year, month, 13)
  if(date.strftime("%a") == "Fri"):
    list.append(i)
  else:
    pass
  
text = 'this is a sentence'
key = 3
date = '10/13/2007'

def encoder(intext, date):
  
  outtext = []
  key = ord(intext[-1]) + friday(int(date[:2]), int(date[-4:]))[0]
  for i in range(0, len(intext)):
    val = ord(intext[i]) + key
    if (val < 91 and  val > 64) or (val < 123 and val > 96):
      outtext.append(chr(val))
    else:
      outtext.append(chr(val - 26))
  return''.join(outtext)

print(encoder(text, date))




