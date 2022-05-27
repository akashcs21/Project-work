def shut_down(s):
    s.lower()
    if s=="yes":
        print("Shuting_down started")
    elif s=="no":
        print("Shutdown aborted")
    else:
        print("Sorry input unmatched try again")
ordr=input("enter the instruction: ")
shut_down(ordr)            

