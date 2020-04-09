## -*- Encoding: UTF-8 -*-  
import testimport

maliste=[]

print("dans main ",__name__)

def toto():
    print("Je suis dans main")

def tata():
    return(testimport.toto())

if __name__ == '__main__':
    print(tata())
    print("Terminé") 