# Problem Set 6: Simulating robots
# Name: Sangwook Cheon
# Collaborators: None
# Time: 4 hours

import math
import random

import ps6_visualize
import pylab

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, pos):
        """
        Initializes a position with coordinates (x, y).
        """
        self.position = pos
        self.x = pos[0]
        self.y = pos[1]

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getposition(self):
        return [self.x, self.y]

    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position((new_x, new_y))

# === Problems 1

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.tiles = {}
        self.numcleantiles = 0
        for i in range(self.width):
            for n in range(self.height):
                self.tiles[(i,n)] = ''
        # print self.tiles

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.pos = Position(pos)
        if self.isPositionInRoom(self.pos):
            self.tiles[int(self.pos.getX()), int(self.pos.getY())] = 'Cleaned'
        # print '-------'
        # print 'current tiles: ' + str(self.tiles)
        # print '-------'
        return self.tiles

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if self.tiles[(m, n)] == 'Cleaned':
            return True
        else:
            return False
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        self.numcleantiles = 0
        for key in self.tiles.keys():
            if self.tiles[key] == 'Cleaned':
                self.numcleantiles += 1
        return self.numcleantiles

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        return [random.randrange(0, self.width, 1, float), random.randrange(0, self.height, 1, float)]

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height:
            return True
        else:
            # print str(pos.getposition()) + ' : out of the room!'
            return False

    def gettiles(self):
        return self.tiles

    def initializekey(self, val):
        for key in self.tiles.keys():
            self.tiles[key] = val
        return self.tiles

# a = RectangularRoom(5,5)
# a.cleanTileAtPosition((0,1))
# a.cleanTileAtPosition((3,2))
# a.cleanTileAtPosition((6,7))
# print 'cleaned: ' + str(a.getNumCleanedTiles())
# print
# print 'Real Simulation --------------------------------'

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """

        self.speed = speed
        self.room = room
        self.position = Position(self.room.getRandomPosition())
        self.direction = random.randrange(0, 360)
        self.nummoves = 0


    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = Position((position.getposition()[0], position.getposition()[1]))
        return self.position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction
        return self.direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.setRobotPosition(self.position)
        self.room.cleanTileAtPosition(self.position)

    def getroom(self):
        return self.room

    def getnummoves(self):
        return self.nummoves

    def setnummoves(self, val):
        self.nummoves = val
        return self.nummoves

# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current direction; when
    it hits a wall, it chooses a new direction randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # if self.direction <= 90:
        #     self.xmove = self.speed * math.sin(abs(self.direction - 90))
        #     self.ymove = self.xmove * math.tan(abs(self.direction - 90))
        # elif 90 < self.direction <= 180:
        #     self.xmove = self.speed * math.sin(abs(self.direction - 180))
        #     self.ymove = - (self.xmove * math.tan(abs(self.direction - 180)))
        # elif 180 < self.direction <= 270:
        #     self.xmove = - (self.speed * math.sin(abs(self.direction - 270)))
        #     self.ymove = self.xmove * math.tan(abs(self.direction - 270))
        # elif 270 < self.direction <= 360:
        #     self.xmove = - (self.speed * math.sin(abs(self.direction - 360)))
        #     self.ymove = - (self.xmove * math.sin(abs(self.direction - 360)))
        #
        # self.position = self.setRobotPosition((self.xmove, self.ymove))

        # self.position = Position((self.position.getposition()))
        self.temppos = self.position.getposition()

        if self.room.isPositionInRoom(Position(self.temppos).getNewPosition(self.direction, self.speed)):
            self.temppos = self.position.getposition()
            self.position = self.position.getNewPosition(self.direction, self.speed)
            self.room.cleanTileAtPosition(self.position.getposition())
            # print 'current position of the robot: ' + str(self.position.getposition())
            self.nummoves = self.nummoves + 1
        else:
            while not self.room.isPositionInRoom(Position(self.temppos).getNewPosition(self.direction, self.speed)):
                # print 'direction: ' + str(self.direction)
                self.temppos = self.position.getposition()
                self.direction = random.randrange(0,360)
            self.position = self.position.getNewPosition(self.direction, self.speed)
            self.room.cleanTileAtPosition(self.position.getposition())
            # print 'current position of the robot: ' + str(self.position.getposition())
            self.nummoves += 1


# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    """
    room = RectangularRoom(width, height)
    robotlist = []
    for i in range(num_robots):
        robotlist.append(robot_type(room, speed))
        # print robotlist
    mean = 0
    for i in range(num_trials):
        print '------------------------------------------------------------------'
        print 'Moving On'
        print '------------------------------------------------------------------'
        anim = ps6_visualize.RobotVisualization(num_robots, width, height)
        room.initializekey('')
        while float(room.getNumCleanedTiles())/room.getNumTiles() < min_coverage:
            for robot in robotlist:
                robot.updatePositionAndClean()
                print 'room tiles: ' + str(robot.room.getNumTiles())
                print 'current ratio: ' + str(float(robot.room.getNumCleanedTiles())/robot.room.getNumTiles())
                print 'cleanedtiles: ' + str(robot.room.getNumCleanedTiles())
                print 'nummoves: ' + str(robot.getnummoves())
                print 'direction: ' + str(robot.direction)
                anim.update(room, robotlist)
        for robot in robotlist:
            mean += float(robot.getnummoves()) / num_robots / num_trials
            robot.setnummoves(0)
            print 'mean: ' + str(mean)
            print '------------------------------------------------------------------'
            print 'Next Robot'
            print '------------------------------------------------------------------'
        anim.done()
    print 'Robot(s) took on average ' + str(mean) + \
          ' clock ticks to clean ' + str(min_coverage) + ' of the ' + str(width) +'x' + str(height) + ' room.'
    return int(mean)

