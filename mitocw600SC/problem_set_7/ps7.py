# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics
# Name: Sangwook Cheon
# Collaborators: None
# Time:

import numpy
import random
import pylab

''' 
Begin helper code
'''


class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """
'''
End helper code
'''


#
# PROBLEM 1
#
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

# exception = SimpleVirus(0.8, 0.5)
# exception.reproduce(0.9)


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
                # print 'CLEARED!!!!!!!!!!!!!!!!!!!!!!!!!!!' + str(self.viruses)
            else:
                temp = self.viruses[:]
                repro = virus.reproduce(len(self.viruses) / float(self.maxPop))
                temp.append(repro)
                if len(temp) <= self.maxPop and type(repro) != NoChildException:
                    self.viruses.append(repro)

        return self.getTotalPop()

# patient = SimplePatient([SimpleVirus(0.8, 0.8), SimpleVirus(0.8,0.8)], 5)
# patient.update()


#
# PROBLEM 2
#
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
        # print len(viruses)
        patient = SimplePatient(viruses, maxPop)
        # print patient.getTotalPop()

        for i in range(300):
            a = patient.update()
            # print 'CHANGED: ' + str(patient.getTotalPop())
            averagelist[i] += a / float(numtrials)
            timesteplist.append(i+1)

    print averagelist
    print len(averagelist)
    print len(timesteplist)

            # print poplist

    pylab.figure(1)
    pylab.title("Population of virus in patient's body over time steps, \n without drug treatment (clearProb: 0.05, MaxBirthProp: 0.1)")
    pylab.xlabel('# Time steps')
    pylab.ylabel('# of viruses')
    pylab.plot(timesteplist, averagelist, label = 'Average number of viruses after ' + str(numtrials) + ' trials')
    pylab.legend(loc = 'best')
    pylab.show()

# Testing
simulationWithoutDrug()

