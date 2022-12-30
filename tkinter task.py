from tkinter import*
from tkinter.ttk import*
import tkinter as tk
from tkinter import ttk


# create the parent window of the tab
root = tk.Tk() 
root.title("Prototype Application")
root.geometry("950x950")

# creating the menu bar 
menubar = Menu(root)

# Menu bar for File
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = file)
file.add_command(label = "New File", command = None)
file.add_command(label = "Open", command = None)
file.add_separator()
file.add_command (label = "Exit", command = root.destroy)

# Menu bar for Edit
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = edit)
edit.add_command (label = "Select All", command = None)
edit.add_command (label = "Copy", command = None)
edit.add_command (label = "Paste", command = None)

# Menu bar for View 
view = Menu(menubar, tearoff = 0)
menubar.add_cascade (label = "View", menu = view)
view.add_command(label = "New view", command = None)

# creating a scrollbar 
scroll_bar = Scrollbar(root)
scroll_bar.pack(side = RIGHT, fill = Y)

# creating four tabs to align to the key requirements
tabControl = ttk.Notebook(root)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)

tabControl.add(tab1, text = "Data Cleansing")
tabControl.add(tab2, text = "Data Storage")
tabControl.add(tab3, text = "Data Visualization")
tabControl.add(tab4, text = "Customization")
tabControl.pack(expand = 1, fill = "both" )

# ________ 1st requirement to load and clean the initial data set ____________________________________

# Create functionality to load data  
ttk.Label(tab1, text = "Loading", font = "bold").grid(column = 0, row = 0, padx = 30, pady = 30)
data_source = Label(tab1, text = "Data Source").place(x = 60, y = 80)

def show():
    label.config(text = clicked.get())

# dropdown menu options
options = [
    "Select data source",
    "File - Computer / Cloud", 
    "Database",  
    "API"
    ]
clicked = StringVar()
clicked.set("Select data source") # initial menu text
drop = OptionMenu(tab1, clicked, *options)
drop.place(x = 180, y = 80)


file_name = Label(tab1, text = "File Name").place(x = 60, y = 120)
file_name_input = Entry(tab1, width = 60).place (x = 180, y = 120)
upload_button = tk.Button(tab1, text = "Upload", bg='#7e9fcc').place (x = 500, y = 200)


# Create functionality to clean data  
ttk.Label(tab1, text = "Cleaning", font = "bold").grid(column = 0, row = 700, padx = 30, pady = 160)

# Creating the groupbox for cleaning data - Check if data contains header 
labelframe1 = LabelFrame(tab1, text = "Data contains headers")
labelframe1.place(height= 50, width = 600, x = 60, y = 270)
option = StringVar()
radiobutton1 = Radiobutton(tab1, text = "Yes", value = "yes", var = option).place(x = 80, y = 290)
radiobutton1 = Radiobutton(tab1, text = "No", value = "no", var = option).place(x = 180, y = 290)


# Creating the groupbox for cleaning data - Select what fields to cleanse
labelframe2 = LabelFrame(tab1, text = "Select fields to cleanse")
labelframe2.place(height= 100, width = 600, x = 60, y = 350)
checkbutton1 = Checkbutton(tab1, text = "Field 1").place(x = 80, y = 370)
checkbutton2 = Checkbutton(tab1, text = "Field 2").place(x = 80, y = 390)
checkbutton3 = Checkbutton(tab1, text = "Field 3").place(x = 80, y = 410)

# Creating the groupbox for cleaning data - Replacing nulls 
labelframe3 = LabelFrame(tab1, text = "Replace Nulls")
labelframe3.place(height= 90, width = 600, x = 60, y = 480)
checkbutton4 = Checkbutton(tab1, text = "Replace with Blanks (String fields)").place(x = 80, y = 500)
checkbutton5 = Checkbutton(tab1, text = "Replace with 0 (Numeric fields)").place(x = 80, y = 520)



