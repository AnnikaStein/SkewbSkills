# SkewbSkills
Practice and learn skewb algs, first layer and more!

This description intends to show you how to use SkewbSkills. SkewbSkills is free to use
for all skewbers out there! 

# What's new?
You can now download and use the first version of SkewbSkills! Browse through the source code or simply run the
executable and have fun! More info on how to install your own copy of SkewbSkills down below.

# Installation
Take the zip-files, containing the .exe, some pictures and .txt files. Do not move the .txt-files out of the directory, they contain the scrambles.
Using my pictures is not necessary, but they are included for design purposes.

To open the program, extract the zip-folder and open "MainWindow.exe", either by using the executable itself, by defining
a shortcut (which is pretty nice if you want to put the program on your desktop or the taskbar), or by running the MainWindow.py-code (for those of you that have a python interpreter set up).

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
"Small warning": the more moves you select, the larger the files are that contain the scramble. Therefore, it might take a little until
the process is completed.

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
I learned a lot from [this playlist](https://www.youtube.com/playlist?list=PL1FgJUcJJ03uO70zDLDF3oaTu6s2QLOPa)
by Parwiz Forogh. I also used [this project](https://github.com/enkore/qt-stop-watch.py/blob/master/qt-stop-watch.py) by enkore
to get the stopwatch running. Also thanks to Mattheo de Wit, who created a similar (but web-based) [application!](https://yutu58.github.io/?fbclid=IwAR2cVMBE9LneUZ1J0XpDWPcTV2XjGsCDmXmTCIu4qhWUh7EJIDhA-f0eNTY)

