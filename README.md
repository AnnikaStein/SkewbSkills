# SkewbSkills
Practice and learn skewb algs, first layer and more!

This description intends to show you how to use SkewbSkills and give a quick overview on the development process.

SkewbSkills is free to use for all skewbers out there (!) and has been created by Annika Stein (also known as HugaCuba on social media such as YouTube or Instagram) to
+ practice the first layer
+ practice algs for the last two layers
+ practice programming with python and qt. ;)

![SkewbSkills Logo](logogreen.png)

# What's new?
You can now download and use the first version of SkewbSkills! Browse through the source code on [github](https://github.com/AnnikaStein/SkewbSkills) or simply run the
executable and have fun! More info on how to install your own copy of SkewbSkills down below.

# What's planned?
+ Improve the way the scrambles are generated / processed to reduce the file sizes
+ Make video on how to install and use SkewbSkills
+ Add other practicing modes, or modify the current ones:
   + I'd like the user to identify his / her weak algs and put them on a special pile to work on particularly
   + add timer to the first layer trainer
   + add quiz where you only see three faces and have to identify the case
   + add competition sim where you get five scrambles, but only four times a day ;)
   + add statistics for every L2L case that shows improvement
   + function to identify which cases you know, where you can put in your own algs and keep track of the cases you know
+ Make SkewbSkills available to more platforms than Windows

# Installation
Download the zip-file, containing the .exe, some pictures and .txt files. Do not move the .txt-files out of the directory, they contain the scrambles.
Actually, using my pictures is not necessary, but they are included for design purposes.

To open the program, extract the zip-folder and open "MainWindow.exe", either by using the executable itself, by defining
a shortcut (which is pretty nice if you want to put the program on your desktop or the taskbar), or by running the MainWindow.py-code (for those of you that have a python interpreter set up).

*Note*: since the .exe is really new and not many people use it, you might have to allow your computer to execute it. This also
applies to antivirus software if you use some.

# Usage
## Starting Window
Choose any from the different practicing modes, by pressing the corresponding button or key, respectively. A new window appears, the
starting window closes. Note: the First Layer Trainer takes some time to open, so be a little patient.

## First Layer Trainer
Currently, the First Layer Trainer is pretty slow, so do not expect it to open immediately after you start it.
There's a slider to define the length of the scrambles, you can choose between 1 and 7 moves. If you want the scrambles to be 
shuffled, use the checkbox "Shuffle scrambles". The checkbox "Use all colours" allows SkewbSkills to show you various colours so that
you can practice to start the first layer with every color (to become CN). When you're ready with the customization, press
"Generate Scramble + Colour" (or Space). A new scramble appears, both as a label containing the scramble sequence, and with a drawing.
*Small warning*: the more moves you select, the larger the files are that contain the scrambles. Therefore, it might take a little until
the process is completed. In further versions, this should not be the case anymore.

## L2L Alg Trainer
Select all the alg sets that you'd like to practice. SkewbSkills is going to shuffle (randomize) the order in which they appear.
Use the "Generate L2L Scramble" Button or press Return to generate a scramble. A drawing of the scramble appears. All scrambles are
performed with the White/Red/Green Corner on top/front. Start the timer with the "Start" Button or press Space. After starting the
timer, you can stop it again by clicking the same button ("Pause") or pressing Space again. You can than reset the timer to zero by
using the "Reset" button (or press "R").

## Your own algs
You do not need to change anything on any file anymore once you've extracted the folder. But:
if you find that you'd like other scrambles to be displayed than the current ones, open any of the .txt-Docs and modify the
scrambles to your liking. If you want to keep track of which scrambles generate which case, see
[this document](https://docs.google.com/spreadsheets/d/1j-SGlgZk20D3d2TyeiXhMWzeyTBuuix3Owgj9Q8rNbo/edit#gid=1743463298)
(credits: Elias Malomgré and Carter Cucala). I use the same terms for the cases to indicate them, as well as the same order.
When modifying the scrambles in the .txt-Files, note that the very last character of the file must be one space in the line of the
last scramble. So do not make any additional line break after the last scramble, but end the line of the last scramble with a space.
In almost the same manner, do not use a space or anything else to end the previous scrambles. All lines that are not the last line
should only contain the scramble itself, ending with the last move. If you do not apply the steps above, your program might crash
(because it can only read and use the scrambles provided in the form mentioned earlier).

# Credits
As I am just starting out Python (and PyQt5), I had a lot of input from various online sources.
I learned a lot from [this playlist](https://www.youtube.com/playlist?list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa)
by Parwiz Forogh and also used [this project](https://github.com/enkore/qt-stop-watch.py/blob/master/qt-stop-watch.py) by enkore
to get the stopwatch running. Also thanks to Mattheo de Wit, who created a similar (but web-based) [application!](https://yutu58.github.io/?fbclid=IwAR2cVMBE9LneUZ1J0XpDWPcTV2XjGsCDmXmTCIu4qhWUh7EJIDhA-f0eNTY)
This was a big influence on how the L2L-Trainer should work.

When reading the [LICENSE](https://github.com/AnnikaStein/SkewbSkills/blob/master/LICENSE) doc, you might find out that you are not only free to use the program, but also the source code.
This is to ensure everyone can learn something, of course I appreciate every suggestion for improvement, as I might actually be the one to learn something through this project! :)

# Other links
If you want to get to know about my other activities in cubing, visit my youtube channel:
[HugaCuba](https://www.youtube.com/channel/UCbqOLjnPUxAvBx2GB3tTZAw/).