# Creating the groupbox for cleaning data - Removing unwanted characters e.g. trailing whitespaces etc. 
labelframe4 = LabelFrame(tab1, text = "Remove Unwanted Characters")
labelframe4.place(height= 170, width = 600, x = 60, y = 590)
checkbutton6 = Checkbutton(tab1, text = "Leading and Trailing whitespace").place(x = 80, y = 615)
checkbutton7 = Checkbutton(tab1, text = "Tabs, Line breaks and duplicate whitespace").place(x = 80, y = 635)
checkbutton8 = Checkbutton(tab1, text = "All whitespace").place(x = 80, y = 655)
checkbutton9 = Checkbutton(tab1, text = "Letters").place(x = 80, y = 675)
checkbutton10 = Checkbutton(tab1, text = "Numbers").place(x = 80, y = 695)
checkbutton11 = Checkbutton(tab1, text = "Punctuation").place(x = 80, y = 715)

save_button = Button(tab1, text = "Save").place (x = 600, y = 850)

# create confirmation when cancel is selected
def warning():
    result = messagebox.askquestion("Confirmation needed", "Are you sure?")
    if result == "yes":
        root.destroy()
    
cancel_button = tk.Button(tab1, text = "Cancel", bg='#fa3137', command = warning).place(x = 700, y = 850)

#----------------------------------------------------------------------------------------------------------------------------------------------

# ________ 2nd requirement to load and save the prepared data set ____________________________________

# Create functionality to load data  
ttk.Label(tab2, text = "Loading", font = "bold").grid(column = 0, row = 0, padx = 30, pady = 30)
file_name = Label(tab2, text = "File Name").place(x = 60, y = 80)
file_name_input = Entry(tab2, width = 60).place (x = 180, y = 80)

# Create functionality to save the data
ttk.Label(tab2, text = "Output Details", font = "bold").grid(column = 0, row = 10, padx = 30, pady = 95)

# Create label for output location 
output_location = Label(tab2, text = "Output Location").place(x = 60, y = 230)

# Create menu listbox with output location 
output_location_listbox = Listbox(tab2, exportselection = False)
output_location_listbox.place(x= 180, y = 230, width = 400, height = 70)
output_location_listbox.insert(END, "File - Computer / Cloud")
output_location_listbox.insert(END, "Database")
output_location_listbox.insert(END, "Saved Connections")


# Create label for Save as Name
save_as_name = Label(tab2, text = "Save as Name").place(x = 60, y = 350)
save_as_name_input = Entry(tab2, width = 60).place (x = 180, y = 350, width = 400)

# Create label for Save as Type
save_as_type = Label(tab2, text = "Save as Type").place(x = 60, y = 420)

# Create menu listbox with options on storage format 
save_as_type_listbox = Listbox(tab2, exportselection = False)
save_as_type_listbox.place(x= 180, y = 420, width = 400, height = 70)
save_as_type_listbox.insert(END, "XML (.xml)")
save_as_type_listbox.insert(END, "JSON (.json)")
save_as_type_listbox.insert(END, "Entity Relation Structure")

# Create label for output options
output_options = Label(tab2, text = "Output Options").place(x = 60, y = 530)

# Create menu listbox with options on how newly stored file should behave

output_options_listbox = Listbox(tab2, exportselection = False)
output_options_listbox.place(x= 180, y = 530, width = 400, height = 70)
output_options_listbox.insert(END, "Overwrite sheet")
output_options_listbox.insert(END, "Create New Sheet")
output_options_listbox.insert(END, "Append to Existing sheet")

# Save and cancel button
save_button = Button(tab2, text = "Save").place (x = 600, y = 850)

# create confirmation when cancel is selected
def warning2():
    result = messagebox.askquestion("Confirmation needed", "Are you sure?")
    if result == "yes":
        root.destroy()

cancel_button = tk.Button(tab2, text = "Cancel", bg='#fa3137', command = warning2).place(x = 700, y = 850)


