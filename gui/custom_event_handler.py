import collections

import event_handler


class EventHandler(event_handler.EventHandler):
    def __init__(self, events: collections.deque):
        self.events = events

    def emit_event(self, event):
        print("event from handler: " + event)
        self.events.append(event)
