import logging

def getLogLevel(inputLogLevel):
    
    logLevel = logging.ERROR
    
    if not inputLogLevel == None:
        numeric_level = getattr(logging, inputLogLevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % inputLogLevel)
        logLevel = numeric_level
        
    return logLevel
