import re
from robobrowser import RoboBrowser
from pprint import pprint
import data
import config
import time


#init robobrowser and open bsamp login page
scrapper = RoboBrowser()
scrapper.open('http://balkan-samp.com/forum/index.php?action=login')

#find the form on the login page
login_form = scrapper.get_form()
login_form['user'] = config.BSAMP_USERNAME
login_form['passwrd'] = config.BSAMP_PASSWORD
scrapper.submit_form(login_form)

## check to see if the login is successful
scrapper.open('http://balkan-samp.com/forum/index.php')
userinfo = str(scrapper.select('#userinfo'))

## set authenticated to false
authenticated = False

## Check if there is 'Gost' in userinfo div
## if there is we can say that the authentication failed
if userinfo.find('Gost') == -1:
    authenticated = True
else:
    authenticated = False

## Check if the authentication failed and print it
if authenticated == False:
    pprint('Authentication failed! Please insert correct credentials!')

#start the infinite loop so we can get the data
#every couple of seconds
if authenticated == True:
    ## set infinite to true so we get an infinite loop
    infinite = True
    while infinite == True:
        print('Authenticated')
        ##todo
        ##finish webscrapping with extracting messages and tag spans
        ##compare them to the ones in the storage
        ##if there are missmatches - notify
        ##re-store them for further matchings

    ## loop every 10 seconds
    time.sleep(10)