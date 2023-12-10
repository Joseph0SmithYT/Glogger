import time
import datetime

bLogFile = False
bTimeStamp = True


def getLocalTime():
    return datetime.datetime.now().strftime("%H:%M:%S")


def setup(logfile_option=False, timestamp_option=False):
    global bLogFile, bTimeStamp
    bLogFile = logfile_option
    bTimeStamp = timestamp_option


def printmsg(logtype, reason):
    if bTimeStamp is True:
        local_time = getLocalTime()
        print(f"{local_time}: {logtype.upper()} | {reason}")
    else:
        print(f"{logtype.upper()} | {reason}")


def measuretime(func):
    """
    Put '@measuretime' before a function to use this function.
    You can also put measuretime([functionname])
    """
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        elapsedTime = round((endTime - startTime), 3)

        if bTimeStamp is True:
            local_time = getLocalTime()
            print(f"{local_time}: Elapsed time: {elapsedTime}")
        else:
            print(f"Elapsed time: {elapsedTime}s")
    return wrapper


@measuretime
def error(reason):
    printmsg("ERROR", reason)


def warning(reason):
    printmsg("WARNING", reason)


def info(reason):
    printmsg("INFO", reason)


def custom(reason, custommsg):
    printmsg(custommsg, reason)


if __name__ == "__main__":
    setup(logfile_option=True, timestamp_option=True)

    error("Error!")
    warning("Warning!")
    info("Info!")
    custom("Custom!", "custom")

    measuretime_custom = measuretime(custom)
    measuretime_custom("Custom", "MEASURED")
