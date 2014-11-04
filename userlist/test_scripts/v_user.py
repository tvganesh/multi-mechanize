###########################################################################################################################
# This multi mechanize script is used to display documents to MongoDB. The Firstname, Lastname and Mobile are generated randomly.
# Based on the random string generated, 5 documents are displayed.
# Test : userlist
# Developed by: Tinniam V Ganesh                        Date: 04 Nov 2014
############################################################################################################################
import random
import time
import mechanize


class Transaction(object):
    def __init__(self):
        pass

    def run(self):
      # create a Browser instance 
      br = mechanize.Browser()

      # don"t bother with robots.txt
      br.set_handle_robots(False)

      # start the timer 
      start_timer = time.time() 

      #print("Display userlist")
      # Display 5 random documents
      resp=br.open("http://bluemixmongo.mybluemix.net/userlist/")
      assert("Example Mongo Page" in resp.get_data())

      # stop the timer 
      latency = time.time() - start_timer
      self.custom_timers["Userlist"] = latency
      r = random.uniform(1, 2)
      time.sleep(r)
      self.custom_timers['Example_Timer'] = r


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers