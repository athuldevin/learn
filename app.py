import aiml
import sys

kern = aiml.Kernel()
kern._addSession("athuldevin")
sessionID="athuldevin"

brainLoaded = False
forceReload = False
while not brainLoaded:
    if forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
        # Use the Kernel's bootstrap() method to initialize the Kernel. The
        # optional learnFiles argument is a file (or list of files) to load.
        # The optional commands argument is a command (or list of commands)
        # to run after the files are loaded.
        kern.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
        brainLoaded = True
        # Now that we've loaded the brain, save it to speed things up for
        # next time.
        kern.saveBrain("bot.brn")
    else:
        # Attempt to load the brain file.  If it fails, fall back on the Reload
        # method.
        try:
            # The optional branFile argument specifies a brain file to load.
            kern.bootstrap(brainFile = "bot.brn")
            brainLoaded = True
        except:
            forceReload = True

kern.restoreSessionData("bot.dat",sessionID)

while True:
    input =raw_input("user>>>")
    output =kern.respond(input,sessionID)
    print ("bot>>>%s" %output)
    kern.saveSessionData("bot.dat",sessionID)
