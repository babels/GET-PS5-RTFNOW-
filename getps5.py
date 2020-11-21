### WARNING: Running this script outside of the USA "Free Zone" may not be permitted by your Locale.
###          Pleasae check and abide all ordinces ever

### NOTICE:  The following script is freely distributed under the Dread License Roberts.
###          If it finds itself used to turn a profit, cused ye will be... cursed

### Given the spacing, indentation, possible color highlighting and auspicious use of
### one to three letter variables you may have the impression that I spent years learning to program
### just to basterdize well known concepts for your personal benifit and or detriment. You'd be right!

### INSTRUCTIONS: https://www.youtube.com/watch?v=ewRjZoRtu0Y


from  urllib2  import  Request, urlopen
from  datetime import  datetime
from  random   import  shuffle
from  time     import  sleep
from  os       import  path, popen

join      =  path.join
sep       =  path.sep
exist     =  path.exists

### Global Variable - Set to Zero to Disable

LOG       =  1
LOGSCRN   =  1
VERBOSE   =  1

### With great power comes great responsibility
DIALOUT   =  1
TXTNUM    =  "4155555555"
CUSMSG    =  "OMFGG_PS5_WOOT" # no spaces


drv       =  "C:"
adb       =  str( "Program' 'Files/Unity/Hub/Editor/2019.4.9f1/Editor/Data/PlaybackEngines/AndroidPlayer/SDK/platform-tools/adb.exe" )

adb       = join( drv, adb )




urls = [
         [ "https://www.newegg.com/p/N82E16868110292", "SOLD OUT", "Newegg", 1 ],
         [ "https://www.newegg.com/p/N82E16868110291", "SOLD OUT", "Newegg", 1 ],
         [ "https://www.newegg.com/p/N82E16868110293", "SOLD OUT", "Newegg", 1 ],

         [ "https://www.walmart.com/ip/Sony-PlayStation-5-Digital-Edition/493824815", "now available at", "Walmart", 1],
         [ "https://www.walmart.com/ip/PlayStation-5-Console/363472942", "now available at", "Walmart", 1],

         [ 'https://www.target.com/p/playstation-5-console/-/A-81114595', 'shouldShowCurbsideMessage":false' ,'Target', 1],
         [ 'https://www.target.com/p/playstation-5-digital-edition-console/-/A-81114596', 'shouldShowCurbsideMessage":false' ,'Target', 1],

         [ "https://www.amazon.com/PlayStation-5-Console/dp/B08FC5L3RG", "Currently unavailable.", "Amazon", 1],
         [ "https://www.amazon.com/PlayStation-5-Digital/dp/B08FC6MR62", "Currently unavailable.", "Amazon", 1]
       ]


shuffle( urls )



def dlog( log ):
  # log it yo

  if( LOG ):
     try:                                       # sanity
       log = str( log ).encode("utf-8")

     except:
       return

     now   =  datetime.now()
     dtme  =  now.strftime("%d/%m/%Y %H:%M:%S")
     log   =  str( "%s  -at-  %s" % (log, dtme) )

     if( LOGSCRN ):
       print( log )

  return



def chxmch(qdn, url):
  # All your telephony are belog to us

  log = str( "[+++++] WINNER FROM %s at url %s" % (qdn, url) )
  dlog( log )

  # no spaces in msg
  msg = str( "%s_%s_%s" % (CUSMSG, qdn, url) )

  cmd = str( '%s shell service call isms 7 i32 1 s16 "com.android.mms" s16 "5152164023" s16 "null" s16 "%s" s16 "null" s16 "null"' % (adb, msg) )
  popen( cmd )



def chkurl( url, rgx, qdn, mch ):
  # check the urls

  #uas  =  'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
  uas  =  "Lynx"
  hdr  =  { 'User-Agent': uas }


  req  =  Request( url, headers=hdr)
  rsp  =  urlopen( req )

  txt  =  str( rsp.read() )

  #print(txt)
  if(rgx in txt):                       # make money
     if( VERBOSE ):
       log = str("[+] We have regex %s from %s" % (rgx, qdn) )
       dlog( log )

     if( mch == 1       ):              # chicken dinner
        chxmch(qdn, url)
        return

     if( VERBOSE ):
        log = str("[!] Missed regex from %s" % qdn)
        dlog( log )

  else:
     if( VERBOSE ):
        log = str("[!] Missed regex from  %s" % qdn)
        dlog( log )

     if( mch == 1):
        return

     else:
        log = str( "[+] Have match on missed regex %s from %s" % (rgx, qdn) )
        dlog( log )
        chxmch(qdn, url)                # chicken dinner


def purls():
  # i < f(P)n

  if( DIALOUT ):

     if( adb ):
        pass

     else:
       log = str("[!] Android Debug Bridge not found in path, Required for Dial Out - BAILING.")
       dlog( log )

       return

  lurl   =  len( urls )

  for i in range( lurl ):       # i is for indece is for... nevermind
    url  =  urls[i][0]          # url to search
    rgx  =  urls[i][1]          # regular expression to match
    qdn  =  urls[i][2]          # fully qualified domain name to tag
    mch  =  urls[i][3]          # does regex win on match or miss

    if( LOG ):
       if( VERBOSE ):
         log = str( "[+] URL %s\tRegex %s\tFQDN %s" % (url, rgx, qdn) )
         dlog( log )

    # try:
    chkurl( url, rgx, qdn, mch )
    sleep(5)



if __name__ == "__main__":
   while( 1 ):
      purls()
      sleep(180)
