import os;
import sys;
import psutil;

def ProcessDisplay():
    print("Running processess");
    
    for pobj in psutil.process_iter():
        print(pobj);

def main():
    ProcessDisplay();

if __name__ == "__main__":
    main();
