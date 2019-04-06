import abc


class EventHandler(abc.ABC):
    @abc.abstractmethod
    def emit_event(self, event):
        pass
