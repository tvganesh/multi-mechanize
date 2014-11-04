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
    	resp = br.open("http://bluemixmongo.mybluemix.net/newuser")
        #resp = br.open("http://localhost:3000/newuser")
    	resp.read() 
        

        # stop the timer 
        latency = time.time() - start_timer

        # store the custom timer 
        self.custom_timers["Load_Front_Page"] = latency

        # think-time 
        time.sleep(2)

        # select first (zero-based) form on page 
        br.select_form(nr=0) 
        
        # Create random Firstname
        a = (''.join(random.choice(string.ascii_uppercase) for i in range(5)))
        b = (''.join(random.choice(string.digits) for i in range(5)))
        firstname = a + b

        # Create random Lastname  
        a = (''.join(random.choice(string.ascii_uppercase) for i in range(5)))
        b = (''.join(random.choice(string.digits) for i in range(5)))
        lastname = a + b

        # Create a random mobile number
        mobile = (''.join(random.choice(string.digits) for i in range(9)))

        
     
        # set form field 
        br.form["firstname"] = firstname
        br.form["lastname"] = lastname
        br.form["mobile"] = mobile

        # start the timer 
        start_timer = time.time() 
    
        # submit the form 
        resp = br.submit() 
        resp.read() 
    
        # stop the timer 
        latency = time.time() - start_timer  

    
        # store the custom timer 
        self.custom_timers["Search"] = latency
    
        # think-time 
        time.sleep(2)

if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers
