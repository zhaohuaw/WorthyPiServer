import subprocess

class Radio:
    def play(self):
        self.process = subprocess.Popen(['mplayer','http://bbcwssc.ic.llnwd.net/stream/bbcwssc_mp1_ws-einws'],stdin=subprocess.PIPE)
    def stop(self):
            self.process.communicate(input=b'q')