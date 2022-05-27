def comput_pay(time,rate):
    if time<40:
        x=time*rate
        print(f"the pay is:{x}")
    else:
        y=40*rate+(time-40)*1.5*rate
        print(f"the pay is:{y}")
time=int(input("enter time in hour: "))
rate=int(input("enter rate: "))
comput_pay(time,rate)
