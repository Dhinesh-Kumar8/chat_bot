import tkinter
from tkinter import ttk
from tkinter import messagebox
def enter_data():
    accepted = accept_var.get()
    
    if accepted == "Accepted":
        #user info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_spinbox.get()
            
            #course info
            registrtion_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemster = numsemster_spinbox.get()
            
            print(f"first name: {firstname}, Lastname: {lastname}")
            print(f"Title: {title}, age: {age},Nationality: {nationality}")
            print(f"course: {numcourses}, semster: {numsemster}")
            print(f"Registration status {registrtion_status}")
            print("------------------------------------------")