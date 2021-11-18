# c1003077_Project2_OOP_contact_list

In this application, I have used DB Browser for the database to hold all contact information. This is because I have
previous experience with using DB Browser and SQL functions, so chose to pursue this option instead of using a csv file.
The application when run, gives the user options for different interactions available with the database. I have created
functions that can be accessed by the user by pressing specific keys, highlighted when the program is run. The
interactions available are updating, searching and adding new contacts to the database. The SQL statements 'SELECT' and
'UPDATE' are used to perform these functions. Furthermore, the 'fetchall' function is used to retrieve all information
from a table/database.

An assumption I have made with making this application is the way the user will give their inputs on contact information.
For example, I have added '.lower()' to input statements made, so that the program won't crash if the input given
is case insensitive. As well as this, I have added '+44' and 'dd/mm/yyyy' to the add contact function to increase
usability of the program so users know the types of format that is required to keep consistency.


