#!/usr/bin/python

import threading
import time

exitFlag = 0
actualThread = 0
nThreads = 10

phrase = "Wait A Minute, Doc. Are You Telling Me You Built A Time Machine... Out Of A DeLorean?"

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        self.capitalize(self.name)

    def testCapitalize(self):
        global phrase

        for i in phrase:
            if i.islower():
                return False
        return True
                    
    def capitalize(self, threadName):
        global actualThread
        global phrase
        global nThreads

        while True:

            if self.testCapitalize():
                break
            
            if actualThread == self.threadID:
                
                for i in range(len(phrase)):

                    if phrase[i].islower():

                        phrase = phrase[:i] + phrase[i].capitalize() + phrase[i+1:]
                        
                        time.sleep(1)
                        print(f"Thread {str(self.threadID)} changed a character:")
                        print(f"{phrase}\n")
                        actualThread = (actualThread+1) % nThreads
                        break


if __name__ == "__main__":
    
    threads = []
    for i in range(10):
        threads.append(myThread(i, "Thread-"+str(i), i))

    for i in range(10):
        threads[i].start()
    
    while True:
        if not threads[0].is_alive():
            time.sleep(1)
            print("----- FINALIZADO -----")
            print(phrase)
            break