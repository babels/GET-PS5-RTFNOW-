#_*_coding: utf-8_*_
from time import sleep
from random import shuffle

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sendgridkey = "YOURKEYHERE"
fxprofile   =  "C:\Users\\User\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\1gnozqko.default-release"

### prototype  [ 'site', 'regex', attribute, value, ismatch ]
trg1  = [ 'https://www.target.com/p/playstation-5-console/-/A-81114595', "//*[@data-test='soldOutBlock']", ["innerHTML", "Sold out"], 0]
trg2  = [ 'https://www.target.com/p/playstation-5-console/-/A-81114596', "//*[@data-test='soldOutBlock']", ["innerHTML", "Sold out"], 0]
trg3  = [ 'https://www.target.com/p/xbox-series-x-console/-/A-80790841', "//*[@data-test='soldOutBlock']", ["innerHTML", "Sold out"], 0]

wal1  = [ 'https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815', "//*[@class='prod-blitz-copy-message']", ["innerHTML", "out of stock"], 0]
wal2  = [ 'https://www.walmart.com/ip/PlayStation-5-Console/363472942', "//*[@class='prod-blitz-copy-message']", ["innerHTML", "out of stock"], 0]
wal3  = [ 'https://www.walmart.com/ip/Xbox-Series-X/443574645', "//*[@class='prod-blitz-copy-message']", ["innerHTML", "out of stock"], 0]

