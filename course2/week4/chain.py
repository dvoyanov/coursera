class EventGet:
    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, kind):
        self.kind = kind.__class__
        self.value = kind


class NullHandler:
    def __init__(self, successor=None):
        self.successor = successor

    def handle(self, obj, event):
        if self.successor is not None:
            return self.successor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == int:
            if isinstance(event, EventGet):
                return obj.integer_field
            elif isinstance(event, EventSet):
                obj.integer_field = event.value
            else:
                raise TypeError
        else:
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == float:
            if isinstance(event, EventGet):
                return obj.float_field
            elif isinstance(event, EventSet):
                obj.float_field = event.value
            else:
                raise TypeError
        else:
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == str:
            if isinstance(event, EventGet):
                return obj.string_field
            elif isinstance(event, EventSet):
                obj.string_field = event.value
            else:
                raise TypeError
        else:
            return super().handle(obj, event)


class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""