# Testing
runSimulation(num_robots= 2, speed= 1.0, width= 5, height= 5, min_coverage= 0.8, num_trials= 1, robot_type= StandardRobot)

# === Problem 4
#
# 1) How long does it take to clean 80% of a 20x20 room with each of 1-10 robots?
#
# 2) How long does it take two robots to clean 80% of rooms with dimensions
# 	 20x20, 25x16, 40x10, 50x8, 80x5, and 100x4?

def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    numsteps = []
    robotindex = []
    for i in range(1,11):
        robotindex.append(i)
        numsteps.append(runSimulation(i, 1, 20, 20, 0.80, 5, StandardRobot))
    pylab.figure(1)
    pylab.title('Mean steps needed for each of 1-10 robots to clean 80% of 20x20 room')
    pylab.xlabel('Number of robots')
    pylab.ylabel(('Mean steps'))
    pylab.ylim(0,1000)
    pylab.plot(robotindex, numsteps)
    pylab.show()

showPlot1()

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    roomlist = [(20,20), (25,16), (40,10), (50,8), (80,5), (100,4)]
    roomratio = []
    numsteps = []
    for i in roomlist:
        roomratio.append(float(i[0])/i[1])
    for i in roomlist:
        numsteps.append(runSimulation(2, 1, i[0], i[1], 0.80, 5, StandardRobot))

    pylab.figure(2)
    pylab.title('Means steps needed for 2 robots to clean 80% of different rooms of size 200')
    pylab.xlabel('Width : Height')
    pylab.ylabel('Mean steps')
    pylab.ylim(0,600)
    pylab.plot(roomratio, numsteps)
    pylab.show()

showPlot2()
# === Problem 5

class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random after each time-step.
    """
    def updatePositionAndClean(self):
        self.temppos = self.position.getposition()

        if self.room.isPositionInRoom(Position(self.temppos).getNewPosition(self.direction, self.speed)):
            self.direction = random.randrange(0,360)
        else:
            self.temppos = self.position.getposition()
            while not self.room.isPositionInRoom(Position(self.temppos).getNewPosition(self.direction, self.speed)):
                self.temppos = self.position.getposition()
                self.direction = random.randrange(0,360)
        self.position = self.position.getNewPosition(self.direction, self.speed)
        self.room.cleanTileAtPosition(self.position.getposition())
        self.nummoves += 1

#Testing
runSimulation(num_robots= 1, speed= 5.0, width= 5, height= 5, min_coverage= 0.8, num_trials= 1, robot_type= RandomWalkRobot)


# === Problem 6

# For the parameters tested below (cleaning 80% of a 20x20 square room),
# RandomWalkRobots take approximately twice as long to clean the same room as
# StandardRobots do.
def showPlot3():
    """
    Produces a plot comparing the two robot strategies.
    """
    pylab.figure(3)
    pylab.title('comparing performance of Standard robot and RandomWalk robot')
    pylab.xlabel('Number of robots')
    pylab.ylabel('Mean steps')

    robotindex = []
    stnumsteps = []
    rdnumsteps = []
    for i in range(1,11):
        robotindex.append(i)
        stnumsteps.append(runSimulation(i, 1, 20, 20, 0.80, 5, StandardRobot))
        rdnumsteps.append(runSimulation(i, 1, 20, 20, 0.80, 5, RandomWalkRobot))

    pylab.plot(robotindex, stnumsteps, '-b', label = 'StandardRobot')
    pylab.plot(robotindex, rdnumsteps, '-r', label = 'RandomWalkRobot')
    pylab.legend(loc = 'upper right')
    pylab.text(5, 600, "StandardRobot performs about twice \n"
                          "better than RandomWalkRobot")
    pylab.show()

showPlot3()
