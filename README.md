# What is PyVariable?
Basically what this module does is to save variables ouside the code. </br>
Let's say you've created a game with pygame. There is a high score system and you want to save the highest score in an online database so that users all over the world can see the highest score. Here comes the usage of PyVariable. Yes you can also do it without PyVariable, but you've to write more to do so. Again, if you don't want a variable to be reset everytime you run your code, you should use PyVariable. Using PyVariable, you can save a variable in your device (offline) or in an online database. It's really simple enough.

</br></br></br>

# Installation
Installing the module is quite easy ;)
Simple open your terminal and enter <code> pip install pyvariable</code>.</br></br>
<b><i>Note: If you face any error like <code> ModuleNotFoundError: No module named 'Crypto'</code>, then follow these steps - </i></b></br>
<i>Step 1:</i> &nbsp; Open your terminal. </br>
<i>Step 2:</i> &nbsp; Enter <code> pip uninstall crypto</code>. </br>
<i>Step 3:</i> &nbsp; Enter <code> pip uninstall pycryptodome</code>. </br>
<i>Step 4:</i> &nbsp; Enter <code> pip install pycryptodome</code>.

</br></br></br></br>

# LocalVariable
Import the module and create an object of the class <b>LocalVariable</b>. Call the <b>save</b> method with the name and the value of a variable as argument to store your data locally and call any of the methods from the list below to read the value. </br>
<ul>
      <li> read_int (var_name) </li>
      <li> read_float (var_name) </li>
      <li> read_str (var_name) </li>
      <li> read_bool (var_name) </li>
      <li> read_list (var_name) </li>
      <li> read_tuple (var_name) </li>
      <li> read_set (var_name) </li>
      <li> read_dict (var_name) </li>
</ul>
Also, call exists() method with name of a variale as argument to check if the variable exists. <b><i>Note: It will return True or False.</i></b></br>
</br></br>
Here is a sample code -
<pre>
import pyvariable
data = pyvariable.LocalVariable()
data.save("Name", "John")  # This will store the variable Name with the value John
LocalName = data.read_str("Name")  # This will read the value of Name from files and store in LocalName
print(LocalName)  # This will print John
</pre>
Another example of checking if a variable exists -
<pre>
import PyVariable
data = Variables.LocalVariable()
if data.exists("X"):  # The method returns true if the variable exists
      print("The variable X exists")
else:
      print("The variable X doesn't exist")
</pre>

</br></br></br></br></br>
# CloudVariable
<h3>Setting up your database:</h3>
<i>Step 1</i>: &nbsp; Go to https://console.firebase.google.com/ </br>
<i>Step 2</i>: &nbsp; Login with your google account. </br>
<i>Step 3</i>: &nbsp; Click on <b>Add Project</b></br>
<i>Step 4</i>: &nbsp; Enter any name (The name doesn't matter at all). </br>
<i>Step 5</i>: &nbsp; Disable <b>Google Analytics</b> and click on continue. </br>
<i>Step 6</i>: &nbsp; After the the database creation is finished, click on continue and you'll see a window like this. </br>
<i>Step 7</i>: &nbsp; Click on <b>Realtime Database</b> on the left. </br>
<i>Step 8</i>: &nbsp; Click on <b>Create Database</b> and select your nearest location. </br>
<i>Step 9</i>: &nbsp; After clicking <b>Next</b>, Select <b>Start in test mode</b> and click on <b>Enable</b> </br>
<i>Step 10</i>: &nbsp; Finally, just copy this url as shown in the image.</br></br>
<p align="CENTER" style="margin:5px;"><img src="step10.jpg" alt="Step 10" width = 800></p>
<i>Step11</i>: &nbsp; Now go to your code and import the module <b>Variables</b>.</br>
<i>Step12</i>: &nbsp; After that create an object of the class <b>CloudVariable</b> with the url you copied as argument. </br></br>

Everything is now ready. Simply call the <b>save</b> method with the name and the value of a variable as argument to store your data online and call the <b>read</b> method with the name of your variable as argument to read the value. <i>Note: The returned value will automatically be in your desired data type.</i></br>
</br></br>
Here is a sample code -
<pre>
import pyvariable
data = pyvariable.CloudVariable(The_Url_You_Copied)
data.save("Name", "John")  # This will store the variable Name with the value John
LocalName = data.read("Name")  # This will read the value of Name from your database and store in LocalName
print(LocalName)  # This will print John
</pre>
<b><i>Note: You have to use multiple firebase database (Not account) for multiple projects, simply follow from step 3</i></b>

</br></br></br></br>

# Some example usage
Example 1 (Count how many times a code is run):
<pre>
import pyvariable  # Importing the module

count = 0
data = pyvariable.LocalVariable()  # Create the object
if not data.exists("count"):  # Create a variable if it doesn't exist
    data.save("count", 0)
count = data.read_int("count")  # This will read the value of count and store in count variable
count = count + 1
data.save("count", count)  # This will store the variable count with the value John
print("This program ran " + str(count) + " times")

</pre>

</br></br></br></br>

# Lisence
This module is completely free and open source. You can freely use and modify the module if you want. Any suggestion will be highly appreciated ;) </br>
Created by <b> Sajedur Rahman Fiad </b> </br>
Email : <code> neural.gen.official@gmail.com</code> </br>
<i> Let me know your valuable feedback. </i>
