import mechanize 
import time
import random
import string


class Transaction(object):
    def __init__(self): 
    	pass

    def run(self): 
    	# create a Browser instance 
    	br = mechanize.Browser()
 
    	# don"t bother with robots.txt 
    	br.set_handle_robots(False) 
        print("Hello")
    	br.addheaders = [("User-agent", "Mozilla/5.0Compatible")]

    	# start the timer 
    	start_timer = time.time() 

    	# submit the request 
    	resp = br.open("http://bluemixmongo.mybluemix.net/remuser")
        #resp = br.open("http://localhost:3000/remuser")
    	resp.read() 
        

        # stop the timer 
        latency = time.time() - start_timer

        # store the custom timer 
        self.custom_timers["Load_Front_Page"] = latency

        # think-time 
        time.sleep(2)

        # select first (zero-based) form on page 
        br.select_form(nr=0) 
        
        
     
        # set form field 
        br.form["firstname"] = ""
        br.form["lastname"] = ""
        br.form["mobile"] = ""

        # start the timer 
        start_timer = time.time() 
    
        # submit the form 
        resp = br.submit() 
        resp.read() 
    
        # stop the timer 
        latency = time.time() - start_timer  

    
        # store the custom timer 
        self.custom_timers["Delete"] = latency
    
        # think-time 
        time.sleep(2)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers