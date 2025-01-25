# Python_Project_Team


Role-based Access:

A and B (Field Executives) can only add and view their own data.
C (Field Manager) can view data from both A and B.
D (Field Manager) cannot view data from A or B.
E (Senior Manager) can view, update, and delete data from A and B.
Adding Data:

Field Executives can input data, which is stored in their respective lists.
Viewing Data:

Access to data is restricted based on the user's role.
Updating and Deleting Data:

Only the Senior Manager (E) can update or delete any data from A and B.
Data Storage:

The data is stored in a dictionary (data_storage), with keys as A and B.
To Run the Code:
Save the code team.py.
