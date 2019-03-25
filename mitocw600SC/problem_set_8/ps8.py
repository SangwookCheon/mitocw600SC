# 6.00 Problem Set 8
#
# Name: Sangwook Cheon
# Collaborators: None
# Time:

import numpy
import random
import pylab

# Code from ps7.py

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.
        maxBirthProb: Maximum reproduction probability (a float between 0-1)
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step.
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        if random.random() <= self.clearProb:
            return True
        else:
            return False

    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.

        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """

        if random.random() <= self.maxBirthProb * (1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            return NoChildException()


class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """

    def __init__(self, viruses, maxPop):
        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """

        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:

        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.
        - The current population density is calculated. This population density
          value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.

        returns: The total virus population at the end of the update (an
        integer)
        """
        curviruses = self.viruses[:]
        for virus in curviruses:
            if virus.doesClear():
                self.viruses.remove(virus)
            else:
                temp = self.viruses[:]
                repro = virus.reproduce(len(self.viruses) / float(self.maxPop))
                temp.append(repro)
                if len(temp) <= self.maxPop and type(repro) != NoChildException:
                    self.viruses.append(repro)

        return self.getTotalPop()


def simulationWithoutDrug():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.
    """
    numtrials = 5
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    averagelist = [0] * 300
    timesteplist = []
    for i in range(numtrials):
        viruses = []
        timesteplist = []
        for i in range(100):
            viruses.append(SimpleVirus(maxBirthProb, clearProb))
        patient = SimplePatient(viruses, maxPop)

        for i in range(300):
            a = patient.update()
            averagelist[i] += a / float(numtrials)
            timesteplist.append(i+1)

    print averagelist
    print len(averagelist)
    print len(timesteplist)

    pylab.figure(1)
    pylab.title("Population of virus in patient's body over time steps, \n without drug treatment (clearProb: 0.05, MaxBirthProp: 0.1)")
    pylab.xlabel('# Time steps')
    pylab.ylabel('# of viruses')
    pylab.plot(timesteplist, averagelist, label = 'Average number of viruses after ' + str(numtrials) + ' trials')
    pylab.legend(loc = 'best')
    pylab.show()

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """

        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb



    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """

        # if drug in self.resistances:
        #     return True
        # else:
        #     return False
        print self.resistances
        return self.resistances[drug]


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity). IMPORTANT
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        modresistances = {}

        for val in self.resistances.itervalues():
            if not val:
                return NoChildException()

        if random.random() <= self.maxBirthProb * (1 - popDensity):
            # for i in self.resistences.keys():
            #     if random.random() <= 1 - self.mutProb:
            #         modresistances[i] = self.resistances[i]
            #     else:
            #         modresistances[i] = not self.resistances[i]
            for i in activeDrugs:
                if random.random() <= 1 - self.mutProb:
                    modresistances[i] = not self.resistances[i]

            return ResistantVirus(self.maxBirthProb, self.clearProb, modresistances, self.mutProb)

        else:
            return NoChildException()

            

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop
        self.druglist = []
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """

        if newDrug not in self.druglist:
            self.druglist.append(newDrug)

        # should not allow one drug being added to the list multiple times


    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """

        return self.druglist

    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistpop = 0

        for virus in self.viruses:
            for drug in drugResist:
                if virus.isResistantTo(drug):
                    continue
                else:
                    resistpop -= 1
            resistpop += 1


        return resistpop

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        curviruses = self.viruses[:]

        for virus in curviruses:
            if virus.doesClear():
                self.viruses.remove(virus)
            else:
                temp = self.viruses[:]
                repro = virus.reproduce(len(self.viruses) / float(self.maxPop), self.druglist)
                temp.append(repro)
                if len(temp) <= self.maxPop and type(repro) != NoChildException:
                    self.viruses.append(repro)

        return self.getTotalPop()
#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    viruses = []
    curpop = []
    timesteps = []
    curresistpop = []

    for i in range(100):
        viruses.append(ResistantVirus(maxBirthProb= 0.1, clearProb= 0.05, resistances= {'guttagonol' : True}, mutProb= 0.005))

    print viruses

    patient = Patient(viruses, maxPop= 1000)
    print patient.getResistPop(['guttagonol'])

    for i in range(150):
        patient.update()
        curpop.append(patient.getTotalPop())
        curresistpop.append(patient.getResistPop(['guttagonol']))
        timesteps.append(i)

    patient.addPrescription('guttagonol')

    for i in range(150, 300):
        patient.update()
        curpop.append(patient.getTotalPop())
        curresistpop.append(patient.getResistPop(['guttagonol']))
        timesteps.append(i)

    pylab.figure(1)
    pylab.title('Average total population of viruses')
    pylab.ylabel('Population of viruses')
    pylab.xlabel('# Time steps')
    pylab.plot(timesteps, curpop)

    pylab.figure(2)
    pylab.title('Average population of guttagonol-resistant virus particles')
    pylab.ylabel('Population of guttagonol-resistant viruses')
    pylab.xlabel('# Time steps')
    pylab.plot(timesteps, curresistpop)

    pylab.show()


# Testing:
simulationWithDrug()
#
# PROBLEM 3
#        

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """

    # TODO

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """

    # TODO



#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    #TODO



