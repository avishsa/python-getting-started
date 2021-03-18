def validIsNumber(myVar):
    floatNum = 0
    try:
        floatNum = float(myVar)
        return True
    except:
        return False
def validLatAndLon(lat,lon):
    if(lat==None or lon==None):
        return {'msg':'invalid parameters key, you should send lat and lon'}
    if (not validIsNumber(lat) or not validIsNumber(lon)):
        return {'msg':'invalid parameters values'}
    return None