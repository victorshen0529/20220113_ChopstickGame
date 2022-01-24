'''
Chae Kim and Yingying Wang
CS111 Final Project
March 15th 2017
Chopstick Game

Victor Shen 
January 9th 2022
Expand Chae's and Yingying's logic from human vs. computer to computer 1 vs computer 2

This program allows a player to play Chopstick Game against the Computer. 

Rules:
Both computer and human players have two hands initially.  
Human starts the game first by using one of the hand to attack one of computer's hand.  
Computer will add your one finger to its exisiting fingers and extend the sum of the two.
On the next turn, computer uses its hand attack you. You now have to add its number to your
existing fingers on the attacked hand.
Take turns between players to attack each other’s hands.
When a player's hand reaches five fingers or more, that hand is considered "dead" 
and is no longer in play.
You can use your turn to switch to redistribute the number of fingers. 
You can also switch number to your ‘dead’ hand to bring it back.
The player loses if both hands are ‘dead’ 

Rules and pictures are adopted and edited from http://www.wikihow.com/Play-Chopsticks
'''

from stat import FILE_ATTRIBUTE_SPARSE_FILE
import graphics

import time
import random

class Hand:
    '''
    This class creates instances of a pair of hands, giving or updating the number of
    fingers on the hands through its methods.
    '''
    
    
    def __init__(self, left_fingers, right_fingers):
        """
        Constructor method
        The parameters take in the number of fingers on the left and right hand at the
        start of the game. 
        Create an instance variable for the number of fingers on the left and right hands
        """
        
        self.left_finger = left_fingers
        self.right_finger = right_fingers
        
        
    def get_R(self):
        """Return the number of fingers on the right hand at a given moment"""
        
        return self.right_finger
    
    
    def get_L(self):
        '''Return the number of fingers on the left hand at a given moment'''
        
        return self.left_finger
    
    
    def move_RtoL(self, number1):
        """
        This method is used to redistribute the fingers between a player's hands from right to left
        Take a number, number1, and subtract number1 from the right hand while simultaneously
        adding number1 to the left hand.
        """
        
        self.right_finger = self.right_finger - number1
        self.left_finger = self.left_finger + number1
        
            
    def move_LtoR(self, number2):
        """
        This method is used to redistribute the fingers between a player's hands from left to right
        Take a number, number2, and subtract number2 from the left hand while simultaneously
        adding number2 to the right hand.
        """
        
        self.right_finger = self.right_finger + number2
        self.left_finger = self.left_finger - number2
        
            
    def add_toR(self, number3):
        '''Add said number, number3, of fingers to the right hand'''
        
        self.right_finger = self.right_finger + number3
        
            
    def add_toL(self, number4):
        '''Add said number, number4, of fingers to the left hand'''
        
        self.left_finger = self.left_finger + number4
        
            
    def fist(self):
        '''
        Whenever a hand has 0 or 5 or more fingers, update the number of fingers to equal 0,
        which makes the hand out or dead.
        '''
        
        if self.right_finger <= 0 or self.right_finger >= 5:
            self.right_finger = 0
        if self.left_finger <= 0 or self.left_finger >= 5:
            self.left_finger = 0
            