#----------------------------------------------------------------------------------------------------------------------------------------------

# ________ 3rd requirement to generate output and visualizations ___________________________

# Tab for file name
ttk.Label(tab3, text = "File Details", font = "bold").grid(column = 0, row = 0, padx = 10, pady = 30)

file_name = Label(tab3, text = "File Name").place(x = 60, y = 80)
file_name_input = Entry(tab3, width = 60).place (x = 180, y = 80)

# Create Canvas for visualisation 
canv = Canvas(tab3, height = 1000, width = 1000 )
canv.place(x = 460, y = 120)
canv.create_rectangle(74, 400, 400, 72, outline = "blue", fill = "white")

# Output and Visualization section
ttk.Label(tab3, text = "Visualization", font = "bold").grid(column = 0, row = 10, padx = 30, pady = 60)

# Group box for display output 

labelframe2 = LabelFrame(tab3, text = "Display Output")
labelframe2.place(height= 100, width = 400, x = 60, y = 180)
group_by = Label(tab3, text = "Group By").place(x = 80, y = 210)
pivot = Label(tab3, text = "Create Pivot Table").place(x = 80, y = 240)

option2 = StringVar()
radiobutton2 = Radiobutton(tab3, text = "Rows", value = "rows", var = option2).place(x = 200, y = 210)
radiobutton3 = Radiobutton(tab3, text = "Columns", value = "columns", var = option2).place(x = 270, y = 210)
option3 = StringVar()
radiobutton4 = Radiobutton(tab3, text = "Yes", value = "yes", var = option).place(x = 200, y = 240)
radiobutton5 = Radiobutton(tab3, text = "No", value = "no", var = option).place(x = 270, y = 240)


# Group box for Display visualization 
labelframe3 = LabelFrame(tab3, text = "Display Visualization")
labelframe3.place(height= 300, width = 400, x = 60, y = 320)
option3 = StringVar()

radiobutton6 = Radiobutton(tab3, text = "Pie Chart", value = "pie chart", var = option3).place(x = 80, y = 350)
radiobutton7 = Radiobutton(tab3, text = "Line Chart", value = "line chart", var = option3).place(x = 80, y = 390)
radiobutton8 = Radiobutton(tab3, text = "Bar Chart", value = "bar chart", var = option3).place(x = 80, y = 430)
radiobutton9 = Radiobutton(tab3, text = "Histogram", value = "histogram", var = option3).place(x = 80, y = 470)
radiobutton10 = Radiobutton(tab3, text = "Scatter chart", value = "scatter chart", var = option3).place(x = 80, y = 510)
radiobutton11 = Radiobutton(tab3, text = "Column", value = "column", var = option3).place(x = 80, y = 550)


# Save and cancel button
save_button = Button(tab3, text = "Save").place (x = 600, y = 850)

def warning3():
    result = messagebox.askquestion("Confirmation needed", "Are you sure?")
    if result == "yes":
        root.destroy()

cancel_button = tk.Button(tab3, text = "Cancel", bg='#fa3137', command = warning3).place(x = 700, y = 850)


#----------------------------------------------------------------------------------------------------------------------------------------------

# ________ 4th requirement to generate output and visualizations ___________________________

# Tab for file name
ttk.Label(tab4, text = "File Details", font = "bold").grid(column = 0, row = 0, padx = 10, pady = 30)

file_name = Label(tab4, text = "File Name").place(x = 60, y = 80)
file_name_input = Entry(tab4, width = 60).place (x = 180, y = 80)

# Create Canvas for visualisation 
canv = Canvas(tab4, height = 1000, width = 1000 )
canv.place(x = 460, y = 120)
canv.create_rectangle(74, 400, 400, 72, outline = "blue", fill = "white")

# Output and Visualization section
ttk.Label(tab4, text = "Visualization", font = "bold").grid(column = 0, row = 10, padx = 30, pady = 60)

