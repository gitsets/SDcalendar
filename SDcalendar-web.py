import calendar
import random
from PIL import Image,ImageDraw,ImageFont
import PIL
import zlib
name='haha'
random.seed(zlib.crc32(bytes(name,encoding='utf-8')))
def cogen():
    sr=random.randrange(190,220)
    sg=random.randrange(190,220)
    sb=random.randrange(220,250)
    co1=(sr,sg,sb)
    co2=(sr-50,sg-50,sb-50)
    co3=(sr-100,sg-100,sb-100)
    return (co1,co2,co3)
list =open(r'C:\Users\Xiao\Documents\Gits\Notebook\SDCalendar\list.md',encoding='UTF-8').readlines()
verb =open(r'C:\Users\Xiao\Documents\Gits\Notebook\SDCalendar\verb.md',encoding='UTF-8').readlines()
for i in range(0,len(verb)):
    verb[i]=verb[i].replace("\n","")
noun =open(r'C:\Users\Xiao\Documents\Gits\Notebook\SDCalendar\noun.md',encoding='UTF-8').readlines()
fo=ImageFont.truetype('slideyouran-Regular.ttf',60)
fo2=ImageFont.truetype('slideyouran-Regular.ttf',20)
fo3=ImageFont.truetype('slideyouran-Regular.ttf',120)
for i in range (5,6):
    for j in range(1,calendar.monthrange(2020,i)[1]+1):
        day=Image.new('RGBA',(240,320))
        pen=ImageDraw.Draw(day)
        color=cogen()
        pen.rectangle((10,10,230,310),outline=color[0],width=3,fill=color[0])
        pen.rectangle((20,30,210,150),fill="white",outline=color[0],width=2)
        pen.text((50,220),"宜"+random.choice(list),font=fo2,fill=color[2])
        pen.text((50,250),"忌"+random.choice(verb)+random.choice(noun),font=fo2,fill=color[2])
        pen.text((30,20),calendar.month_name[i],font=fo,fill=color[1])
        pen.text((90,20),str(j),font=fo3,fill=color[1])
        pen.text((10,290),name,font=fo2,fill="white")
        filename=name+"-"+calendar.month_name[i]+" "+str(j)+".png"
        day.save(filename)
