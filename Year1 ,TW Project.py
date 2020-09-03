import mysql.connector
from tkinter import *
import re
global role
from tkinter import filedialog




mydb= mysql.connector.connect(
    host="51.89.139.9",
    user="root",
    password="Gernot-Is-Cool420",
    db="ParkingDB"
    
    
)
mycursor = mydb.cursor()


print(mydb)

def login():
    home=Tk()
    home.title("Log in")
    home.geometry('300x75')
    
    Label(home, text="Username: ").grid(row=1, column=0)
    e1=Entry(home)
    e1.grid(row=1, column=1)
    Label(home, text="Password: ").grid(row=2)
    e2=Entry(home,show="*")
    e2.grid(row=2, column=1)
    
    

    def callback():
    
        username=e1.get()
        password=e2.get()
        
        mycursor.execute("select username from CREDENTIALS where username= '%s' and password= '%s' "%(username,password))
        usern=mycursor.fetchone()
        mycursor.execute("select password from CREDENTIALS where username= '%s' and password= '%s' "%(username,password))
        passw=mycursor.fetchone()
        mycursor.execute("select role from CREDENTIALS where username= '%s' and password= '%s' "%(username,password))
        role=mycursor.fetchone()
        mycursor.execute("select fk_employee_num from CREDENTIALS where username= '%s' and password= '%s' "%(username,password))
        employee_num=mycursor.fetchone()
        employee_num=employee_num[0]
        try:
            role=role[0]
        except TypeError:
            Label(home, text="Wrong username or password").grid(row=4, column=0)
   
       
        
        def employee():
            
            def save_filepath():
                reports_window.filename = filedialog.asksaveasfilename(initialdir="C:\Documents", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
                filepath = reports_window.filename + '.csv'
                return filepath


            def total_bookings_by_employee(mysqldb, employee_id, start_date, end_date, filepath=None):  #1
                query = "select EMPLOYEE.employee_num, EMPLOYEE.first_name, EMPLOYEE.surname, BOOKINGS.fk_parking_slot, BOOKINGS.fk_vehicle_registration, BOOKINGS.date, BOOKINGS.start_time, BOOKINGS.end_time, BADGE_INFO.fk_badge_colour "+"from EMPLOYEE, BOOKINGS, BADGE_INFO, VEHICLE, BADGE_COLOUR where EMPLOYEE.employee_num = BOOKINGS.fk_employee_num and EMPLOYEE.employee_num = VEHICLE.fk_employee_num and BOOKINGS.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_badge_colour = BADGE_COLOUR.badge_colour and EMPLOYEE.employee_num = {} and BOOKINGS.date >= \'{}\' and BOOKINGS.date <= \'{}\';".format(employee_id, start_date, end_date)

                cursor = mysqldb.cursor()

                cursor.execute(query)

                file_object = open(filepath, "w")

                file_object.write("Employee #,First Name,Surname,Parking Slot #,Registration Plate,Date,Start Time,End Time,"
                                  "Badge Colour")

                for x in cursor:
                    file_object.write("\n{},{},{},{},{},{},{},{},{}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

                file_object.close()


            def all_bookings(mysqldb, filepath=None): #4
                query = "select EMPLOYEE.employee_num, EMPLOYEE.first_name, EMPLOYEE.surname, BOOKINGS.fk_parking_slot, BOOKINGS.fk_vehicle_registration, BOOKINGS.date, BOOKINGS.start_time, BOOKINGS.end_time, BADGE_INFO.fk_badge_colour " + "from EMPLOYEE, BOOKINGS, BADGE_INFO, VEHICLE, BADGE_COLOUR where EMPLOYEE.employee_num = BOOKINGS.fk_employee_num and EMPLOYEE.employee_num = VEHICLE.fk_employee_num and BOOKINGS.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_badge_colour = BADGE_COLOUR.badge_colour;"

                cursor = mysqldb.cursor()

                cursor.execute(query)

                file_object = open(filepath, "w")

                file_object.write("Employee #,First Name,Surname,Parking Slot #,Registration Plate,Date,Start Time,End Time,"
                                  "Badge Colour")

                for x in cursor:
                    file_object.write("\n{},{},{},{},{},{},{},{},{}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

                file_object.close()


            def bookings_by_colour(mysqldb, colour_group, filepath=None): #5
                query = "select EMPLOYEE.employee_num, EMPLOYEE.first_name, EMPLOYEE.surname, BOOKINGS.fk_parking_slot, BOOKINGS.fk_vehicle_registration, BOOKINGS.date, BOOKINGS.start_time, BOOKINGS.end_time, BADGE_INFO.fk_badge_colour " + "from EMPLOYEE, BOOKINGS, BADGE_INFO, VEHICLE, BADGE_COLOUR where EMPLOYEE.employee_num = BOOKINGS.fk_employee_num and EMPLOYEE.employee_num = VEHICLE.fk_employee_num and BOOKINGS.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_badge_colour = BADGE_COLOUR.badge_colour AND BADGE_INFO.fk_badge_colour = \'{}\';".format(colour_group)

                cursor = mysqldb.cursor()

                cursor.execute(query)

                file_object = open(filepath, "w")

                file_object.write("Employee #,First Name,Surname,Parking Slot #,Registration Plate,Date,Start Time,End Time,"
                                  "Badge Colour")

                for x in cursor:
                    file_object.write("\n{},{},{},{},{},{},{},{},{}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

                file_object.close()


            def bookings_by_multiple_colours(mysqldb, colour_groups, filepath=None): #6
                query = "select EMPLOYEE.employee_num, EMPLOYEE.first_name, EMPLOYEE.surname, BOOKINGS.fk_parking_slot, BOOKINGS.fk_vehicle_registration, BOOKINGS.date, BOOKINGS.start_time, BOOKINGS.end_time, BADGE_INFO.fk_badge_colour " + "from EMPLOYEE, BOOKINGS, BADGE_INFO, VEHICLE, BADGE_COLOUR where EMPLOYEE.employee_num = BOOKINGS.fk_employee_num and EMPLOYEE.employee_num = VEHICLE.fk_employee_num and BOOKINGS.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_vehicle_registration = VEHICLE.vehicle_registration and BADGE_INFO.fk_badge_colour = BADGE_COLOUR.badge_colour AND (BADGE_INFO.fk_badge_colour = \'{}\'".format(colour_groups[0])

                for i in range(1, len(colour_groups)):
                    query += " OR BADGE_INFO.fk_badge_colour = \'{}\'".format(colour_groups[i])

                query += ");"

                cursor = mysqldb.cursor()

                cursor.execute(query)

                file_object = open(filepath, "w")

                file_object.write("Employee #,First Name,Surname,Parking Slot #,Registration Plate,Date,Start Time,End Time,"
                                  "Badge Colour")

                for x in cursor:
                    file_object.write( "\n{},{},{},{},{},{},{},{},{}".format(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

                file_object.close()


            def parking_booking_click():
                employee_id = employee_id_entry.get()
                start_date = start_date_entry.get()
                end_date = end_date_entry.get()

                total_bookings_by_employee(mydb, employee_id, start_date, end_date, save_filepath())


            def single_employee_click():
                test = 2


            def multiple_employee_click():
                test = 3


            def all_bookings_click():
                all_bookings(mydb, save_filepath())


            def colour_bookings_click():
                colour_group = colour_bookings_lb.curselection()
                print(colour_group)

                colour_group = colour_bookings_lb.get(colour_group[0])
                bookings_by_colour(mydb, colour_group, save_filepath())


            def multiple_colour_bookings_click():
                colour_groups_indexes = multiple_colour_bookings_lb.curselection()
                print(colour_groups_indexes)
                colour_groups = []

                for index in colour_groups_indexes:
                    colour_groups.append(multiple_colour_bookings_lb.get(index))

                bookings_by_multiple_colours(mydb, colour_groups, save_filepath())


            def reports():
                global reports_window
                reports_window = Tk()
                reports_window.title('Reports')
                reports_window.geometry('500x700')

                employee_id_lbl = Label(reports_window, text='Employee Id')
                employee_id_lbl.grid(row=0, column=0)

                start_date_lbl = Label(reports_window, text='Start Date')
                start_date_lbl.grid(row=0, column=1)

                end_date_lbl = Label(reports_window, text='End Date')
                end_date_lbl.grid(row=0, column=2)

                global employee_id_entry
                employee_id_entry = Entry(reports_window)
                employee_id_entry.grid(row=1, column=0)

                global start_date_entry
                start_date_entry = Entry(reports_window)
                start_date_entry.grid(row=1, column=1)

                global end_date_entry
                end_date_entry = Entry(reports_window)
                end_date_entry.grid(row=1, column=2)

                parking_booking_button = Button(reports_window, text='Total Employee Bookings', command=parking_booking_click)
                parking_booking_button.grid(row=2, column=1)

                space_lbl1 = Label(reports_window, text='  ')
                space_lbl1.grid(row=3, column=1)

                single_employee_button = Button(reports_window, text='Single Employee Reporting', command=single_employee_click)
                single_employee_button.grid(row=4, column=1)
                single_employee_button.grid_forget()

                space_lbl2 = Label(reports_window, text='  ')
                space_lbl2.grid(row=5, column=1)

                multiple_employee_button = Button(reports_window, text='Multiple Employee Reporting',
                                                  command=multiple_employee_click)
                multiple_employee_button.grid(row=6, column=1)
                multiple_employee_button.grid_forget()

                space_lbl3 = Label(reports_window, text='  ')
                space_lbl3.grid(row=7, column=1)

                all_bookings_button = Button(reports_window, text='All Booking Details', command=all_bookings_click)
                all_bookings_button.grid(row=8, column=1)

                space_lbl4 = Label(reports_window, text='  ')
                space_lbl4.grid(row=9, column=1)

                global colour_bookings_lb
                colour_bookings_lb = Listbox(reports_window, selectmode=SINGLE)
                colour_bookings_lb.insert(1, 'Red')
                colour_bookings_lb.insert(2, 'Light Pink')
                colour_bookings_lb.insert(3, 'Dark Green')
                colour_bookings_lb.insert(4, 'White')
                colour_bookings_lb.insert(5, 'Grey')
                colour_bookings_lb.insert(6, 'Dark Blue')
                colour_bookings_lb.insert(7, 'Brown')
                colour_bookings_lb.insert(8, 'Purple')
                colour_bookings_lb.insert(9, 'Yellow')
                colour_bookings_lb.insert(10, 'Orange')
                colour_bookings_lb.insert(11, 'Blue')
                colour_bookings_lb.grid(row=10, column=1)

                colour_bookings_button = Button(reports_window, text='Booking Details for a Specific Colour Weeks',
                                                command=colour_bookings_click)
                colour_bookings_button.grid(row=11, column=1)

                space_lbl5 = Label(reports_window, text='  ')
                space_lbl5.grid(row=12, column=1)

                global multiple_colour_bookings_lb
                multiple_colour_bookings_lb = Listbox(reports_window, selectmode=MULTIPLE)
                multiple_colour_bookings_lb.insert(1, 'Red')
                multiple_colour_bookings_lb.insert(2, 'Light Pink')
                multiple_colour_bookings_lb.insert(3, 'Dark Green')
                multiple_colour_bookings_lb.insert(4, 'White')
                multiple_colour_bookings_lb.insert(5, 'Grey')
                multiple_colour_bookings_lb.insert(6, 'Dark Blue')
                multiple_colour_bookings_lb.insert(7, 'Brown')
                multiple_colour_bookings_lb.insert(8, 'Purple')
                multiple_colour_bookings_lb.insert(9, 'Yellow')
                multiple_colour_bookings_lb.insert(10, 'Orange')
                multiple_colour_bookings_lb.insert(11, 'Blue')
                multiple_colour_bookings_lb.grid(row=13, column=1)

                multiple_colour_bookings_button = Button(reports_window, text='Booking Details for Multiple Colour Weeks',
                                                         command=multiple_colour_bookings_click)
                multiple_colour_bookings_button.grid(row=14, column=1)

                reports_window.mainloop()




                
            
            
            def manager():
                
                mng=Tk()
                mng.title("Manager Menu")
                Label(mng, text="Enter employees num ").grid(row=1, column=0)
                e3=Entry(mng)
                e3.grid(row=1,column=1)
                def EditBook():
                    e=e3.get()
                    print(e)
                    print("hello world")
                    
                    
                btn = Button(mng, text="Check/Manage Employees bookings",command=EditBook).grid(column=0, row=2)
                btn = Button(mng, text="Run Reports",command=reports).grid(column=0, row=3)
                

                
    
            def Systemadmin():
                def update_usr():
                    global first_name_update
                    global surname_update
                    global registration_plate_update
                    global vehicle_make_update
                    global employee_number_update
                    global mobile_number_update
                    global extension_number_update
                    global postcode_travelled_update
                    global badge_update
                    global electric_car_update
                    global role_update
                    
                    e=e4.get()
                    print(e)
                    sql_script = ("SELECT EMPLOYEE.first_name, EMPLOYEE.surname, VEHICLE.vehicle_registration, VEHICLE.vehicle_make, EMPLOYEE.employee_num, EMPLOYEE.mobile_num, EMPLOYEE.extension_num, EMPLOYEE.postcode, BADGE_INFO.fk_badge_colour, VEHICLE.electric, CREDENTIALS.role FROM EMPLOYEE, VEHICLE, BADGE_INFO, CREDENTIALS, BADGE_COLOUR WHERE  VEHICLE.fk_employee_num = EMPLOYEE.employee_num AND VEHICLE.vehicle_registration = BADGE_INFO.fk_vehicle_registration AND BADGE_INFO.fk_badge_colour = BADGE_COLOUR.badge_colour AND CREDENTIALS.fk_employee_num = EMPLOYEE.employee_num AND EMPLOYEE.employee_num = {}").format(e)
        
                    print(sql_script)

                    mycursor.execute(sql_script)
                    result = mycursor.fetchone()
                    print(result)
                    
                    first_name_update = result[0]
                    surname_update = result[1]
                    registration_plate_update = result[2]
                    vehicle_make_update = result[3]
                    employee_number_update = result[4]
                    mobile_number_update = result[5]
                    extension_number_update = result[6]
                    postcode_travelled_update = result[7]
                    badge_update = result[8]
                    electric_car_update = result[9]
                    role_update = result[10]

                    global employee_number_perm
                    global registration_plate_perm

                    employee_number_perm = employee_number_update
                    registration_plate_perm = registration_plate_update

                


                        

                    mainframe = Tk()
                    mainframe.title("Edit User")
                    mainframe.geometry("500x500")

                    # new user label
                    new_user_label = Label(mainframe, text="Edit User")
                    new_user_label.grid(row=0, column=0)

                    # error label
                    error_text = StringVar()
                    error_text.set("")
                    error_label = Label(mainframe, textvariable = error_text)
                    error_label.grid(row=0, column=2)


                    def update_command():

                        # first name
                        first_name_storage = first_name_input.get()

                        # surname
                        surname_storage = surname_input.get()

                        # registration plate
                        registration_plate_storage = registration_plate_input.get()

                        # vehicle_make
                        vehicle_make_storage = vehicle_make_input.get()

                        # employee_number
                        employee_number_storage = employee_number_input.get()

                        # mobile_number
                        mobile_number_storage = mobile_number_input.get()

                        # employer_department

                        # extension_number
                        extension_number_storage = extension_number_input.get()

                        # postcode_travelled
                        postcode_travelled_storage = postcode_travelled_input.get()

                        badge_storage = badge_input.get()

                        electric_car_storage = electric_car_input.get()
                        role_storage = role_input.get()

                        mycursor.execute("SET global foreign_key_checks = 0;")
                        mycursor.execute("commit;")


                        employee_update = ("UPDATE EMPLOYEE SET first_name = '{}', surname = '{}', employee_num = {}, mobile_num = '{}', extension_num = '{}', postcode = '{}' WHERE employee_num = {};")
                        vehicle_update = ("UPDATE VEHICLE SET    vehicle_registration = '{}', vehicle_make = '{}', electric = '{}', fk_employee_num = {} WHERE fk_employee_num = {};")
                        badge_update = ("UPDATE BADGE_INFO SET    fk_vehicle_registration = '{}', fk_badge_colour = '{}' WHERE fk_vehicle_registration = '{}';")
                        credentials_update = ("UPDATE CREDENTIALS SET    fk_employee_num = '{}', role = '{}' WHERE  fk_employee_num = {};")

                        employee_update = employee_update.format(first_name_storage, surname_storage, employee_number_storage, mobile_number_storage, extension_number_storage, postcode_travelled_storage, employee_number_perm)
                        mycursor.execute(employee_update)

                        vehicle_update = vehicle_update.format(registration_plate_storage, vehicle_make_storage, electric_car_storage, employee_number_storage, employee_number_perm)
                        mycursor.execute(vehicle_update)

                        badge_update = badge_update.format(registration_plate_storage, badge_storage, registration_plate_perm)
                        mycursor.execute(badge_update)

                        credentials_update = credentials_update.format(employee_number_storage, role_storage, employee_number_perm)
                        mycursor.execute(credentials_update)

                        mycursor.execute("commit;")

                        mycursor.execute("SET global foreign_key_checks = 1;")
                        mycursor.execute("commit;")
                    first_name = Label(mainframe,text="First Name:")
                    first_name.grid(row=1, column=1)

                    first_name_input = Entry(mainframe)
                    first_name_input.grid(row=1, column=2)
                    first_name_input.insert(0, first_name_update)


                    # Surname
                    surname = Label(mainframe,text="Surname:")
                    surname.grid(row=2, column=1)

                    surname_input = Entry(mainframe)
                    surname_input.grid(row=2, column=2)
                    surname_input.insert(0, surname_update)

                    # Registration plate
                    registration_plate = Label(mainframe,text="Registration Plate:")
                    registration_plate.grid(row=3, column=1)

                    registration_plate_input = Entry(mainframe)
                    registration_plate_input.grid(row=3, column=2)
                    registration_plate_input.insert(0, registration_plate_update)

                    # Vehicle make
                    vehicle_make = Label(mainframe,text="Vehicle make:")
                    vehicle_make.grid(row=4, column=1)

                    vehicle_make_input = Entry(mainframe)
                    vehicle_make_input.grid(row=4, column=2)
                    vehicle_make_input.insert(0, vehicle_make_update)

                    # Employee number
                    employee_number = Label(mainframe,text="Employee number:")
                    employee_number.grid(row=5, column=1)

                    employee_number_input = Entry(mainframe)
                    employee_number_input.grid(row=5, column=2)
                    employee_number_input.insert(0, employee_number_update)

                    # Mobile number
                    mobile_number = Label(mainframe,text="Mobile number:")
                    mobile_number.grid(row=6, column=1)

                    mobile_number_input = Entry(mainframe)
                    mobile_number_input.grid(row=6, column=2)
                    mobile_number_input.insert(0, mobile_number_update)

                    # Extension number
                    extension_number = Label(mainframe,text="Extension number:")
                    extension_number.grid(row=8, column=1)

                    extension_number_input = Entry(mainframe)
                    extension_number_input.grid(row=8, column=2)
                    extension_number_input.insert(0, extension_number_update)

                    # Postcode travelled from
                    postcode_travelled = Label(mainframe,text="Postcode travelled from:")
                    postcode_travelled.grid(row=9, column=1)

                    postcode_travelled_input = Entry(mainframe)
                    postcode_travelled_input.grid(row=9, column=2)
                    postcode_travelled_input.insert(0, postcode_travelled_update)

                    badge = Label(mainframe,text="Badge:")
                    badge.grid(row=10, column=1)

                    badge_input = Entry(mainframe)
                    badge_input.grid(row=10, column=2)
                    badge_input.insert(0, badge_update)
                                         
                    l=Label(mainframe,text="Electric car: (0/1)").grid(row=11, column=1)

                    electric_car_input = Entry(mainframe)
                    electric_car_input.grid(row=11, column=2)
                    electric_car_input.insert(0, electric_car_update)

                    l=Label(mainframe, text="Role/Permission: (").grid(row=12, column=1)
                    l=Label(mainframe, text="Role/Permission (0 employee/1 manager/2 facility/3 admin)").grid(row=13, column=1)
                    role_input = Entry(mainframe)
                    role_input.grid(row=12, column=2)
                    role_input.insert(0, role_update)


                    # Submit button
                    submit_button = Button(mainframe, text="Submit", command=update_command)
                    submit_button.grid(row=14, column=2)

                    mainframe.mainloop()
                def add_manager():
                    t=e6.get()
                    r=e7.get()
                    sql = """INSERT INTO EMPLOYER VALUES ('{}',{})""".format(t,r)
                    mycursor.execute(sql)
                    mycursor.execute("commit")
                def EditBook():
                    e=e5.get()
                    print(e)
                    print("hello world")
                
                    
                    
                def new_user():
                    mainframe = Tk()
                    mainframe.title("New User")
                    mainframe.geometry("500x500")

                    # new user label
                    new_user_label = Label(mainframe,text="New User")
                    new_user_label.grid(row=0, column=0)

                    # error label
                    error_text = StringVar()
                    error_text.set("")
                    error_label = Label(mainframe, textvariable = error_text)
                    error_label.grid(row=0, column=2)


                    def submit_command():

                        # first name
                        first_name_storage = first_name_input.get()
                        

                        # surname
                        surname_storage = surname_input.get()

                        # registration plate
                        registration_plate_storage = registration_plate_input.get()

                        # vehicle_make
                        vehicle_make_storage = vehicle_make_input.get()

                        # employee_number
                        employee_number_storage = employee_number_input.get()

                        # mobile_number
                        mobile_number_storage = mobile_number_input.get()

                        # employer_department
                        

                        # extension_number
                        extension_number_storage = extension_number_input.get()

                        # postcode_travelled
                        postcode_travelled_storage = postcode_travelled_input.get()
                        
                        badge_storage = badge_input.get()
                        date='2018-06-09'
                        electric_car_storage=electric_car_input.get()
                        role_storage=role_input.get()
                        try:
                            username1=first_name_storage[0]+surname_storage
                        except:
                            
                            l=Label(mainframe,text="No fields can be empty").grid(row=15, column=1)
                            
                        sql = """INSERT INTO EMPLOYEE VALUES ({},'{}','{}','{}','{}','{}')""".format(employee_number_storage,first_name_storage,surname_storage, mobile_number_storage,extension_number_storage,postcode_travelled_storage)
                        mycursor.execute(sql)
                        sql = """INSERT INTO VEHICLE VALUES ('{}','{}','{}','{}')""".format(registration_plate_storage,employee_number_storage,vehicle_make_storage,electric_car_storage)
                        mycursor.execute(sql)
                        sql = """INSERT INTO CREDENTIALS VALUES ('{}','{}','{}','{}')""".format(username1,surname_storage,employee_number_storage,role_storage)
                        mycursor.execute(sql)
                        sql = """INSERT INTO BADGE_INFO VALUES ('{}','{}','{}')""".format(registration_plate_storage,date,badge_storage)
                        mycursor.execute(sql)
                        
                        mycursor.execute("commit")
                                  
                        
                        
                    
                    
                    # just realised i could have used a try except for this. I'll change tomorrow

                    # First Name
                    first_name = Label(mainframe,text="First Name:")
                    first_name.grid(row=1, column=1)

                    first_name_input = Entry(mainframe)
                    first_name_input.grid(row=1, column=2)

                    # Surname
                    surname = Label(mainframe,text="Surname:")
                    surname.grid(row=2, column=1)

                    surname_input = Entry(mainframe)
                    surname_input.grid(row=2, column=2)

                    # Registration plate
                    registration_plate = Label(mainframe,text="Registration Plate:")
                    registration_plate.grid(row=3, column=1)

                    registration_plate_input = Entry(mainframe)
                    registration_plate_input.grid(row=3, column=2)

                    # Vehicle make
                    vehicle_make = Label(mainframe,text="Vehicle make:")
                    vehicle_make.grid(row=4, column=1)

                    vehicle_make_input = Entry(mainframe)
                    vehicle_make_input.grid(row=4, column=2)

                    # Employee number
                    employee_number = Label(mainframe,text="Employee number:")
                    employee_number.grid(row=5, column=1)

                    employee_number_input = Entry(mainframe)
                    employee_number_input.grid(row=5, column=2)

                    # Mobile number
                    mobile_number = Label(mainframe,text="Mobile number:")
                    mobile_number.grid(row=6, column=1)

                    mobile_number_input = Entry(mainframe)
                    mobile_number_input.grid(row=6, column=2)

                  

                    # Extension number
                    extension_number = Label(mainframe,text="Extension number:")
                    extension_number.grid(row=8, column=1)

                    extension_number_input = Entry(mainframe)
                    extension_number_input.grid(row=8, column=2)

                    # Postcode travelled from
                    postcode_travelled = Label(mainframe,text="Postcode travelled from:")
                    postcode_travelled.grid(row=9, column=1)

                    postcode_travelled_input = Entry(mainframe)
                    postcode_travelled_input.grid(row=9, column=2)

                    badge = Label(mainframe,text="Badge:")
                    badge.grid(row=10, column=1)

                    badge_input = Entry(mainframe)
                    badge_input.grid(row=10, column=2)
                                         
                    l=Label(mainframe,text="Electric car: (0/1)").grid(row=11, column=1)
                    
                    electric_car_input = Entry(mainframe)
                    electric_car_input.grid(row=11, column=2)

                    l=Label(mainframe,text="Role/Permission: (").grid(row=12, column=1)
                    l=Label(mainframe,text="Role/Permission (0 employee/1 manager/2 facility/3 admin)").grid(row=13, column=1)
                    role_input = Entry(mainframe)
                    role_input.grid(row=12, column=2)
                    
                    



                    # Submit button
                    submit_button = Button(mainframe,text="Submit", command=submit_command)
                    submit_button.grid(row=14, column=2)

                    mainframe.mainloop()
                admin=Tk()
                admin.title("Admin Screen")
                btn = Button(admin, text="Create user",command=new_user).grid(column=0, row=1)
                Label(admin, text="Enter employees num: ").grid(row=2, column=0)
                e4=Entry(admin)
                
                    
                e4.grid(row=2,column=1)
                btn = Button(admin, text="Edit user",command=update_usr).grid(column=0, row=3)
            
                Label(admin, text="Enter employees num ").grid(row=5, column=0)
                e5=Entry(admin)
                e5.grid(row=5,column=1)
                
                btn = Button(admin, text="Check/Manage Employees bookings",command=EditBook).grid(column=0, row=6)
                btn = Button(admin, text="Create Reports",command=reports).grid(column=0, row=7)
                Label(admin, text="Enter Department").grid(row=10, column=0)
                e6=Entry(admin)
                e6.grid(row=10,column=1)
                btn = Button(admin, text="Add manager to a department",command=add_manager).grid(column=0, row=14)
                Label(admin, text="Enter managers employee number : ").grid(row=11, column=0)
                e7=Entry(admin)
                e7.grid(row=11,column=1)
                


                
                    
            def Facility():
                facility=Tk()
                home.title("Report Tab")
                btn = Button(facility, text="Check/Manage Employees bookings",command=report).grid(column=1, row=2)
                facility.mainloop()


            
                
            def booking_form():

    
                mainframe1 = Tk()
                mainframe1.title("Booking Form ")
                mainframe1.geometry("400x400")
                
                month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
                time = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                days31 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]



                month_days_28 = ["February"]
                month_days_30 = ["April", "June", "September", "November"]
                month_days_31 = ["January", "March","May", "July", "August", "October", "December"]

                def check():

                    def booking_selection():

                        mainframe2 = Tk()
                        mainframe2.title("Booking Selection")
                        mainframe2.geometry("400x400")

                        def cp():
                            mainframe2.destroy()

                        back_button = Button(mainframe2, text="Back", command=cp)
                        back_button.grid(row=1, column=0)

                        available_spaces_listbox = Listbox(mainframe2)
                        available_spaces_listbox.grid(row=0, column=1)

                        submit_button = Button(mainframe2, text="submit")
                        submit_button.grid(row=1, column=2)

                        def get_info():
                            l = available_spaces_listbox.curselection()
                            p = available_spaces_listbox.get(l[0])
                        
                    
                    day_storage = int(day_input.get())
                    month_storage = int(month_input.get())
                    from_storage = int(from_input.get())
                    to_storage = int(to_input.get())
                    

                    sql="Select vehicle_registration,electric from VEHICLE where fk_employee_num='{}'".format(employee_num)
                    mycursor.execute(sql)
                    resul=mycursor.fetchone()
                    veh_reg=resul[0]
                    electric=resul[1]
                    
                    sql="Select fk_badge_colour from BADGE_INFO where fk_vehicle_registration='{}'".format(veh_reg)
                    mycursor.execute(sql)
                    badge_info=mycursor.fetchone()
                    badge_info=badge_info[0]
                    
                    sql="Select start_blockout from BLOCKOUT_DATES where fk_badge_color='{}'".format(badge_info)
                    mycursor.execute(sql)
                    blackout_str=mycursor.fetchall()

                    sql="Select end_blockout from BLOCKOUT_DATES where fk_badge_color='{}'".format(badge_info)
                    mycursor.execute(sql)
                    blackout_end=mycursor.fetchall()
                    
                    
                    month=(2018,month_storage,day_storage)
                    print(month)
                    blockout=blackout_str[0]
                    
                    print(blockout)
                    
                    blockout1=blackout_str[1]
                    blockout2=blackout_str[2]
                    blockout3=blackout_str[3]
                    blockout4=blackout_str[4]
                    blockout5=blackout_end[0]
                    blockout6=blackout_end[1]
                    blockout7=blackout_end[2]
                    blockout8=blackout_end[3]
                    blockout9=blackout_end[4]
                    
                    
            


                    if badge_info=="Blue":
                        print("hello")
                     
                    if electric==1:
                        if month==blockout:
                            
                            print("hello")
                    
                              
                    
                                   
                    

                    booking_selection()

                    

                

                # search_Button
                search_button = Button(mainframe1, text="Search", command=check)
                search_button.grid(row=4, column=1)


                """method below is called when the month is selected"""

                def get_day(input_day):
                    input_day_string = str(input_day)

                    print(input_day_string)
                    return input_day_string



                day_input_label = Label(mainframe1, text="Day:").grid(row=0,column=0)
                day_input = Entry(mainframe1)
                day_input.grid(row=0, column=1)


                month_input_label= Label(mainframe1, text="Month:").grid(row=1,column=0)
                month_input = Entry(mainframe1)
                month_input.grid(row=1, column=1)


                time_label = Label(mainframe1, text="Time:").grid(row=2,column=0)

                from_label = Label(mainframe1,text="From:").grid(row=2,column=1)
                from_input =Entry(mainframe1)
                from_input.grid(row=2, column=2)

                to_label = Label(mainframe1, text="To:").grid(row=2,column=3)
                to_input = Entry(mainframe1)
                to_input.grid(row=2, column=4)



                mainframe1.mainloop()

            def edit_click():
                print(var.get())


            def department():
                r=manager_entry.get()
                sql = """INSERT INTO EMPLOYEE_EMPLOYER_LINK VALUES ({},'{}')""".format(employee_num,r)
                mycursor.execute(sql)
                mycursor.execute("commit")
               
                
                
                        


            def home_page():
                global home_page_window
                home_page_window = Tk()
                global manager_entry

                global var
                var = StringVar()
                var.set(1)
                
                if role==1:
                    btn = Button(home_page_window, text="Manager menu",command=manager).grid(column=7, row=3)
                elif role==2:
                    btn = Button(home_page_window, text="Facility menu",command=Facility).grid(column=7, row=3)
                elif role==3:
                    btn = Button(home_page_window, text="Admin menu",command=Systemadmin).grid(column=7, row=3)
                else:
                    space_lbl2 = Label(home_page_window, text='Enter/Change department currently working for:  ')
                    space_lbl2.grid(row=14, column=1)
                    manager_entry = Entry(home_page_window)
                    manager_entry.grid(row=15, column=1)

                    space_lbl3 = Label(home_page_window, text=' ')
                    space_lbl3.grid(row=16, column=1)

                    manager_button = Button(home_page_window, text='Submit', command=department)
                    manager_button.grid(row=17, column=1)
                    
                
                def c():
                    home_page_window.destroy()
                btn = Button(home_page_window, text="Log out",command=c).grid(column=5, row=1)
                
                home_page_window.title('Home Page')
                home_page_window.geometry('600x600')

                booking_button = Button(home_page_window, text='Booking', command=booking_form)
                booking_button.grid(row=0, column=1)

                space_lbl = Label(home_page_window, text='  ')
                space_lbl.grid(row=1, column=1)
                
                
                #DROP DOWN MENU TO STILL IN WORKS
                
                mycursor.execute("select *  from BOOKINGS  where fk_employee_num=2")
                Bookings=mycursor.fetchall()
                print(Bookings)
                
                    
                
                listbox = Listbox(home_page_window)
                listbox.grid(row=2, column=1)
                listbox.config(width=50, height=20)
                
                x=0
                for item in Bookings:
                    
                    listbox.insert(END,Bookings[x])
                    x=x+1
                    
                
                space_lbl1 = Label(home_page_window, text='  ')
                space_lbl1.grid(row=12, column=1)
                def Edit():
                    l=listbox.curselection()
                    p=listbox.get(l[0])
                    




                    
                    
                edit_button = Button(home_page_window, text='Edit', command=Edit)
                edit_button.grid(row=13, column=1)

                

               

                home_page_window.mainloop()


            home_page()
        try:
            usern=usern[0]+passw[0]
        except:
            error=Tk()
            #Label(error, text="Username or password is wrong").grid(row=1, column=0)     
            def close():
                error.destroy()
            btn = Button(error, text="close",command=close).grid(column=1, row=3)
            error.mainloop()
                     
        
        
        username=username+password
       
        
        if usern==username :
            employee()
            
            
        
           
            
           
    btn = Button(home, text="Log In",command=callback).grid(column=1, row=3)
    home.mainloop()
        


login()






