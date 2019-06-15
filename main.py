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
        scrapper.open('http://balkan-samp.com/forum/index.php'

        ## select message span and extract the 
        ## message count from the span
        message_span = str(scrapper.select('#button_pm'))
        message_res = re.search("\[<strong>(.*?)\</strong>]", message_span)

        ## chack if the regex matched with [*] if it is
        ## we check current message count with the provided one
        ## and if there are no messages set message count to 0
        if message_res:
            result = int(message_res.group(1))
            data.compare_messages(result)
        else:
            if data.get_message_count() != 0:
                data.set_message_count(0)


        ## select profile span and extract the
        ## mention tag
        profile_span = str(scrapper.select("#button_profile"))
        profile_res = re.search("\[<strong>(.*?)\</strong>]", profile_span)
        

        ## chack if the regex matched with [*] if it is
        ## we check current mentions count with the provided one
        ## and if there are no mentions set mention count to 0
        if profile_res:
            result = int(profile_res.group(1))
            data.compare_mentions(result)
        else:
            if data.get_mention_count() != 0:
                data.set_mention_count(0)



    ## loop every 10 seconds
    time.sleep(10)