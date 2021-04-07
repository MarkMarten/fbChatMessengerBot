from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time
from fbchat import Client, log
from fbchat.models import *
options = webdriver.ChromeOptions()
#options.add_argument('headless')
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(options=options)


class MessengerBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)
        users = client.fetchAllUsers()
        threads = client.fetchThreadList()

        for thread in threads:
            recentMessages=client.fetchThreadMessages(thread.uid,1)
            msg=recentMessages[0].text.lower()
            print(msg)
            trigger1="msgtrigger"

            if(msg==trigger1):
                client.sendMessage("triggeranswer",thread.uid,ThreadType.USER)



client = MessengerBot("username","password")
client.listen()