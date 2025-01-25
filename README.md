# Python_Project_Team


*Role-based Access:

1.A and B (Field Executives) can only add and view their own data.
2.C (Field Manager) can view data from both A and B.
3.D (Field Manager) cannot view data from A or B.
4.E (Senior Manager) can view, update, and delete data from A and B.
Adding Data:

**Field Executives can input data, which is stored in their respective lists.
Viewing Data:

#Access to data is restricted based on the user's role.
Updating and Deleting Data:

##Only the Senior Manager (E) can update or delete any data from A and B.
Data Storage:

##The data is stored in a dictionary (data_storage), with keys as A and B.
To Run the Code:
Save the code team.py.





#  Output

PS E:\python Project> python team.py

Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): E

Available actions:
1. Add Data (Only for Field Executives A and B)
2. View Data
3. Update Data (Only for Senior Manager E)
4. Delete Data (Only for Senior Manager E)
Choose an action (1/2/3/4): 2
Data accessible to Senior Manager E:
Data from A: ['sham', 'hyderabd']
Data from B: ['kiran', 'delhi']


Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): A

Available actions:
1. Add Data (Only for Field Executives A and B)
2. View Data
3. Update Data (Only for Senior Manager E)
4. Delete Data (Only for Senior Manager E)
Choose an action (1/2/3/4): 2
Data for A: ['sham', 'hyderabd']


Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): B

Available actions:
1. Add Data (Only for Field Executives A and B)
2. View Data
3. Update Data (Only for Senior Manager E)
4. Delete Data (Only for Senior Manager E)
Choose an action (1/2/3/4): 1
B, enter the data you want to add: Software developwe
Data added successfully by B.


Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): B

Available actions:
1. Add Data (Only for Field Executives A and B)
2. View Data
3. Update Data (Only for Senior Manager E)
4. Delete Data (Only for Senior Manager E)
Choose an action (1/2/3/4): 2
Data for B: ['kiran', 'delhi', 'Software developwe']


Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): C

Available actions:
1. Add Data (Only for Field Executives A and B)
2. View Data
3. Update Data (Only for Senior Manager E)
4. Delete Data (Only for Senior Manager E)
Choose an action (1/2/3/4): 1
You do not have permission to add data.


Roles: A, B (Field Executives), C, D (Field Managers), E (Senior Manager)
Enter your role (A/B/C/D/E or 'exit' to quit): exit
Exiting program.
PS E:\python Project> 
