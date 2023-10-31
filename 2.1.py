We_wish_you = "We wish you a Merry Christmas"
Good_tiding = "Good tidings we bring to you and your kin"
Now__bring = "Now bring us some figgy pudding"
We_wont = "Now bring us some figgy pudding"

def We():


    for something in [1, 2]:
        print(We_wish_you)
        if something == 2:
            print(f"{We_wish_you} and a Happy New Year")



def Good():
    print (f"\n{Good_tiding}")
    print(f"{We_wish_you} and a Happy New Year\n")

def Now():

    for Now_b in {1, 2}:
        print (f"{Now__bring}")
        if Now_b == 2:
            print (f"{Now__bring}, now bring some out here\n")
    
def Wont():
    for wont in [1, 2]:
        print (f"{We_wont}")
        if wont == 2:
            print (f"{We_wont}, so bring som out here\n")


We()
Good()
Now()
Good()
Wont()
Good()
We()
