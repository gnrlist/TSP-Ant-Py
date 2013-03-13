#!/usr/bin/python
# coding: utf-8
## TSP virtual ant colony implementation


import random
import math
import sys
import os
from collections import deque
import time

# Ant Class
# class to hold ant objects
class Ant:
   """Class for ant objects"""
# nextCity(curCity, Ci)        determines the next edge
   def nextCity(curCity, unvisCities):
       """Determine the next city to visit and move ant"""        
       # compare options
       # add city to cities visited list
       # total pheromone
       pherTot = 0.0
       # total inverse distance
       invDistTot = 0.0
       #list of edges
       edgeList = []
       edgeTuples = []
       edgeProbs = []
       #pheromone weight
       pw = math.sin(v)**2
       #distance weight
       dw = 1 - pw

       for city in self.validCities:
           if curCity < city:
               curEdge = edges.get((curCity,city))
           else:
               curEdge = edges.get((city,curCity))
           edgeList.append(curEdge)
           edgeTuples.append(curEdge.ends)
           pherTot = pherTot + curEdge.pheromone
           invDistTot = invDistTot + (1/curEdge.distance)
       
       for edge in edgeList:
           p = dw*(1/edge.dist)/invDistTot + pw*(edge.pheromone)
           edgeProbs.append(p)

       nextEdge = random_pick(edgeTuples, edgeProbs)
       return edges.get(nextEdge)
       
   # dripPher        adds pheromone to travelled edges
   def dripPher(pher):
       """Add pheromone to edges travelled"""
       # update pheromone level on edges
       for i in edges:
           i.updPher(pher)
       
           # gives list of city id, x coord, y coord
           l = line.split()


   def __init__(self, curCity):
       """Initialize the ant object"""
       self.distance = 0 # initially 0
       # cities                cities that have been visited
       self.cities = deque()  
       # edges traveled
       self.cities.append(curCity)
       # print "curCity\t" + str(curCity)
       self.unvisCities = cityList.difference(self.cities)
       self.curCity = curCity
       self.edges = []

       while(self.unvisCities != set([])):

           self.curEdge = self.nextCity(self.curCity, self.unvisCities)
           # print "curEdge\t" + str(self.curEdge)
           if self.curCity == self.curEdge.ends[0]:
               # print "curCity == curEdge.ends[0]"
               self.cities.append(self.curEdge.ends[1])
               self.curCity = self.curEdge.ends[1]
           else:
               # print "curCity == curEdge.ends[1]"               
               self.cities.append(self.curEdge.ends[0])
               self.curCity = self.curEdge.ends[0]
           # print "cities\t" + str(self.cities)

           self.unvisCities = cityList.difference(self.cities)
           # print "unvisCities\t" + str(self.unvisCities)
           self.distance = self.distance + self.curEdge.distance
           # print "distance\t" + str(self.distance)
           self.edges.append(self.curEdge)
           # print "curCity\t" + str(self.curCity)
       return

   # methods                
   # nextCity(curCity, Ci)        determines the next edge
   def nextCity(self, curCity, unvisCities):
       """Determine the next city to visit and move ant"""        
       # compare options
       # add city to cities visited list
       # total pheromone
       pherTot = 0.0
       # total inverse distance
       invDistTot = 0.0
       #list of edges
       edgeList = []
       edgeTuples = []
       edgeProbs = []
       #pheromone weight
       pw = math.sin(v)**2
       #distance weight
       dw = 1 - pw

       for city in self.unvisCities:
           if curCity < city:
               curEdge = edges.get((curCity,city))
           else:
               curEdge = edges.get((city,curCity))
           edgeList.append(curEdge)
           edgeTuples.append(curEdge.ends)
           pherTot = pherTot + curEdge.pheromone
           
           # print str(curEdge)
           # print str(curEdge.distance)
           # print str(1.0/curEdge.distance)
           invDistTot = invDistTot + (1.0/curEdge.distance)
       # print pherTot
       # print invDistTot
       for edge in edgeList:
           p = dw*(1/edge.distance)/invDistTot + pw*(edge.pheromone)/pherTot
           edgeProbs.append(p)
           

       nextEdge = random_pick(edgeTuples, edgeProbs)
       return edges.get(nextEdge)
       
   # dripPher        adds pheromone to travelled edges
   def dripPher(self, pher):
       """Add pheromone to edges travelled"""
       # update pheromone level on edges
       for i in self.edges:
           i.updPher(pher)
       
  
           
## class to hold edge objects
class Edge:
   pheromone =0
   ends = ()
   distance =0
   def __init__(self, a, b):
       self.pheromone = 1
       # print self.pheromone
       self.ends = a[0],b[0]
       self.distance = int(round(math.sqrt((a[1]-b[1])**2+(a[2]-b[2])**2),1))
       if (self.distance == 0.0):
           f = open('zerofile.txt', 'w')
           f.write(str(self.distance))
           f.write(str(self.ends))
           f.write(str(self.ends[0]))
           f.write(str(self.ends[1]))
   def updPher(self, pher):
       self.pheromone = self.pheromone+pher
   def decayPher(self, rate):
       # set rate to baseline
       if rate == 0:
           self.pheromone = 1
       # multiple pheromone by rate
       elif rate > 0:
           self.pheromone = rate * self.pheromone
       elif rate < 0:
           return
       return

   def __repr__(self):
       return "Edge: " +str(self.ends[0]) + " to " + str(self.ends[1])
   def __str__(self):
       stringToReturn = "Edge: " +str(self.ends[0]) + " to " + str(self.ends[1])
       return stringToReturn



   
