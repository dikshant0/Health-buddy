# Health Buddy
#### Video Demo:  <https://youtu.be/fy8aHFOWWi0>
#### Description:
The main purpose of Health Buddy application is to provide users with valuable health information related to their bodies, common diseases, and drugs. It achieves this through the use of a API call. It also stores information on existing users, as well as new users who sign up to use the application.

Upon running the program, users are greeted with a welcome screen featuring three options: Existing User Login, New User Registration, and Admin Login. Existing User Login allows individuals who have previously registered to enter their username and password to log in. New User Registration is intended for those who are new to the application, requiring basic personal information such as name, age, and gender, as well as the selection of a unique username and strong password. Finally, Admin Login is reserved for those with designated administrative privileges, allowing them to view all registered user data and delete user accounts.

When a new user signs up, their personal details (such as name, age, gender, username, and password) are recorded and stored in a CSV file name "data.csv". To provide security each of the users have to choose a unique username, that the application after reviewing the CSV provides available usernames. As two users cannot have the same username.

To provide extra security, the password follows a criterion that the user has to follow, i.e, the Password should contain atleast 8 letters, 1 Uppercase alphabet, 1 Lowercase alphabet, 1 numeric value, and 1 special symbol(@, #, ^, etc.).

After sign-up, the user can log in to his account, which is validated by checking the username and password in the CSV file. They can then use the app to access a range of health-related features.

One of the main features of the application is its Body Mass Index (BMI) calculator. This feature allows users to input their height and weight, and the application will calculate their BMI, which is a measure of body fat based on height and weight. This feature can help users understand their current health status and identify areas for improvement.

Another feature of the application is its ability to provide generic drug names for branded medicines. When a user enters the name of a branded medicine, the application make a API call to HealthWise API on RapidAPI.com to find the generic name for that medicine. This feature can help users save money by purchasing less expensive generic versions of their medications.

The application also provides information on common diseases for different organs. Users can select a particular organ (such as the heart, lungs, brain, etc.) and the application will provide information on common diseases associated with that organ. This feature can help users understand the health risks associated with different organs and take preventative measures to maintain good health.
This feature is also achieved by the help of an API call to HealthWise on rapidapi.com.

Finally, the application provides information on different drugs, including their uses, side effects, and interactions with other medications. This feature can help users make informed decisions about the medications they take and avoid any negative interactions that could cause harm.

In addition to these features, the application also includes an admin panel that allows authorized individuals to view and manage the database of users. Admins can view user information, delete existing users, and perform other tasks related to managing the application.