class Game_Graphics:
    '''
    Game_Graphics class provides graphical instructions for the chopstick game
    '''
    
    
    def __init__(self):
        """Constructor that initializes the graphics window
        and information that we will use for displaying things"""
        
        self.win = graphics.GraphWin("Chopsticks", 675, 600)
        self.win.setBackground("Lavender Blush")
        self.h_r = None
        self.h_l = None
        self.c_r = None
        self.c_l = None
        self.h_turn_text = None
        self.c_turn_text = None
        self.comp_action = None
        self.text_attack = None
        self.error_message = None
        

    def introduction(self):
        '''
        This method will display introduction and rules to human player
        '''
        
        #this click_ thing tells the player to click to continue
        click_= graphics.Text(graphics.Point(600,550), "Click to Continue")
        click_.setStyle("bold italic")
        click_.setTextColor("Plum")
        click_.draw(self.win)
        
        #this part will display images for the rule
        Images = ["intro_pic.gif","r1.gif","r2.gif","r3.gif","r4.gif","r5.gif"]
        for im in Images:
            rules = graphics.Image(graphics.Point(337,300), im)
            rules.draw(self.win)
            click_p = self.win.getMouse()
            rules.undraw()
        rules_t = graphics.Text(graphics.Point(337,300),"The player loses if both hands are ‘dead’")
        rules_t.setTextColor("Dark Olive Green")
        rules_t.setSize(20)
        rules_t.draw(self.win)
        click_p = self.win.getMouse()
        rules_t.undraw()
        click_.undraw()
        
        
    def hand_images(self):
        '''
        This method will display images that represent human hands and computer hands
        '''
        
        c_lImage = graphics.Image(graphics.Point(130,275),"c_l.gif") 
        c_lImage.draw(self.win)
        c_rImage = graphics.Image(graphics.Point(478,275),"c_r.gif")
        c_rImage.draw(self.win)
        h_lImage = graphics.Image(graphics.Point(130,475),"h_l.gif")
        h_lImage.draw(self.win)
        h_rImage = graphics.Image(graphics.Point(478,475),"h_r.gif")
        h_rImage.draw(self.win)
        

    def hand_status(self, p1, p2):
        '''
        This method will display the status of current remaining fingers 
        for both computer and human
        
        p1 - hand instance of player 1(human)
        p2 - hand instance of player 2(computer)
        '''
        
        self.h_r = graphics.Text(graphics.Point(578,475), str(int(p2.get_R())))
        self.h_r.draw(self.win)
        self.h_r.setTextColor("Firebrick")
        self.h_r.setSize(20)
        self.h_r.setStyle("bold")
        self.h_l= graphics.Text(graphics.Point(230,475), str(int(p2.get_L())))
        self.h_l.draw(self.win)
        self.h_l.setTextColor("Firebrick")
        self.h_l.setSize(20)
        self.h_l.setStyle("bold")
        self.c_r= graphics.Text(graphics.Point(578,275), str(int(p1.get_R())))
        self.c_r.draw(self.win)
        self.c_r.setTextColor("Medium Slate Blue")
        self.c_r.setSize(20)
        self.c_r.setStyle("bold")
        self.c_l = graphics.Text(graphics.Point(230,275), str(int(p1.get_L())))
        self.c_l.draw(self.win)
        self.c_l.setTextColor("Medium Slate Blue")
        self.c_l.setSize(20)
        self.c_l.setStyle("bold")
    
    
    def dont_click(self):
        '''This method prints waring to the windown when the player does not click the button'''
        
        print("Do not click outside the buttons")
        self.error_message=graphics.Text(graphics.Point(506,50),"Please click the Button!")
        self.error_message.setStyle("bold")
        self.error_message.setTextColor("Midnight Blue")
        self.error_message.draw(self.win)
        
    	
    def undraw(self):
        '''This method will help update the information by undrawing 
        the previously drawn objects'''
        
        if self.h_r:
            self.h_r.undraw()
        if self.h_l:
            self.h_l.undraw()
        if self.c_r:
            self.c_r.undraw()
        if self.c_l:
            self.c_l.undraw()
        if self.h_turn_text:
            self.h_turn_text.undraw()
        if self.c_turn_text:
            self.c_turn_text.undraw()
        if self.comp_action:
            self.comp_action.undraw()    
    
    def h_turn(self, p1, p2):
        '''This method notify the human player that it is his or her turn to take actions
        and display current finger status
        
        p1 - hand instance of player 1(human)
        p2 - hand instance of player 2(computer)
        '''
        
        # the undraw makes it so the objects do not write over each other but actually
        #   erases before drawing again a different instance of the same kind.
        self.undraw()
        
        #this actually draws the text shown in the middle of the window
        self.h_turn_text = graphics.Text(graphics.Point(330,375),"Human's Turn")
        self.h_turn_text.setStyle("bold")
        self.h_turn_text.setTextColor("Maroon")
        self.h_turn_text.setSize(15)
        self.h_turn_text.draw(self.win)
        human_turn = self.hand_status(p1,p2)
        
            
    def c_turn(self, p1, p2, is_p1):
        '''This method displays computer's turn and current finger status
        
        p1 - hand instance of player 1(human)
        p2 - hand instance of player 2(computer)
        '''
        
        # the undraw makes it so the objects do not write over each other but actually
        #   erases before drawing again a different instance of the same kind.
        self.undraw()
        
        # these two fist functions are here to make sure that the numbers displayed for
        #   the status of every hands are updated before drawing themselves onto the
        #   window.  The repetiton is just for safety measures of these two functions
        #   throughout the code is for safety measures.
        p1.fist()
        p2.fist()
        
        # this draws the text shown in the middle of the window
        comp_turn = self.hand_status(p1,p2)\

        if (is_p1):
            self.c_turn_text = graphics.Text(graphics.Point(330,340),"Computer1's Turn")
        else:
            self.c_turn_text = graphics.Text(graphics.Point(330,340),"Computer2's Turn")

        self.c_turn_text.setStyle("bold")
        self.c_turn_text.setTextColor("Light Slate Blue")
        self.c_turn_text.setSize(15)
        self.c_turn_text.draw(self.win)
        

    def comp_dec(self,text):
        '''This method tells the human player the decisions of computer
        
        text - is the action computer does in its run
        '''
        
        self.comp_action = graphics.Text(graphics.Point(330,375), text)
        self.comp_action.setStyle("bold")
        self.comp_action.setTextColor("Cornflower Blue")
        self.comp_action.setSize(15)
        self.comp_action.draw(self.win)
        
        
    def get_button(self, p1x, p1y, p2x, p2y, message):
        """This method creates the buttons accoring to given position value
        
        p1x, p1y - x and y coordinates of a point that is on the 
            upper-left corner of a rectangle
        p2x, p2y - x and y coordinates of a point that is on the 
            lower-right corner of a rectangle
        message - the text to be written in the box drawn/the move the player can make
        """
        
        #get the top left and bottom right points to draw a rectangle
        p1 = graphics.Point(p1x,p1y)
        p2 = graphics.Point(p2x,p2y)
        rect = graphics.Rectangle(p1, p2)
        rect.draw(self.win)
        
        #draw text within the boxes
        label = graphics.Text(graphics.Point(p1x + 37, p1y + 25), message)
        label.setStyle("bold")
        label.draw(self.win)
        
        # returning the rectangle and label objects to be used for
        #   the erase obj function later
        return [rect, label]
    
    
    def click_button(self, p1y, p2y, click_lists):
        """
        General method that recognizes clicking of buttons.
        The p1y and p2y are the y coordinates of all the buttons made
        The click_lists is a list of numbers that tell which buttons have actually been
        made for a specific case.
        """
        
        # this snippet makes it so the 'Pick a button :)' text at the top erases every
        #   time someone clicks to prevent it writing over itself again and again.
        if self.text_attack:
            self.text_attack.undraw()
            
        # this snippet makes it so the 'Pick a button :)' text at the top redraws after
        #   being erased, so it is always at the top.
        self.text_attack = graphics.Text(graphics.Point(168,60), "Pick a button :) ")
        self.text_attack.setStyle("bold")
        self.text_attack.setSize(18)
        self.text_attack.draw(self.win)
        
        p = self.win.getMouse()
        
        # Return None to x so it could be assigned later in this function, but also so
        #   the entire game won't break if someone clicks outside the buttons.
        # The game should work just fine without this part, but it is just a safety
        #   measure to prevent bigger bugs.
        x = None
        
        # this undraws the error_message that pops up when someone clicks outside the
        #   buttons if such object is drawn already
        if self.error_message:
            self.error_message.undraw()
            
        # The y coordinates of the buttons drawn do not vary, so the if statement at the
        #   top makes sure what is being clicked is within one range of y for all buttons.
        if p1y <= p.getY() <= p2y:
            
            # this part actually does the recognizing of the clicks
            # the latter part of the if statements make sure that only the buttons
            #   that are currently drawn on the window can be clicked.
            # the values return essentially tell the computer what number button the
            #   player clicked
            if 50 <= p.getX()<= 125 and (0 in click_lists):
                x = 0          
            elif 175 <= p.getX() <= 250 and (1 in click_lists):
                x = 1
                
            elif 300 <= p.getX() <= 375 and (2 in click_lists):
                x = 2
                
            elif 425 <= p.getX() <= 500 and (3 in click_lists):
                x = 3
            elif 550 <= p.getX() <= 625 and (4 in click_lists):
                x = 4
            else:
                #if player clicks outside of button, print instruction
                self.dont_click()
                return self.click_button(100,150,click_lists)
            
        else:
            #if player clicks outside of button, print instruction
            self.dont_click()
            return self.click_button(100,150,click_lists)
        
        return x
    
    
    def erase_button(self, lists):
        """general function that takes in lists of graphics objects and deletes them"""
        
        for list in lists:
            for obj in list:
                obj.undraw()
                
                
    def get_attack(self, p1_r, p1_l, p2_r, p2_l):
        """
        creates buttons to choose type of attack.  returns the type of attack chosen.
        p1_r and p1_l are the number of fingers in the right and left hands of player 1
        p2_r and p2_l are the number of fingers in the right and left hands of player 2
        """
        
        # lists creates a list of buttons the need to be undrawn later
        lists = []
        
        # clicks_list1 creats a list of numbers that will later tell the click_button
        #   method above which buttons have actually been drawn
        click_list1 = []
        
        # the if else statements here make sure only the buttons for the moves the player
        #   is allowed to click on is drawn.
        # a specific number gets appended to click_list1 for each button being drawn
        if p1_r > 0:
            if p2_r > 0:
                self.attack0 = self.get_button(50, 100, 125, 150, "Attack Right \n w/ my Right")
                lists.append(self.attack0)
                click_list1.append(0)
    
            if p2_l > 0:
                self.attack1 = self.get_button(175, 100, 250, 150, "Attack Left \n w/ my Right")
                lists.append(self.attack1)
                click_list1.append(1)
        if p1_l > 0:
            if p2_r > 0:
                self.attack2 = self.get_button(300, 100, 375, 150, "Attack Right \n w/ my Left")
                lists.append(self.attack2)
                click_list1.append(2)
            if p2_l > 0:
                attack3 = self.get_button(425, 100, 500, 150, "Attack Left \n w/ my Left")
                lists.append(attack3)
                click_list1.append(3)
        if (p1_r > 1 or p1_l > 1) or (p1_r == 1 and p1_l == 1):
            attack4 = self.get_button(550, 100, 625, 150, "Switch \n w/ myself")
            lists.append(attack4)
            click_list1.append(4)
        
        # recognizes clicking of one the buttons by the player
        attack = self.click_button(100, 150, click_list1)
        
        # erases buttons drawn after click using method written below
        self.erase_button(lists)
                
        # returns to the method play later which attack move the player has chosen
        return attack
    
    
    def get_action(self, r, l):
        '''
        This method is for switching fingers between hands.
        It allows players to either choose to move from the right to the left hand
        or vice versa.
        It draws the buttons appropriate in certain situations and returns the action taken
        by the player in terms of the switch move.
        The r and l parameters return how many fingers are on the r and left hands of
        the human player
        '''
        
        # the action_list creates a list of buttons that are drawn and should be
        #   undrawn later
        action_list = []
        
        # the click_list2 creates a list of numbers that later tell the click_button
        #   method which buttons were actually made and are available to be clicked on
        click_list2=[]
        
        # creates only the buttons for moves available to the player in any given situation
        # appends information to lists made above to be used later in click_button method.
        if r > 0:
            action0 = self.get_button(50, 100, 125, 150, "Switch R to L")
            action_list.append(action0)
            click_list2.append(0)
        if l > 0:
            action1 = self.get_button(175, 100, 250, 150, "Switch L to R")
            action_list.append(action1)
            click_list2.append(1)
        
        # recognizes clicking of one of the buttons by player
        action = self.click_button(100, 150, click_list2)
        
        # erases buttons drawn after click using method written below
        self.erase_button(action_list)
                
        # returns the choice of the player(either move fingers from left to right hand
        #   or vice versa)
        return action
        
        
    def get_fingnum(self, fing_choiceR, fing_choiceL):
        '''
        Creates buttons to choose how many numbers of fingers to switch.
        Returns how many fingers to switch to the play method below.
        fing_choiceR and fing_choiceL are the number of fingers available to be
        switched the right or left hand of player1
        '''
        
        # creates buttons according to how many fingers are available to move
        # creates lists fing_list or click_list3 to return info to functions
        #   erase_button and click_button used below
        if fing_choiceR == 4:
            fing_num0 = self.get_button(50, 100, 125, 150, "1")
            fing_num1 = self.get_button(175, 100, 250, 150, "2")
            fing_num2 = self.get_button(300, 100, 375, 150, "3")
            fing_num3 = self.get_button(425, 100, 500, 150, "4")
            fing_list = [fing_num0, fing_num1, fing_num2, fing_num3]
            click_list3=[0,1,2,3]
        
        elif fing_choiceR == 3:
            fing_num0 = self.get_button(50, 100, 125, 150, "1")
            fing_num1 = self.get_button(175, 100, 250, 150, "2")
            fing_num2 = self.get_button(300, 100, 375, 150, "3")
            fing_list = [fing_num0, fing_num1, fing_num2]
            click_list3=[0,1,2]
            
        elif fing_choiceR == 2:
            fing_num0 = self.get_button(50, 100, 125, 150, "1")
            fing_num1 = self.get_button(175, 100, 250, 150, "2")
            fing_list = [fing_num0, fing_num1]
            click_list3=[0,1]
            
        elif fing_choiceR == 1:
            fing_num0 = self.get_button(50, 100, 125, 150, "1")
            fing_list = [fing_num0]
            click_list3=[0]
            
        # recognizes clicking of one of the buttons by player
        fing_num = self.click_button(100, 150, click_list3)
        
        # erases buttons drawn after click using method written below
        self.erase_button(fing_list)
        
        # if the number of fingers being switched between the hands doesn't change the
        #   situation (ex. right has 2 fingers, left has 3 fingers, switch 1 finger from left
        #   to right so now right has 3 and left has 2), show an error message and force
        #   the player to choose a different button
        if fing_choiceR == (fing_choiceL + fing_num + 1):
            print("Move not allowed. Choose again.")
            self.error_message=graphics.Text(graphics.Point(500,50),"That's the same!! Pick again.")
            self.error_message.setStyle("bold")
            self.error_message.setTextColor("Red")
            self.error_message.draw(self.win)
            return self.get_fingnum(fing_choiceR, fing_choiceL)
        
        # return the number of fingers to move chosen by the player
        return fing_num
    
    
    def humanwin(self):
        '''This method will show congratulating message when human play wins'''
        
        self.undraw()
        
        h_win_text = graphics.Text(graphics.Point(330,375),"Yay! You are the chopsticks master!")
        h_win_text.setStyle("bold")
        h_win_text.setTextColor("Gold")
        h_win_text.setSize(20)
        h_win_text.draw(self.win)
        
    
    def compwin(self, did_p1_win):
        '''This method will tell the human player that he or she loses the game'''
        
        self.undraw()
        if (did_p1_win):
             c_win_text = graphics.Text(graphics.Point(330,375),"Computer1 won!")
        else:
             c_win_text = graphics.Text(graphics.Point(330,375),"Computer2 won!")
        c_win_text.setStyle("bold")
        c_win_text.setTextColor("Brown")
        c_win_text.setSize(20)
        c_win_text.draw(self.win)
        
    
    def close(self):
        """This method closes the game window"""
        
        click_2= graphics.Text(graphics.Point(600,550), "Click to EXIT the game")
        click_2.setStyle("bold italic")
        click_2.setTextColor("Plum")
        click_2.draw(self.win)
        click=self.win.getMouse()
        self.win.close()
        
                
