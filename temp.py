import random
from sklearn.preprocessing import LabelEncoder
import math

class ProfSubMetaData:

    PSMAP = {}
    def addMetaData(self, nameID, subIDs, prefSlots):

        metaData = {"subIDs" : subIDs, "prefSlots" : prefSlots}
        self.PSMAP[nameID] = metaData

class EncodePhenotypes:
    sems = {}
    classrooms = {}
    profs = {}
    subs = {}
    days = {}
    slots = {}

    def __init__(self, sems, classrooms, profs, subs, days, slots):
        self.sems = self.encode(list(sems))
        self.classrooms = self.encode(list(classrooms))
        self.profs = self.encode(list(profs))
        self.subs = self.encode(list(subs))
        self.days = self.encode(list(days))
        self.slots = self.encode(list(slots))

    
    def encode(self, data):
        
        le = LabelEncoder()
        le.fit(data)
        temp = le.transform(data)
        EncodedData = {}
        for i in range(0, len(data)):
            bits = math.ceil(math.log(len(temp), 2))
            EncodedData[data[i]] = '0' * (bits-len(bin(i)[2:])) + bin(i)[2:]
        return EncodedData


faculty = {'VIR','LOH','AMO','GUI','NAY','CHT','KUT','AMI','SON','FER','DEV','BOR','PUR','GEE','PAL','MAN','ANK','SHR','JOH','JIL','SAM','MEH'}

S3Subs = {'MAT3', 'CAS', 'EDC', 'DSD', 'EMWT', 'EDCLAB', 'DSDLAB', 'TC', 'MATBC'}
S4Subs = {'SAS', 'MPI', 'LIC', 'TLA', 'SCT', 'MPILAB', 'LICLAB', 'EEM'}
S5Subs = {'ADC', 'DSP', 'PE1', 'PE2', 'CELAB', 'EMLAB', 'OE1', 'EE'}
S6Subs = {'CSE', 'VLSI', 'PE3', 'PE4', 'VLSILAB', 'ESDLAB', 'OE2', 'CLI'}
S7Subs = {'DC', 'PE5', 'DCLAB', 'OE3'}
S8Subs = {'ACE', 'PE6'}
AllSubs = S3Subs | S4Subs | S5Subs | S6Subs |S7Subs | S8Subs

classrooms = {'S1', 'S2', 'S3', 'S4', 'B1', 'B2', 'B3'}
semesters = {'S3', 'S4', 'S5', 'S6', 'S7', 'S8'}
days = {'mon', 'tue', 'wed', 'thu', 'fri'}
slots = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}


def makeRandomMetaData(MetaDataObj, minSubs=1, maxSubs=3, maxOverlap=0):
    subsLeft = AllSubs
    for f in faculty:
        r = random.choice(tuple(subsLeft))
        MetaDataObj.addMetaData(f, [r], prefSlots=random.randint(0, 6))
        subsLeft.remove(r)
    profsLeft = faculty
    for s in subsLeft:
        f = random.choice(tuple(profsLeft))
        MetaDataObj.PSMAP[f]['subIDs'].append(s)
        profsLeft.remove(f)

# assingn subjects to teachers randomly for test purpose
metadata = ProfSubMetaData()
makeRandomMetaData(metadata)

#this objects stores binary encoded dicionaries
x = EncodePhenotypes(sems=semesters, classrooms= classrooms, profs=faculty, subs=AllSubs, days=days, slots=slots)

print(x.subs)

class GenetiAlgo:
    '''
    ---This class is responsible for all the Genetic Operations and Manipulations---

    intialPopSize -> sets the inital population pool size
    numClasses -> the number different classes you want to make a tt for
    numSlots -> the total number of slots for a class per week
    numSlotBits -> the number of bits required to represent information about one slot
    '''

    initialPop = []
    initialPopSize = 100
    subs = {}
    classrooms = {}
    numClasses = 3
    numSlots = 20
    numSlotBits = None
    def __init__(self, subs, classrooms, initialPopSize=100, numClasses = 3, numSlots = 20):
        self.initialPopSize = initialPopSize
        self.subs = subs
        self.classrooms = classrooms
        self.initialPop = []
        self.numClasses = numClasses
        self.numSlots = numSlots
        self.numSlotBits = len(list(self.subs.values()[0]))+ len(list(self.classrooms.values()[0]))
    def generateIntialPop(self ):
        '''
        Randomly Populates intialPop with binary values from subjects and classrooms
        '''
        for i in range(0, self.initialPopSize):
            individual = ''
            # an individual solution will contain numClasses * numSlots amount of slots in total... i.e the consolidated time table
            for j in range(0, (self.numClasses * self.numSlots)):
                s = random.choice(list(self.subs.values()))
                c = random.choice(list(self.classrooms.values()))
                individual = individual + s + c
            self.initialPop.append(individual)
            

    def fitness(self, individual):
        '''
        This function calculates the feasibility or the goodness of an individual solutionS 
        ---Yet to be programmed---
        '''
        return 0

sol = GenetiAlgo(subs=x.subs, classrooms=x.classrooms)
sol.generateIntialPop()
#print(len(sol.initialPop[1]))
