import logging

# Setup code for logging in Python. This code produces 0, which is not intended.

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.debug("Return value is %s" % (total))
    return total


print(factorial(5))

logging.debug("End of program")

# A small change is made in the code to fix the above problem, which is
# range needs to start at 1, rather than 0.

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Start of program")


def factorial(n):
    logging.debug("Start of factorial(%s)" % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug("i is %s, total is %s" % (i, total))

    logging.debug("Return value is %s" % (total))
    return total


print(factorial(5))

logging.debug("End of program")

# logging.debug is used to prevent having to use print() for logs.
# Once finished, add logging.disable(logging.CRITICAL) at the top to prevent
# having to remove logging line by line.

# logging.debug(), logging.info(), logging.warning(), logging.error(),
# logging.critical() are all types of log. Critical is the highest level
# and when logging.disable(logging.CRITICAL) is used, it stops all logs
# from critical on down. Debug is the lowest level. Warning means something
# could go wrong and error means something has gone wrong.
# Critical means something that has gone wrong stopped the program.
# A text file of the log can be created by passing `filename=x.txt",
# to the beginning of the logging.basicConfig function.
