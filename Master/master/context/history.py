import time
from random import randint

class History():
    max_history_count = int((3600 * 24 * 7) / 30) # total seconds in a week period at 30 second sample rate
    def __init__(self):
        self.client_history = list()
        self.instance_history = list()
        self.server_history = list()
        #self.add_dummy_data()

    def add_client_history(self, client_num):
        if len(self.client_history) >= History.max_history_count:
            self.client_history = self.client_history[1:]
        self.client_history.append({
            'count' : client_num,
            'time' : int(time.time())
        })

    def add_server_history(self, server_num):
        if len(self.server_history) >= History.max_history_count:
            self.server_history = self.server_history[1:]
        self.server_history.append({
             'count' : server_num,
             'time' : int(time.time())
        })
  
    def add_instance_history(self, instance_num):
        if len(self.instance_history) >= History.max_history_count:
            self.instance_history = self.instance_history[1:]
        self.instance_history.append({
            'count' : instance_num,
            'time' : int(time.time())
        })

    def add_dummy_data(self):
        max_dummy_history = int(History.max_history_count / 2)
        for i in range (0, max_dummy_history):
            self.client_history.append({
            'count' : i + 10,
            'time' : int(time.time() - (30 * (max_dummy_history - i)))
            })

            self.server_history.append({
            'count' : i + 100,
            'time' : int(time.time() - (30 * (max_dummy_history - i)))
            })

            self.instance_history.append({
            'count' : i,
            'time' : int(time.time() - (30 * (max_dummy_history - i)))
            })
