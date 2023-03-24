import pygame, sys, math
from rails import*
from Bumps import*
from Obstacles.py import*


def loadLevel (lev):
    f = open("levels/"+lev, 'r')
    lines = f.readlines()
    f.close()
    
    size = 50
    offset = size/2
    tiles = []
    walls = []
    spawners = []
    
    newLines = []
    for line in lines:
        newLine = ""
        for c in line:
            if c != "\n":
                newLine += c
        newLines += [newLine]
        
    lines = newLines
    
    
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                walls += [Wall([x*size+offset, y*size+offset])]
            if c == "X":
                spawners += [Spawner([x*size+offset, y*size+offset])]
                
    tiles = [walls, 
            spawners]
    return tiles
