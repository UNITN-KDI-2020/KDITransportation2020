'''
This file contains the models of the previous deliverable that will be exploited to export
data in a way that will be easier to integrate.

@carbogninalberto
'''
import json

class Location:
    def __init__(self, latitude, longitude, altitude):
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude

    def __str__(self):
        return "latitude: {}, longitude: {}, altitude: {}".format(self.latitude, self.longitude, self.altitude)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Address:
    def __init__(self, province, city, street, number, cap, location):
        self.province = province
        self.city = city
        self.street = street
        self.number = number
        self.cap = cap
        self.location = location

    def __str__(self):
        return "province: {}, city: {}, street: {}, number: {}, cap: {}, location: [{}]".format(
            self.province,
            self.city,
            self.street,
            self.number,
            self.cap,
            self.location
        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Contact:
    def __init__(self, phone, email, website):
        self.phone = phone
        self.email = email
        self.website = website
    
    def __str__(self):
        return "phone: {}, email: {}, website: {}".format(
            self.phone,
            self.email,
            self.website
        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Price:
    def __init__(self, cost, currency_type = "€"):
        self.cost = cost
        self.currency_type = currency_type

    def __str__(self):
        return "cost: {}, currency_type: {}".format(
            self.cost,
            self.currency_type
        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class CalendarDates:
    def __init__(self, service_id, date, exception_type):
        self.service_id = service_id
        self.date = date
        self.exception_type = exception_type
    
    def __str__(self):
        return "service_id: {}, date: {}, exception_type: {}".format(
            self.service_id,
            self.date,
            self.exception_type
        )
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)


class Calendar:
    def __init__(self, service_id, monday, tuesday, wednesday, thursday, friday, saturday, sunday, start_date, end_date, exceptions):
        self.service_id = service_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday
        self.sunday = sunday
        self.start_date = start_date
        self.end_date = end_date
        self.exceptions = exceptions

    def __str__(self):
        return "service_id: {}, monday: {}, tuesday,: {} wednesday: {}, thursday: {}, friday: {}, saturday: {}, sunday: {}, start_date: {}, end_date: {}, exceptions: [{}]".format(
            self.service_id,
            self.monday,
            self.tuesday,
            self.wednesday,
            self.thursday,
            self.friday,
            self.saturday,
            self.sunday,
            self.start_date,
            self.end_date,
            self.exceptions
        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

class Facility:
    def __init__(self, type, price, contact, ranking, address, calendar):
        self.type = type
        self.price = price
        self.contact = contact
        self.ranking = ranking
        self.address = address
        self.calendar = calendar

    def __str__(self):
        return "type: {}, price: [{}], contact: [{}], ranking: {}, address: [{}], calendar: [{}]".format(
            self.type,
            self.price,
            self.contact,
            self.ranking,
            self.address,
            self.calendar
        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
    
class Route:
    def __init__(self, type, RouteID, SpeedLimit, StartingPoint, ArrivalPoint, ModeOfTransport, TimeSpent, Facility, Length):
        self.type = type
        self.RouteID = RouteID
        self.SpeedLimit = SpeedLimit
        self.StartingPoint = StartingPoint
        self.ArrivalPoint = ArrivalPoint
        self.ModeOfTransport = ModeOfTransport
        self.TimeSpent = TimeSpent
        self.Facility = Facility
        self.Length = Length


    def __str__(self):
        return "type: {}, RouteID: {}, SpeedLimit: {}, StartingPoint: [{}], ArrivalPoint: [{}], ModeOfTransport: [{}], TimeSpent: [{}], Facility: [{}], Length: {}".format(
            self.type,
            self.RouteID,
            self.SpeedLimit,
            self.StartingPoint,
            self.ArrivalPoint,
            self.ModeOfTransport,
            self.TimeSpent,
            self.Facility,
            self.Length

        )

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
