d={29:"Akash",45:"bhoomi",78:"soumya",19:"Anshika"}
roll_no=int(input("enter you roll number:"))
name=d.get(roll_no,"Student")
print(f"Congratulation {name}!")
roll=int(input("enter your roll number:"))
name=d.get(roll,"Student")
print(f"Congratulation {name}!")
