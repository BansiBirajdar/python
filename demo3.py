import os;
import sys;
import psutil;

def ProcessDisplay(path):
    
    if not os.path.exists(path):
        os.mkdir(path);
    
    filename = os.path.join(path,"Marvellous.txt");
    
    fobj = open(filename,'w');
    print("Running processess");
    
    for pobj in psutil.process_iter():
        print(pobj);
        fobj.write(str(pobj));

    fobj.close();

def main():
    ProcessDisplay(sys.argv[1]);

if __name__ == "__main__":
    main();
