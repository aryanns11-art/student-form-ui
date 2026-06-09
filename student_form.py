import customtkinter as ctk

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue")

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    year = year_var.get()
    course = course_var.get()
    dob = f"{day_var.get()}-{month_var.get()}-{year_dob_var.get()}"

    if (name == "" or age == "" or gender == "" or course == "" or year == "" or
    day_var.get() == "Day" or month_var.get() == "Month" or year_dob_var.get() == "Year"):
        result_label.configure(text="⚠ Please fill all fields!", text_color="red")
    else:
        result = f"Name: {name} | Age: {age} | Gender: {gender} | DOB : {dob} | Course: {course} | Year: {year}"
        result_label.configure(text=result, text_color="green")

#---------------------------------------Window------------------------------------------------------------------
root = ctk.CTk()
root.title("Student Form")
root.geometry("500x720")
#root.resizable(False,False)

#----------------------------------------Title----------------------------------------------------------

title = ctk.CTkLabel(root, text="Student Information Form", font=("Arial", 18))
title.pack(pady=10)

# Inputs
entry_frame = ctk.CTkFrame(root,height=100)
entry_frame.pack(anchor="n",fill="x",pady=10,padx=20)

entry_name = ctk.CTkEntry(entry_frame, placeholder_text="Enter Name")
entry_name.pack(fill="x",pady=5)

entry_age = ctk.CTkEntry(entry_frame, placeholder_text="Enter Age")
entry_age.pack(fill="x",pady=5)

#-------------------------------------------Gender------------------------------------------------

gender_frame = ctk.CTkFrame(root,height=50,width=150)
gender_frame.pack(pady=10,padx=20,fill="x")
gender_frame.pack_propagate(False)

gender_label = ctk.CTkLabel(gender_frame,text="Select Gender :")
gender_label.pack(side="left",padx=10,pady=5)

gender_var = ctk.StringVar(value="")
ctk.CTkRadioButton(gender_frame, text="Male", variable=gender_var, value="Male").pack(side="left",padx=10)
ctk.CTkRadioButton(gender_frame, text="Female", variable=gender_var, value="Female").pack(side="left",padx=10)

#-------------------------------Course---------------------------------------------

course_frame = ctk.CTkFrame(root,height=80,corner_radius=6,border_width=2)
course_frame.pack(padx=20,pady=10,fill="x")
course_frame.pack_propagate(False)

year_var = ctk.StringVar(value="Select Year")
entry_year = ctk.CTkOptionMenu(course_frame , values=["1st","2nd","3rd","4th"],variable = year_var)
entry_year.pack(pady=10,padx=20,side="left")

course_var = ctk.StringVar(value="Select Course")
entry_course = ctk.CTkOptionMenu(course_frame, values=["CM","ME","ENTC","IT","AI/ML","EEE"],variable=course_var)
entry_course.pack(side="left",pady=5,padx=20)

#-------------------------------------------DOB------------------------------------------------

dob_frame = ctk.CTkFrame(root, height=80)
dob_frame.pack(fill="x", pady=10, padx=20)

dob_label = ctk.CTkLabel(dob_frame, text="Date of Birth:")
dob_label.pack(side="left", padx=10)

day_var = ctk.StringVar(value="Day")
month_var = ctk.StringVar(value="Month")
year_dob_var = ctk.StringVar(value="Year")

day_menu = ctk.CTkOptionMenu(dob_frame, values=[str(i) for i in range(1, 32)], variable=day_var)
day_menu.pack(side="left", padx=5)

month_menu = ctk.CTkOptionMenu(dob_frame,values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],variable=month_var)
month_menu.pack(side="left", padx=5)

year_frame = ctk.CTkFrame(dob_frame, fg_color="transparent")
year_frame.pack(fill="x")

year_menu = ctk.CTkOptionMenu(year_frame,values=[str(i) for i in range(1990, 2026)],variable=year_dob_var)   
year_menu.pack(pady=5, anchor="w", padx=10)

#--------------------------------------Submit--------------------------------------
submit_btn = ctk.CTkButton(root, text="Submit", command=submit_form)
submit_btn.pack(pady=15)

#-------------------------------------------Result-----------------------------------------
result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)


root.mainloop()