import qrcode

class Event(object):
    def __init__(self, name, points,):
        self.eventName = name
        self.__eventPoints = points

    def get_name(self):
        return self.eventName

    def get_points(self):
        return self.__eventPoints

    def set_points(self, new_points):
        self.__eventPoints = new_points

    def __str__(self):
        return self.eventName + " " + self.__eventPoints

class EventList(object):
    def __init__(self):
        self.__events = []

    def add_new_event(self, name, points):
        self.__events.append(Event(name , points))

    def get_event(self, name):
        for event in self.__events:
            if event.get_name() == name:
                return event.get_points()


eventList = EventList()
eventList.add_new_event("cs club", 100)

qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)

data = eventList.get_event("cs club")

qr.add_data(data)
qr.make(fit=True)


# Create an image from the QR Code instance
#img = qr.make_image()
#img.save("image.png")

img = qr.make_image(fill_color="black", back_color="white")
img.save("event.png")