## script to read file and get city id's x and y coordinates
##Where the cities are a nested tuple of the format:
## City[0] = City Name and City[1] = (x_coord, y_coord)
## City[1][0] = x_coord and City[1][1] = y_coord
def parseInput(file):
   ##Read a file and return a datastructure of all cities
   cities = []
   # open file
#   with open(file,'r') as f:
       # read each line, store
 #      for line in f:
           # gives list of city id, x coord, y coord
  #         l = line.split()
   #        cityToAdd = (int(l[0]),float(l[1]),float(l[2]))
    #       cities.append(cityToAdd)
#   f.closed
   f = open(file, 'r+')
   lines = f.readlines()
   for i in range(0, len(lines)):
       line = lines[i]
       l = line.split()
       cityToAdd = (int(l[0]),float(l[1]),float(l[2]))
       cities.append(cityToAdd)

   f.close()
   return cities



## takes the input list of cities outputs
## creates a list of all Edges
## each Edge calculates it’s distance between cities
## returns the list.  Access: edgeList[0] = first edge, edgeList[0].distance = length
def edgeMaker(input):
   listOfEdges = []
   i = 0
   for city in input:
       for otherCity in input:
           if (city[0] < otherCity[0]):
               listOfEdges.append(Edge(city, otherCity))
           elif (city > otherCity):
               listOfEdges.append(Edge(otherCity, city))
   
               



   # while i < len(cities):
   #     for otherCity in cities:
   #         if (cities[i] != otherCity):
   #             listOfEdges.append(Edge(cities[i], otherCity))
   #     i += 1
   return listOfEdges

## helper function for antSorter (mergeSort)
def merge(l, r):
    result = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i].distance <= r[j].distance:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result += l[i:]
    result += r[j:]
    return result
   
## sorts ants by distance (ascending) -- mergeSort algorithm
def antSort(ants):
    """Takes a list of ants and returns a sorted list of ants"""
    if len(ants) <= 1:
        return ants
    mid = int(len(ants)/2)
    l = antSort(ants[:mid])
    r = antSort(ants[mid:])
    return merge(l,r)
 
           
def outputCities(distance, cities,outfile):
   """Write cities to file given parameters distance of optimal path, city names in optimal path, and the output file name"""  
   #open the file and write the old results and new ones too7
   # first line is distance of optimal path
   # next n lines are city names
   f = open(outfile,'w')
   distance = str(distance)+ '\n'
   f.write(distance)
   for c in cities:
       city = str(c) + '\n'
       f.write(city)
   f.close()


   
def main():
   ## dictionary to hold edge objects with k = (c1,c2) and v = edge
   global edges
   edges = {}
   ## SETUP Variables
   global v
   shortestDist = float('inf')
   decayF = random.random()
   global startingCity
   v = .80
   curCityShort = float('inf')
   iterations = 8
   numAnts = 15
   
   ## list of all cities
   input = parseInput(sys.argv[1])
   global cityList
   cityList = set()
   randomCity = int(random.random()*len(input))
   startingCity = input[randomCity][0]   
   cityCount = 0
   #tries diff variations of decay per city
   for i in input:
       print str(i)
       print "adding " + str(i[0]) + " to cityList"
       cityList.add(i[0])
       cityCount = cityCount+1
   ## make edges
   edgeList = edgeMaker(input)
   for edge in edgeList:
       edges[edge.ends] = edge
   # unleash the ants
   for varyV in range(iterations):
       j = 0
       #vary the starting city
       while j < (len(cityList)/(iterations)):
           ants = []
           randomCity = int(random.random()*len(input))
           startingCity = input[randomCity][0]
           # number of ants
           for c in range(numAnts):
               ants.append(Ant(startingCity))
           sortAnts = antSort(ants)
           # Pheromene decay
           # set to 0 for full decay: return to baseline = 1
           # set to 0<n<1 for a fractional decay level
           # set to -1 for no decay
           for edge in edgeList:
               edge.decayPher(decayF)
           
           for k in range(len(sortAnts)):
               sortAnts[k].dripPher(len(sortAnts) - k)      
               if sortAnts[k].distance < shortestDist:
                   fastestAnt = k
                   shortestDist = sortAnts[k].distance
                   shortestPath = sortAnts[k].cities
                   topDec = decayF
               if sortAnts[k].distance < curCityShort:
                   curCityShort = sortAnts[k].distance
           print "ShortestPath: " + str(shortestDist) #+":\n"+ str(shortestPath)
           #let comp tune   
           if sortAnts[k].distance<= (curCityShort*1.3):
              decayF += (random.random()-.5)/30
           else:
               decayF= random.random()
           outputCities(shortestDist, shortestPath, sys.argv[2])
           j += 1

       print "ShortestPath: " + str(shortestDist) + " Ants: " + str(numAnts)
       v = v + 1


   
def random_pick(some_list, probabilities):
   random.seed()
   x = random.uniform(0, 1)
   cumulative_probability = 0.0
   for item, item_probability in zip(some_list, probabilities):
       cumulative_probability += item_probability
       if x < cumulative_probability: break
   return item    
   

if __name__ == '__main__':
   main()    
   
   
   
   
   
  



