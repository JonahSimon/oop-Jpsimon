class Publisher(object):
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self,subscriber):
        self.subscribers.append(subscriber)

    def update_subscribers(self, *args, **kwargs):
        for subscriber in self.subscribers:
            subscriber.update(self, *args, **kwargs)

class Subscriber(object):
    notification = "default"
    recived = False
    def __init__(self,publisher):
        publisher.add_subscriber(self)

    def update(self, publisher, *args, **kwargs):
        self.notification = args
        self.recived = True
        print('got', args, kwargs, 'from', publisher)