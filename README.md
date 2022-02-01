# Chopstick Game in Python for Kids

This program allows kids to play Chopsticks against a computer. To play the game, you need a computer with Python installed. The OS can be Windows, Mac, Linux, etc.

This code repo is based on Yingying and Chae's previous work on Chopstick-game.
<code>https://github.com/yingyingww/Chopstick-game</code>


## How to Download the Source Code
You can use either HTTPS or SSH to clone the code repo:

<code>git clone https://github.com/victorshen0529/20220113_ChopstickGame.git</code>, or

<code>git clone git@github.com:victorshen0529/20220113_ChopstickGame.git</code>

## How to Run This Program

You need to go the the directory of the source code. In a terminal, type

<code>python3 chopsticks.py</code>

Alternatively, you can load the directory in Visual Studio Code (https://code.visualstudio.com/download), select chopsticks.py, and click the run button.

## Game Rules

In this game, there are P1 and P2. P1 is the human player, and P2 is the computer. Both players have two hands. P1 moves first. There are buttons for the human to click depending on what he or she wants to do. When a hand reaches zero, that hand is out. If both hands of a player are out, that player loses.

## Software Structure

There are two files. One is chopsticks.py and the other is graphics.py. Graphics.py is a third-party graphics library, which does not have any logic related to the game. Chopsticks.py is the code of the game. There are three classes, namely Hand, GameGraphics, and A_chopsticks. Hand creates the instances of the hands, and updates them through its methods. GameGraphics provides graphics for the game. For example, displaying win or lose messages. A_chopsticks is the most important. It contains the computer's AI. The AI is in isSituationSafe() and comp_play(). Play() is the main loop of the game.

## Future Work

I want to look through the computers AI to look at why it always switches.

## Contact the Author
If you have any questions or see any bugs, please write them in the issues of the code repo. I look forward to hearing from you!
