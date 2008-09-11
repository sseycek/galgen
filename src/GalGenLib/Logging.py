import sys

def logError(msg):
    sys.stdout.write('ERROR: %s\n' % msg)

def logInfo(msg):
    sys.stdout.write('INFO: %s\n' % msg)

def logDebug(msg):
    sys.stdout.write('DEBUG: %s\n' % msg)

def logWarn(msg):
    sys.stdout.write('WARNING: %s\n' % msg)