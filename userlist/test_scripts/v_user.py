
import random
import time
import mechanize


class Transaction(object):
    def __init__(self):
        pass

    def run(self):
      br = mechanize.Browser()
      br.set_handle_robots(False)
      resp=br.open("http://bluemixmongo.mybluemix.net/userlist/")
      assert("Example Mongo Page" in resp.get_data())
      latency = time.time() - start_timer
      self.custom_timers["Google Homepage"] = latency
      r = random.uniform(1, 2)
      time.sleep(r)
      self.custom_timers['Example_Timer'] = r


if __name__ == '__main__':
    trans = Transaction()
    trans.run()
    print trans.custom_timers