gst1  = [ 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5-digital-edition/11108141.html?condition=New', "//*[@class='add-to-cart btn btn-primary ']", ["innerHTML", "Not Available"], 0]
gst2  = [ 'https://www.gamestop.com/video-games/playstation-5/consoles/products/playstation-5/11108140.html?condition=New', "//*[@class='add-to-cart btn btn-primary ']", ["innerHTML", "Not Available"], 0]
gst3  = [ 'https://www.gamestop.com/video-games/xbox-series-x/consoles/products/xbox-series-x/B224744V.html', "//*[@class='add-to-cart btn btn-primary ']", ["innerHTML", "Not Available"], 0]


bby1  = [ 'https://www.bestbuy.com/site/sony-playstation-5-console/6426149.p?skuId=6426149', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby2  = [ 'https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby3  = [ 'https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby4  = [ 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby5  = [ 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby6  = [ 'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-gaming-oc-8g-gddr6-pci-express-4-0-graphics-card-black/6437909.p?skuId=6437909', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby7  = [ 'https://www.bestbuy.com/site/gigabyte-geforce-rtx-3070-eagle-8g-gddr6-pci-express-4-0-graphics-card-black/6437912.p?skuId=6437912', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby8  = [ 'https://www.bestbuy.com/site/msi-nvidia-geforce-rtx-3070-ventus-3x-oc-bv-8gb-gddr6-pci-express-4-0-graphics-card-black/6438278.p?skuId=6438278', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby9  = [ 'https://www.bestbuy.com/site/evga-geforce-rtx-3070-xc3-ultra-gaming-8gb-gddr6-pci-express-4-0-graphics-card/6439299.p?skuId=6439299', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby10 = [ 'https://www.bestbuy.com/site/asus-tuf-rtx3070-8gb-gddr6-pci-express-4-0-graphics-card-black/6439128.p?skuId=6439128', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]
bby11 = [ 'https://www.bestbuy.com/site/pny-geforce-rtx-3070-8gb-dual-fan-graphics-card/6432654.p?skuId=6432654', "//*[@class='btn btn-disabled btn-lg btn-block add-to-cart-button']", ["innerHTML", "Sold Out"], 0]


adr1 = [ 'https://www.adorama.com/so3005718.html?sterm=Qq%3A2qy1fgxyLUMYwUx0Mo36NUkEWF8wFr2%3AfxE0&utm_source=rflaid913479', "//*[@class='stock-special stock']",  ["innerHTML", "Currently, we are not"], 0]
adr2 = [ 'https://www.adorama.com/so3005719.html?sterm=Qq%3A2qy1fgxyLUMYwUx0Mo36NUkEWF53tr2%3AfxE0&utm_source=rflaid913479', "//*[@class='stock-special stock']",  ["innerHTML", "Currently, we are not"], 0]
#adr3 = [ 'https://www.adorama.com/xbrrt00001.html', "//*[@class='stock-special stock']",  ["innerHTML", "Currently, we are not"], 0]


amz1 = [ 'https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG?tag=georiot-us-default-20&ascsubtag=tomsguide-us-5451696863336828000-20&geniuslink=true', "//*[@class='a-size-medium a-color-price']", ["innerHTML", "Currently unavailable"], 0]
amz2 = [ 'https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62?tag=georiot-us-default-20&ascsubtag=tomsguide-us-1019020405428820700-20&geniuslink=true', "//*[@class='a-size-medium a-color-price']", ["innerHTML", "Currently unavailable"], 0]
#amz3 = [ 'https://www.amazon.com/Xbox-X/dp/B08H75RTZ8/ref=sr_1_8?dchild=1&keywords=xbox+series+x&qid=1612883404&sr=8-8', "//*[@class='a-size-medium a-color-price']", ["innerHTML", "Currently unavailable"], 0]

# all urls to search
sites = [ trg1, trg2, trg3, wal1, wal2, wal3, gst1, gst2, gst3, bby1, bby2, bby3, adr1, adr2, amz1, amz2 ]
shuffle( sites )

# start web browser

options = Options()
options.headless = True
firefox_profile = webdriver.FirefoxProfile( fxprofile )
firefox_profile.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
browser = webdriver.Firefox(options=options, firefox_profile=firefox_profile)


# verbose, 0==none, 1==stdout, 2==logfile
vbs  =  1
lfp  =  'log.txt'


def dlog( log ):

  log = str( log ).encode('utf-8')

  if( vbs == 1 ):
     print("%s" % log)


def sndmsg( sbj, txt ):

  msg = Mail(
    from_email    =  'iwantps5now@gmail.com',         # sendgrid single user email
    to_emails     =  'phuckguoogle@gmail.com',
    subject       =  sbj,
    html_content  =  txt )

  try:
    sg = SendGridAPIClient( sendgridkey )
    #response = sg.send(msg)
    sg.send(msg)
    return
    #dlog(response.status_code)
    #dlog(response.body)
    #dlog(response.headers)

  except Exception as e:
    dlog("[!] %s" % str(e) )


def getps5now():

  for site in sites:

     url  =  site[0]
     cls  =  site[1]
     src  =  site[2]

     atr  =  src[0]
     vlu  =  src[1]

     prg  =  site[3]

     #try:
     browser.get(url)
     #except:
     #  dlog("[!] Error fetching %s" % url)
     #  sleep(60)
     #  break

     #html = browser.page_source
     sleep(2)

     #dlog("finding element %s" % cls)

     for i in browser.find_elements_by_xpath(cls):
       #dlog("seeking attribute %s for value %s" % (atr, vlu) )

       val = i.get_attribute(atr)

       if not(val):
          txt = str( "Value error %s from %s" % (val, url) )
          dlog("[!] no value %s" % txt)
          sndmsg("[!] Missing Token", txt)

       if( vlu in val ):
          #dlog("[+] we have value")

          if( prg ):
            txt = str( """WE FOUND A PS5! <a href="%s">%s</a>""" % (url, url) )
            sndmsg("WINNER!", txt)
            dlog("[+] WINNER at %s" % url)
            break

          else:
            #dlog("[-] no match1")
            break

       else:
          #dlog("[-] no match2")

          if( prg ):
            #print("[-] We did not find what we were looking for")
            break

          else:
            txt = str( """WE FOUND A PS5! <a href="%s">%s</a>""" % (url, url) )
            sndmsg("WINNER!", txt)
            dlog("[+] WINNER at %s" % url)
            break


def getps5():
  while(1==1):
     dlog("[+] Its out there some where...")
     getps5now()

  browser.close()


if __name__ == "__main__":
  getps5()
