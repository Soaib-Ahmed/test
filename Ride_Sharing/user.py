from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self,companey_name) -> None:
        self.companey_name=companey_name
        self.riders=[]
        self.drivers=[]
        self.rides=[]

    def add_rider(self,rider):
        self.riders.append(rider)

    def add_driver(self,driver):
        self.drivers.append(driver)

    def __repr__(self) -> str:
        return f'{self.companey_name} with riders: {len(self.riders)} and drivers {len(self.drivers)}'

class User(ABC):
    def __init__(self,name,email,nid,) -> None:
        self.name=name
        self.email=email
        self.__id=0
        self.__nid=nid
        self.wallet=0
        
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError
    
class Rider(User):
    def __init__(self, name, email, nid, curr_location,intital_amount) -> None:
        self.curr_ride=None
        self.wallet=intital_amount
        self.curr_location=curr_location
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Rider: with name: {self.name} and email: {self.email}")

    def load_cash(self,amonut):
        if amonut>0:
            self.wallet+=amonut

    def update_location(self,curr_location):
        self.curr_location=curr_location

    def req_ride(self,ride_sharing,destination):
        if not self.curr_ride:
            ride_req=Ride_req(self,destination)
            ride_matcher=Ride_matching(ride_sharing.drivers)
            ride=ride_matcher.find_driver(ride_req)
            self.curr_ride=ride

    def show_curr_ride(self):
        print(self.curr_ride)



class Driver(User):
    def __init__(self, name, email, nid,curr_loacation) -> None:
        self.curr_loacation=curr_loacation
        super().__init__(name, email, nid)
        self.wallet=0

    def display_profile(self):
        print(f'Driver with name: {self.name} and email: {self.email}')
    
    def accept_ride(self,ride):
        ride.self_driver(self)


class Ride: 
    def __init__(self,start_location,end_loaction)-> None:
        self.start_location=start_location
        self.end_loaction=end_loaction
        self.driver=None
        self.rider=None
        self.start_time=None
        self.end_time=None
        self.estimated_fare=None

    def self_driver(self,driver):
        self.driver=driver

    def start_ride(self):
        self.start_time=datetime.now()

    def end_ride(self,rider,amount):
        self.end_time=datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare

    def __repr__(self) -> str:
        return f'Ride deatils. Starteed {self.start_location} and end {self.end_loaction}'


class Ride_req:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location


class Ride_matching:
    def __init__(self,drivers) -> None:
        self.available_drivers=drivers

    def find_driver(self,ride_req):
        if len(self.available_drivers)>0:
            #find the colsest dirver of the rider
            driver = self.available_drivers[0]
            ride = Ride(ride_req.rider.curr_location ,ride_req.end_location)
            driver.accept_ride(ride)
            return ride

class vehicale(ABC):
    speed={
        'car': 50,
        'bike': 60,
        'cng': 30
    }

    def __init__(self,vehicale_type,license_plate,rate) -> None:
        self.vehicale_type=vehicale_type
        self.license_plate=license_plate
        self.rate=rate
        self.status='available'
        super().__init__()

    @abstractmethod
    def start_drive(self):
        pass

class Car(vehicale):
    def __init__(self, vehicale_type, license_plate, rate) -> None:
        super().__init__(vehicale_type, license_plate, rate)

    def start_drive(self):
        self.status='Unavilable'

class Bike(vehicale):
    def __init__(self, vehicale_type, license_plate, rate) -> None:
        super().__init__(vehicale_type, license_plate, rate)

    def start_drive(self):
        self.status='Unavilable'


tole_Naw = Ride_Sharing('Tole Naw')
abir=Rider("Abir",'abir@gmail.com',1525,'Adalot',500)
tole_Naw.add_rider(abir)
mridul=Driver('Mridul','mridul@gmail.com',333,'Womens clg')
tole_Naw.add_driver(mridul)

print(tole_Naw)
abir.req_ride(tole_Naw,'Dulipara')
abir.show_curr_ride()