class A_chopsticks:
    '''
    
    '''
    def __init__(self, game_g, p1, p2):
        '''
        p1 is the human player and p2 is the computer
        '''
        self.game_g = game_g
        self.play(p1, p2, game_g)
        
    # this function checks after P2 makes his/her move, whether P1 has any moves that
    #   will make P2 lose
    def isSituationSafe(self, p1L, p1R, p2L, p2R):
        # todo: will use fist() or move the following paragraph outside of isSituationSafe
        # check for P1's outs (any hand >= 5) as the result of the previous P2's move/attack
        if (p1L >= 5):
            p1L = 0
        if (p1R >= 5):
            p1R = 0

        # if both P2's hands are alive (> 0), return True and exit because even one hand
        #   is killed, P2 is still alive
        if ((p2L != 0) and (p2R != 0)):
            return True

        # find the P1's attacking hand (the bigger hand) and P2's victim hand (the non-zero hand)
        p1B = None
        if (p1L > p1R):
            p1B = p1L
        else:
            p1B = p1R
        
        p2N = None
        if (p2L > 0):
            p2N = p2L
        else:
            p2N = p2R
        
        # check if the victim hand will die in P1's next turn
        if ((p1B + p2N) >= 5):
            return False
        else:
            return True

    def comp_play_p1_switch(self, p1, p2):
        text = ""
        if ((p1.get_R() - p1.get_L()) > 1):
            if p1.get_R() % 2 == 0:
                #computer1 switched Right to Left(even)
                p1.move_RtoL((p1.get_R()/2))
                text = "Computer1 decides to switch from its RIGHT to LEFT"
            else:
                #computer1 switched Right to Left(odd)
                p1.move_RtoL((p1.get_R()//2))
                text = "Computer1 decides to switch from its RIGHT to LEFT"
        elif ((p1.get_L() - p1.get_R()) > 1):
            if p1.get_L() % 2 == 0:
                #computer1 switched Left to Right(even)
                p1.move_LtoR((p1.get_L()/2))
                text = "Computer1 decides to switch from LEFT to RIGHT "
            else:
                #computer1 switched Left to Right(odd)
                p1.move_LtoR((p1.get_L()//2))
                text = "Computer1 decides to switch from LEFT to RIGHT"
        return text

    def comp_play_p1_attack(self, p1, p2):
        text = ""
        if p1.get_R() >= 1:
            if p2.get_R() > 3:
                #computer1 attacks Right with Right
                p2.add_toR(p1.get_R())
                text = "Computer1 decides to attack computer2's RIGHT with its RIGHT"
            elif p2.get_L() > 3:
                #computer1 attacks Left with Right
                p2.add_toL(p1.get_R())
                text = "Computer1 decides to attack computer2's LEFT with its RIGHT"
            elif p2.get_L() >= 1:
                #computer1 attacks Left with Right
                p2.add_toL(p1.get_R())
                text = "Computer1 decides to attack computer2's LEFT with its RIGHT"
            elif p2.get_R() >= 1:
                #computer1 attacks Right with Right
                p2.add_toR(p1.get_R())
                text = "Computer1 decides to attack computer2's RIGHT with its RIGHT"
        elif p1.get_L() >= 1:
            if p2.get_R() > 3:
                #computer1 attacks Right with Left
                p2.add_toR(p1.get_L())
                text = "Computer1 decides to attack computer2's RIGHT with its LEFT"
            elif p2.get_L() > 3:
                #computer attacks Left with Left
                p2.add_toL(p1.get_L())
                text = "Computer1 decides to attack computer2's LEFT with its LEFT"
            elif p2.get_R() >= 1:
                #computer attacks Right with Left
                p2.add_toR(p1.get_L())
                text = "Computer1 decides to attack computer2's RIGHT with its LEFT"
            elif p2.get_L() >= 1:
                #computer attacks Left with Left
                p2.add_toL(p1.get_L())
                text = "Computer1 decides to attack computer2's LEFT with its LEFT"
        return text

    def comp_play_p1(self, p1, p2, game_g):
        '''
        This program is the intelligence for computer1 to use the old AI to find the next move.
        p1 is the hand instance of computer1, and p2 is the hand instance of 
        computer2.  game_g is a Game_Graphics instance.
        '''
        
        # create an empty string which later gets updated to hold text that explains the
        #   next move of the computer which will get used in method comp_dec for p1.
        text =""
        
        # various moves the computer should take depending on the current situation.
        #   to sum it up, when available, always bring back the 'dead' hand through the
        #   switch move.  Then attack whatever hand has 4 fingers.  Then attack the left
        #   or right hand depending on whichever is not 'dead'

        # will comment later
        ran_num = random.randint(0, 0)
        if (ran_num == 0):
            text = self.comp_play_p1_switch(p1, p2)
            if (text == ""):
                text = self.comp_play_p1_attack(p1, p2)
        else:
            text = self.comp_play_p1_attack(p1, p2)
            if (text == ""):
                text = self.comp_play_p1_switch(p1, p2)
        
        # draws text on window explain the move the computer will make
        game_g.comp_dec(text)
        
        # delays the window from erasing info shown by comp_dec and 
        #   drawing the next sequence of actions
        time.sleep(3.2)
        
        # prints to command line for reference
        print (text)

    def comp_play_p2(self, p1, p2, game_g):
        '''
        This program is the intelligence for the computer to go off of.
        p1 is the hand instance of the human player, and p2 is the hand instance of the
        computer.  game_g is a Game_Graphics instance.
        '''
        
        # create an empty string which later gets updated to hold text that explains the
        #   next move of the computer which will get used in method comp_dec.
        text =""
        
        # this AI strategy always tries to attack, as long as such a move is safe, meaning
        #   P2 won't die after it attacks. if P2 doesn't have a safe attack move, do switch
        #   instead
        foundAGoodMove = False
        # we only use a non-zero hand to attack and only attack a non-zero hand
        if ((p1.get_L() > 0) and (p2.get_L() > 0) and self.isSituationSafe(p1.get_L() + p2.get_L(), p1.get_R(), p2.get_L(), p2.get_R())):     
            p1.add_toL(p2.get_L())
            text = "Computer2 decides to attack computer1's LEFT with its LEFT"
            foundAGoodMove = True
        elif ((p1.get_L() > 0) and (p2.get_R() > 0) and self.isSituationSafe(p1.get_L() + p2.get_R(), p1.get_R(), p2.get_L(), p2.get_R())):
            p1.add_toL(p2.get_R())
            text = "Computer2 decides to attack computer1's LEFT with its RIGHT"
            foundAGoodMove = True
        elif ((p1.get_R() > 0) and (p2.get_L() > 0) and self.isSituationSafe(p1.get_L(), p1.get_R() + p2.get_L(), p2.get_L(), p2.get_R())):
            p1.add_toR(p2.get_L())
            text = "Computer2 decides to attack computer1's RIGHT with its LEFT"
            foundAGoodMove = True
        elif ((p1.get_R() > 0) and (p2.get_R() > 0) and self.isSituationSafe(p1.get_L(), p1.get_R() + p2.get_R(), p2.get_L(), p2.get_R())):
            p1.add_toR(p2.get_R())
            text = "Computer2 decides to attack computer1's RIGHT with its RIGHT"
            foundAGoodMove = True
        else:
            # loop through all possible numbers for P2's left hand
            for i in range(0,p2.get_L() + p2.get_R()):
                # don't do a switch if the hands will stay the same (only the numbers on the two hands
                #   are switched)
                if ((p2.get_L() == i) and (p2.get_R() == (p2.get_L() + p2.get_R() - i))):
                    continue
                
                if (self.isSituationSafe(p1.get_L(), p1.get_R(), i, p2.get_L() + p2.get_R() - i)):
                    # from the value of i, determine if P2 wants to switch from L to R or vice versa
                    if (i < p2.get_L()):
                        #computer switched Left to Right
                        p2.move_LtoR(p2.get_L() - i)
                        text = "Computer2 decides to switch from its LEFT to RIGHT"
                        foundAGoodMove = True
                    else:
                        #computer switched Right to Left
                        p2.move_RtoL(i - p2.get_L())
                        text = "Computer2 decides to switch from its RIGHT to LEFT"
                        foundAGoodMove = True
                    break
        
        # if none of the options work, do a random option
        if (foundAGoodMove == False):
            p1.add_toL(p2.get_L())
            text = "Computer2 has no other choice but to attack computer1's LEFT with its LEFT"

        
        # draws text on window explain the move the computer will make
        game_g.comp_dec(text)
        
        # delays the window from erasing info shown by comp_dec and 
        #   drawing the next sequence of actions
        time.sleep(3.2)
        
        # prints to command line for reference
        print (text)

    def display_info(self, p1, p2):
        '''
        Display the current situation in the game on the command line.
        p1 is an instance hand made for the human player
        p2 is an instance hand made for the computer
        '''
        
        print("Player 1(human) Status: Left Hand = %d, Right Hand = %d" % (p1.get_L(),p1.get_R()))
        print("Player 2(computer) Status: Left Hand = %d, Right Hand = %d" % (p2.get_L(), p2.get_R()))
        print("\n")
        
        
    def play(self, p1, p2, game_g):
        '''
        This program actually plays the game with use of input from the player
        p1 is a Hand instance made for the human player
        p2 is a Hand instance made for the computer
        game_g is an instance of the Game_Graphics class
        '''
        
        # draws the hand images onto the window
        game_g.hand_images()
        
        # while neither of the players are out, play the game!
        while (True):
            # step 1: computer 1's turn
            # print to the command line the situation of the game
            self.display_info(p1, p2)
            print("Player 1(computer 1)'s Turn")
            
            # it is computer 1's turn. Use the intelligence for the computer to go
            game_g.c_turn(p1,p2,True)
            self.comp_play_p1(p1, p2, game_g)  

            # step 2: check if computer 2 has died
            # make sure to update the instance variables using the fist method before
            #   determining if the game should continue on or stop
            p1.fist()        
            p2.fist()
            
            # if game shall stop because computer 2 lost
            if (p2.get_R() == 0 and p2.get_L() == 0):
                self.display_info(p1, p2)
                print("Computer 1 won!")
                game_g.compwin(True)
                break
            
            # step 3: computer 2's turn
            # if the game shall go on
            self.display_info(p1, p2)
            print("Player 2(computer 2)'s Turn")
            
            # it is the computers turn.  Use the intelligence for the computer to go
            game_g.c_turn(p1,p2,False)
            self.comp_play_p2(p1, p2, game_g)  
            
            # step 4: check if computer 1 has died
            # make sure to update the instance variables using the fist method before
            #   determining if the game should continue on or stop
            p1.fist()
            p2.fist()
            
            # if the game should stop because the human player lost
            if (p1.get_R() == 0 and p1.get_L() == 0):
                self.display_info(p1, p2)
                print("Computer 2 won!")
                game_g.compwin(False)
                break
            
        game_g.close()
        exit()
    
    
def main():
    '''
    The main function creates two instances of the hand, one for computer 1 (one AI
    strategy) and another for computer 2 (a different AI strategy).  It then brings
    in the graphics and plays the game!
    '''
    p1 = Hand(1,1)
    p2 = Hand(1,1)
    game_g = Game_Graphics()
    game_g.introduction()
    g = A_chopsticks(game_g, p1, p2)
    
        
if __name__ == '__main__':
    main()