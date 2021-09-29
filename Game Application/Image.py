'''
Brian Nguyen
Final Project: Mastermind Game
CS 5001 Spring 2021
'''

import turtle


class Image:
    '''
    This is a class that is used to create Image objects for my Mastermind game,
    specifically all the option buttons and game notifications are created
    based on this class. It has two methods: new_image() and clicked()
    '''

    def __init__(self, position, gif_file):
        '''
        The constructor for the Image class: create an Image object using turtle

        Parameters:
            position (object): create using the Point class provided
            gif_file (string): a gif file containing the using image
        
        Returns nothing    
        '''

        # create a screen using turtle
        self.screen = turtle.Screen()
        # create a turtle object using the new_image() method
        self.image = self.new_image()
        self.position = position
        self.gif_file = gif_file
        # set the properties for our turtle object
        self.image.speed(0)
        self.image.up()
        self.image.goto(self.position.x, self.position.y)
        # add the image to our game
        self.screen.addshape(self.gif_file)
        self.image.shape(self.gif_file)

    
    def new_image(self):
        '''
        Create a turtle object

        No parameters

        Returns a turtle object
        '''
        
        return turtle.Turtle()


    def clicked(self, x, y):
        '''
        Check to see if we clicked within the Image object

        Parameters:
            x (float): the x coordinate of our mouse click
            y (float): the y coordinate of our mouse click

        Return True (boolean value) if we clicked within the Image object,
        False (boolean value) otherwises.
        '''
        
        if abs(x - self.position.x) <= 40 and \
           abs(y - self.position.y) <= 40:
            return True
        return False
