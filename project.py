from tkinter import *
root = Tk()
root.geometry("1000x600")

def getvals():
    print("Accepted")



Label(root,text="Registration Form using python",font="ar 15 bold").grid(row=0,column=3)

firstname = Label(root, text="First Name")
phone = Label(root, text="Contact Phone")
gender = Label(root, text="Gender")
emailid = Label(root, text="Email id")
paymentmood = Label(root, text="Payment Mood")

firstname.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emailid.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

firstnamevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emailidvalue = StringVar
paymentmoodvalue = StringVar
checkvalue=IntVar

firstnameentry=Entry(root, textvariable=firstnamevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emailidentry=Entry(root, textvariable=emailidvalue)
paymentmoodentry=Entry(root, textvariable=paymentmoodvalue)

firstnameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emailidentry.grid(row=4,column=3)
paymentmoodentry.grid(row=5,column=3)

checkbtn = Checkbutton(text="remeber me?", variable=checkvalue)
checkbtn.grid(row=6, column=3)

Button(text="Submit", command=getvals).grid(row=7,column=3)

root.mainloop()



import shelve
with shelve.open("data") as db:
    data: dict =[firstnameentry]
db.close()
print(data)



