def makePoint(x,y):
    return (x,y)

def xCoord(x):
    return x[0]

def yCoord(y):
    return y[1]

def makeSegment(start,end):
    return (start,end)

def segStart(start):
    return start[0]

def segEnd(end):
    return end[1]

def zoomPoint(pt,factor):
    return makePoint(factor*xCoord(pt),factor*yCoord(pt))

def scaleSegment(seg,factor):
    return makeSegment(zoomPoint(seg,factor),zoomPoint(seg,factor))

