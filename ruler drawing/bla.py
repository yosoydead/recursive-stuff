'''
    In general, an interval with a central tick length L >= 1 is composed of:
        * an interval with a central tick length L-1
        * a single tick of length L
        an interval with a central tick length L-1
'''

#first, i start by drawing a line
#with a given tick length
#if there is a tick label given, append that
#label to the line
def drawLine(tickLength, tickLabel=""):
    #using the functionality of python to
    #generate a string containing a certain 
    #number of characters
    line = '-' * tickLength

    #if there is a tick label given
    if tickLabel:
        #concat the line with the label
        line += (" " + str(tickLabel))

    #print the line
    print(line)

#recursively draw the interval based upon
#a central tick length
def drawInterval(centralLength):
    #if the length reaches 0, stop
    if centralLength>0:
        #this line draws only the top part
        drawInterval(centralLength-1)

        #as the call stack is popped, this function
        #will be called to draw a line
        drawLine(centralLength)

        #draw the bottom part of the ruler
        drawInterval(centralLength-1)


#draw a ruler based on a given length and some
#major length
def drawRuler(unit, majorLength):
    #draw the first line of the ruler with unit = 0
    drawLine(majorLength, '0')

    for i in range(1, unit +1):
        drawInterval(majorLength-1)
        drawLine(majorLength, str(i))

drawRuler(3, 4)

'''
    output
    ---- 0
    -
    --
    -
    ---
    -
    --
    -
    ---- 1
    -
    --
    -
    ---
    -
    --
    -
    ---- 2
    -
    --
    -
    ---
    -
    --
    -
    ---- 3
'''

    