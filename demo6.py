import os;
import sys;
import psutil;
import time;
import schedule;

def ProcessDisplay(path="DD"):
    
    if not os.path.exists(path):
        os.mkdir(path);
    
    filename = os.path.join(path,"Marvellous%s.txt"%time.ctime());

    line = "-"*40;
    fobj = open(filename,'w');


    fobj.write(line+"\n");
    fobj.write("Marvellous Process Logger at : %s\n"%time.ctime());
    fobj.write(line+"\n");
    
    for pobj in psutil.process_iter():
        #print(pobj);
        fobj.write(str(pobj));

    fobj.close();

def main():
    schedule.every(1).minute.do(ProcessDisplay)

    while True:
        schedule.run_pending();
        time.sleep(1);

if __name__ == "__main__":
    main();