# Group box for display output 

labelframe3 = LabelFrame(tab4, text = "Display Output")
labelframe3.place(height= 100, width = 400, x = 60, y = 180)

# Radiobutton for Group by 
group_by = Label(tab4, text = "Group By").place(x = 80, y = 210)
option4 = StringVar()
radiobutton12 = Radiobutton(tab4, text = "Rows", value = "rows", var = option4).place(x = 200, y = 210)
radiobutton13 = Radiobutton(tab4, text = "Columns", value = "columns", var = option4).place(x = 270, y = 210)

# Radiobutton for Create pivot table 
pivot = Label(tab4, text = "Create Pivot Table").place(x = 80, y = 240)
option5 = StringVar()
radiobutton14 = Radiobutton(tab4, text = "Yes", value = "yes", var = option5).place(x = 200, y = 240)
radiobutton15 = Radiobutton(tab4, text = "No", value = "no", var = option5).place(x = 270, y = 240)


# Group box for Validation 
labelframe5 = LabelFrame(tab4, text = "Validation")
labelframe5.place(height= 300, width = 400, x = 60, y = 320)

# Specified values 
specified_values = Label(tab4, text = "Specified Values ").place(x = 80, y = 350)

# List box for specified values 
output_location_listbox = Listbox(tab4, exportselection = False)
output_location_listbox.place(x= 200, y = 350, width = 245, height = 65)
output_location_listbox.insert(END, "Any value")
output_location_listbox.insert(END, "Decimals")
output_location_listbox.insert(END, "Whole Numbers")

# User to enter start range of values for validation 
start_range = Label(tab4, text = "Start Range ").place(x = 80, y = 440) 
start_range_input = Entry(tab4, width = 40).place (x = 200, y = 440)

# User to enter end range of values for validation
end_range = Label(tab4, text = "End Range ").place(x = 80, y = 490)
end_range_input = Entry(tab4, width = 40).place (x = 200, y = 490)

# User to select fields on which to display visualization
fields = Label(tab4, text = "Fields ").place(x = 80, y = 550)
yscrollbar = Scrollbar(tab4)
field_listbox = Listbox(tab4, selectmode = "multiple", yscrollcommand = yscrollbar.set)
field_listbox.place(x= 200, y = 550, width = 245, height = 50)
field_listbox.insert(END, "Field 1")
field_listbox.insert(END, "Field 2")
field_listbox.insert(END, "Field 3")
yscrollbar.config(command = field_listbox.yview)


# Group box for Display visualization 
labelframe4 = LabelFrame(tab4, text = "Visualization Type")
labelframe4.place(height= 150, width = 400, x = 60, y = 650)
option5 = StringVar()

radiobutton6 = Radiobutton(tab4, text = "Pie Chart", value = "pie chart", var = option5).place(x = 80, y = 690)
radiobutton7 = Radiobutton(tab4, text = "Line Chart", value = "line chart", var = option5).place(x = 80, y = 720 )
radiobutton8 = Radiobutton(tab4, text = "Bar Chart", value = "bar chart", var = option5).place(x = 80, y = 750)
radiobutton9 = Radiobutton(tab4, text = "Histogram", value = "histogram", var = option5).place(x = 250, y = 690)
radiobutton10 = Radiobutton(tab4, text = "Scatter chart", value = "scatter chart", var = option5).place(x = 250, y = 720)
radiobutton11 = Radiobutton(tab4, text = "Column", value = "column", var = option5).place(x = 250, y = 750)

# Save and cancel button
save_button = Button(tab4, text = "Save").place (x = 600, y = 850)

def warning4():
    result = messagebox.askquestion("Confirmation needed", "Are you sure?")
    if result == "yes":
        root.destroy()

cancel_button = tk.Button(tab4, text = "Cancel", bg='#fa3137', command = warning4).place(x = 700, y = 850)



root.config(menu = menubar)
root.mainloop()
