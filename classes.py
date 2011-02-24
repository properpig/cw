# Filename: classes.py
# Author: Heng U San
# Centre No / Index No: 3024 /
# Description: Supporting classes for resource, music cd and film dvd

''' Super class Resource '''
class Resource():

    ''' Resource class constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType):
        self.__ResourceNo = ResourceNo
        self.__Title = Title
        self.__DateAcquired = DateAcquired
        self.__ResourceType = ResourceType

    ''' Resource number accessor '''
    def getResourceNo(self):
        return self.__ResourceNo

    ''' Title accessor '''
    def getTitle(self):
        return self.__Title

    ''' DateAcquired accessor '''
    def getDateAcquired(self):
        return self.__DateAcquired

    ''' ResourceType accessor '''
    def getResourceType(self):
        return self.__ResourceType

    ''' Title modifier '''
    def setTitle(self, newTitle): # because we are setting a new number we need to parse in that number
        self.__Title = newTitle

    ''' DateAcquired modifier '''
    def setDateAcquired(self, newDateAcquired):
        self.__DateAcquired = newDateAcquired

    ''' ResourceType modifier '''
    def setResourceType(self, newResourceType):
        self.__ResourceType = newResourceType

    ''' Helper function to display all data '''
    def display(self):
        return("{0:5s}{1:30s}{2:6s}{3:1s}".format(self.__ResourceNo, self.__Title, self.__DateAcquired, self.__ResourceType))

# Subclass Music CD
class MusicCD(Resource):

    ''' MusicCD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Artist, NoOfTracks): # parse in what is common + the things you wanna add
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Artist = Artist
        self.__NoOfTracks = NoOfTracks

    ''' Artist accessor '''
    def getArtist(self):
        return self.__Artist

    ''' NoOfTracks accessor '''
    def getNoOfTracks(self):
        return self.__NoOfTracks

    ''' Artist modifier '''
    def setArtist(self, newArtist):
        self.__Artist = newArtist

    ''' NoOfTracks modifier '''
    def setNoOfTracks(self, newNoOfTracks):
        self.__NoOfTracks = newNoOfTracks

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2}{3:50s}{4}".format(super().display(), self.__Artist, self.__NoOfTracks.zfill(2), "NULL", "000"))
        
# Subclass FilmDVD
class FilmDVD(Resource):

    ''' FilmDVD constructor '''
    def __init__(self, ResourceNo, Title, DateAcquired, ResourceType, Director, RunningTime):
        super().__init__(ResourceNo, Title, DateAcquired, ResourceType)
        self.__Director = Director
        self.__RunningTime = RunningTime

    ''' Director accessor '''
    def getDirector(self):
        return self.__Director

    ''' RunningTime accessor '''
    def getRunningTime(self):
        return self.__RunningTime

    ''' Director modifier '''
    def setDirector(self, newDirector):
        self.__Director = newDirector

    ''' RunningTime modifier '''
    def setRunningTime(self, newRunningTime):
        self.__RunningTime = newRunningTime

    ''' Helper function to display all data '''
    def display(self):
        return("{0:42s}{1:50s}{2}{3:50s}{4}".format(super().display(), "NULL", "00", self.__Director, self.__RunningTime.zfill(3)))


##r1 = Resource("00001", "Best of Super Junior", "090911", "C")
##r2 = Resource("00002", "Shaolin Temple", "121210", "D")
##
###print(r1.getResourceNo())
###print(r1.display())
###print(r1.setTitle("Hello SJ"))
###print(r1.display())
##
##r3 = Resource("00003", "", "", "")
##
###print(r3.display())
##r3.setTitle("Good morning Shinee")
##r3.setDateAcquired("C")
###print(r3.display())
##
##cd1 = MusicCD("00004", "Michael Jackson Last Album", "050508", "C", "Michael Jackson", 12)
##
###print(cd1.getResourceNo()) #inheritance
###print(cd1.display()) # overriding
##
### print(cd1.__Title) #illegal due to information hiding
##
##
##dvd1 = FilmDVD("00005", "Green Hornet", "030311", "D", "Jay Chou", 120)
##
##res_list = []
##res_list.append(cd1)
##res_list.append(dvd1)
##
##for item in res_list:
##    print(item.display()) #polymorphism

#in order to demonstrate polymorphism you need to first have inheritance. these objects
# have the same parent class. Even though the same method, display(), is called,
# it displays 2 different ways depending on the subclass.
