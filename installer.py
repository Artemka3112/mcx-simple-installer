import settings, os, urllib.request, logger,subprocess

class JavaInstaller:
    def __init__(self,bittnes,custompath,path):
        logger.addLogData("Initialization Java Installer")
        if bittnes == "64":
            self.url = settings.java_64_url
            self.file_name = settings.java_64_file_name
        elif bittnes == "86":
            self.url = settings.java_32_url
            self.file_name = settings.java_32_file_name
        self.arg = settings.java_opt.split(" ")
        if custompath:
            self.arg.append("INSTALLDIR="+path+"")

    def install(self):
        logger.addLogData('Starting installation Java...')
        if settings.dev:
            logger.addLogDataDebug(self.arg)
        logger.addLogData('Download java installer...')
        if not settings.dev:
            urllib.request.urlretrieve(self.url, self.file_name)
            str = ""
            f = open('jre-install.properties', 'w')
            for item in self.arg:
                str += item +"\n"
            f.write(str)  # python will convert \n to os.linesep
            f.close()
        logger.addLogData('Install Java...')
        if not settings.dev:
            subprocess.run(self.file_name + " INSTALLCFG=\""+os.path.abspath(os.getcwd())+"\\jre-install.properties\"", shell=True)
            #os.system(self.arg)
        logger.addLogData('Deleting Java installer...')
        if not settings.dev:
            os.remove(self.file_name)
            os.remove("jre-install.properties")
        logger.addLogDataSuccess('Installation Java end successfully!')

class LauncherInstaller:
    def __init__(self):
        self.desktoppath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    def install(self):
        logger.addLogData('Starting installation Launcher...')
        logger.addLogData('Download and unpack '+settings.launcher_file_name+' on desktop')
        if not settings.dev:
            urllib.request.urlretrieve(settings.launcher_url, self.desktoppath + "\\" + settings.launcher_file_name)
        logger.addLogDataSuccess('Installation Launcher end successfully!')