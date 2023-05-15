import threading, zipfile


class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile

    def run(self):
        f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print("Finished background zip of:", self.infile)


# background = AsyncZip("./tutorial/data/sam", "./tutorial/data/sam.zip")
# background.start()
# print("The main program continues to run in foreground.")

# background.join()  # Wait for the background task to finish
# print("Main program waited until background was done.")

# 11.5 로깅
import logging

logging.debug("Debugging information")
logging.info("Informational message")
logging.error("An error has happened!")
