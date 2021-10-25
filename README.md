![Android or Windows](https://img.shields.io/badge/OS-Android%20%20%7C%20%20Windows-orange) &nbsp; &nbsp;
![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange)

</br>

<h3>Are you having problem keeping variables outside of your python program
or writting and managing codes for your cloud database? 🥵</h3>

<h4>Don't destroy your pc or damage your head ❌. </h4>
Try <b>PyDataman</b> 👷‍♂️, he will do all the hard works on your behalf!!

</br></br></br></br>

# What is PyDataman?
<b>Basically this module is for saving data specially variables including other data like images or text files outside your code so that you never ever lose them.</b> </br>
Let's say you've created a game with pygame. There is a high score system and you want to save the highest score in an online database so that users all over the world can see the highest score. Here comes the usage of <b>PyDataman</b>. Yes you can also do it without <b>PyDataman</b>, but you've to write more to do so. </br>
Again, let's say you don't want a variable to be reset everytime you run your code, here you must use <b>PyVariable</b>. Using <b>PyDataman</b>, you can save a variable in your drive (offline) or in an online database. It's really simple enough.</br></br>
One more feature, you can save any of your files in an online databse and download from any device whenever and wherever you need them.</br></br>

<h3> <i> Note: You can save and read variables of any data type even lists, tuples, sets and dictionaries. All of them is supported. </i></h3>

</br></br></br></br>

# Installation
Installing the module is quite easy ;) </br>
Simple open your terminal and enter <code> pip install pydataman</code>.</br></br>
<i> Note: If you are having any problem with the installation, feel free to contact me in </i>[Gmail](neural.gen.official@gmail.com) <i>and in </i>[facebook](https://www.facebook.com/neuralgen)


</br></br></br></br>


# Variable in Folder
</br> Save your variables outside your code so that whenever you restart your code, you won't lose them. Here's how to do it - </br></br>
Simply import the module. Call the <code> save(var_name, value)</code> method with the name and the value of a variable as argument to store your data locally and call <code> read(var_name)</code> to read the value. The value will already be in your desired data type, no need to covert again.</br>

Also, call <code> exists()</code> method with name of a variable as argument to check if the variable exists. </br> <b><i>Note: It will return True or False.</i></b>
</br></br></br></br>

Here is a sample code - </br>

```python
import pydataman

pydataman.save("Name", "John")  # This will store the variable Name with the value John
LocalName = pydataman.read("Name")  # This will read the value of Name from files and store in LocalName
print(LocalName)  # This will print John
```

Another example of checking if a variable exists -</br>

```python
import pydataman

if pydataman.exists("X"):  # The method returns true if the variable exists in your folder
      print("The variable X exists")
else:
      print("The variable X doesn't exist")
```




</br></br></br></br>




# Variable in online database

</br> Store your variables online so that everytime you restart your code, you don't lose the values. Even you can create a variable from a device and access it's value from another. Here's how to do these -
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
<i>Step 10</i>: &nbsp; Go to <b> Rules</b> tab and replace the code by this - </br>
<pre>
{
  "rules": {
    ".read": "True",
    ".write": "True",
  }
}
</pre>
<i>Step 11</i>: &nbsp; Finally, come back to <b>Data</b> tab and just copy this url shown in the image.</br></br>
<p align="CENTER" style="margin:5px;"><img src="step10.jpg" alt="Step 10" width = 800></p>
<i>Step 12</i>: &nbsp; Now go to your code and import the module <code> pydataman</code>.</br>
<i>Step 13</i>: &nbsp; After that create an object of the class <code> CloudVariable</code> with the url you copied as argument. </br></br>

Everything is now ready. Simply call the <code> save()</code> method with the name and the value of a variable as argument to store your data online and call the <code> read()</code> method with the name of your variable as argument to read the value of it. </br> <b><i>Note: The returned value will automatically be in your desired data type.</i></b></br>
Also, call <code> exists()</code> method with name of a variable as argument to check if the variable exists.<i>It will return True or False.</i></br>
</br></br>


Here is a sample code -
```python
import pydataman

data = pydataman.CloudVariable(The_Url_You_Copied)

data.save("Name", "John")  # This will store the variable Name with the value John
LocalName = data.read("Name")  # This will read the value of Name from your database and store in LocalName
print(LocalName)  # This will print John
```


Another example of checking if a variable exists -
```python
import pydataman

data = pydataman.CloudVariable(The_Url_You_Copied)

if data.exists("X"):  # The method returns true if the variable exists in your database
      print("The variable X exists")
else:
      print("The variable X doesn't exist")
```

</br>
<b><i>Note: You have to use multiple firebase database (Not account) for multiple projects.</i></b></br>




</br></br></br></br>




# Store files online
</br> Store your files online like variables, and here is how to do it -
<h3>Setting up your online storage:</h3>
<i>Step 1</i>: &nbsp; Go to https://console.firebase.google.com/ </br>
<i>Step 2</i>: &nbsp; Login with your google account. </br>
<i>Step 3</i>: &nbsp; Click on <b>Add Project</b></br>
<i>Step 4</i>: &nbsp; Enter any name (The name doesn't matter at all). </br>
<i>Step 5</i>: &nbsp; Disable <b>Google Analytics</b> and click on continue. </br>
<i>Step 6</i>: &nbsp; The project creation is now finished. </br>
<i>Step 7</i>: &nbsp; Click on <b>Storage</b> on the left. </br>
<i>Step 8</i>: &nbsp; Click on <b>Get Started</b> and click next. </br>
<i>Step 9</i>: &nbsp; Select your nearest location and click done. </br>
<i>Step 10</i>: &nbsp; Now go to <b> Rules</b> tab and replace the line <code> allow read, write: if request.auth != null;</code> by <code> allow read, write</code> </br>
<i>Step 11</i>: &nbsp; Then click the settings icon beside <b>Project Overview</b> on the left and select <b>Project settings</b>.</br>
<i>Step 12</i>: &nbsp; Click on the <code> &lt;/&gt;</code> icon under <b>Your apps</b>.</br>
<i>Step 13</i>: &nbsp; Enter any name and press register.</br>
<i>Step 14</i>: &nbsp; Copy the items of the dictionary <code> firebaseConfig</code>, it's important.</br>
<i>Step 15</i>: &nbsp; Click <b>Continue to console</b>.</br>
<i>Step 16</i>: &nbsp; Now go to <b>Service accounts</b> tab and select <b>Python</b>.</br>
<i>Step 17</i>: &nbsp; Click on <b>Generate new private key</b> and save the key in any easy-to-remember name.</br>
<i>Step 18</i>: &nbsp; Finally click on <b>Storage</b> on the left and you are ready for the code.</br>
<i>Step 19</i>: &nbsp; Now go to your code and import the module <code> pydataman</code>.</br>
<i>Step 20</i>: &nbsp; After that create an object of the class <code> CloudFile</code> with these 2 arguments -</br></br>
<ul>
      <li>The dictionary you recently copied.</li>
      <li>The directory of you private key file</li>
</ul></br></br>
<b><i>Note 1: You can find the dictionary in the general tab in project settings.</i></b></br>
<b><i>Note 2: You have to convert the dictionary to Python as it is written in JavaScript. (Don't worry, you don't need to know javascript)</i></b></br>
<b><i>Note 3: Only <code> "apiKey"</code>, <code> "authDomain"</code>, <code> "databaseURL"</code> and <code> "storageBucket"</code> is needed. Others are optional.</i></b></br></br></br>


Everything is now ready. Simply import the module <code> pydataman</code>, call the <code> upload()</code> method with the name of your variable and the directory of your file (in your local device) as argument to upload your file online and call the <code> download()</code> method with the name of your variable and the path you want to save the file as argument to download the file. <b></br>
</br></br>
Some othe methods available in this <code> CloudFile</code>:</br>
<ul>
      <li><code> exists(variable_name) </code> - This will search for a file, returns True if the file exists and False if it doesn't.</li>
      <li><code> all_vars() </code> - Ths will return a list of all file names available in your database.</li>
</ul>
</br></br></br>

Here is a sample code - <br>

```python
import pydataman

#You must change the values of config as your own info, otherwise the code won't work
config = {
    "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
    "authDomain": "variables-2da3.firebaseapp.com",
    "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "variables-2da3.appspot.com",
}

file = pydataman.CloudFile(config, serviceAccount)
file.upload("Image", "MyFile.png")  #The file "MyFile.png" is now uploaded as name "Image"
file.download("Image", path = "MyFile.png")  #This will download the file named "Image" and save as "MyFile.png"
```

Another example of checking if a file exists in your database - </br>

```python
import pydataman

#You must change the values of config as your own info, otherwise the code won't work
config = {
    "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
    "authDomain": "variables-2da3.firebaseapp.com",
    "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "variables-2da3.appspot.com",
}

file = pydataman.CloudFile(config, serviceAccount)
if file.exists("Logo"):  #The method returns true if the variable exists in your database
      print("The logo exists in your database")
else:
      print("The logo doesn't exist in your database")
```

</br></br>
<h4><i>Twist: </i> You can save the firebaseConfig dictionary using <code> CloudVariable()</code> and use in <code> CloudFile()</code> whenever you want so that you don't have any chance to lose them. </h4>






</br></br></br></br>





# Some example usage
<h3>Example 1.1 (Count how many times a code is run) - Saving in your drive:</h3>

```python
import pydataman  # Importing the module

count = 0
if not pydataman.exists("count"):  # Create a variable if it doesn't exist
    pydataman.save("count", 0)
        
count = pydataman.read("count")  # This will read the value of count and store in count variable
count = count + 1
    
pydataman.save("count", count)  # This will store the variable count with the value of count
print("This program ran " + str(count) + " times")
```

</br></br>

<h3>Example 2  (Storing my accounts in online database):</h3>

```python
import pydataman  # Importing the module
    
data = pydataman.CloudVariable(the_url_you_copied)  # Create the object
    
Accounts = {"myemail@gmail.com" : "mypassword",
              "mysecondemail@gmail.com" : "hardpassword",
              "blahblahemail@gmail.com" : "blahblahpassword"}
                  
data.save("MyAccounts", Accounts)  # This will store the dictionary with name MyAccounts
```

After running the code above, you can run this code from anywhere in the world and any device you want to get the value of MyAccounts -

```python
import pydataman  # Importing the module
    
data = pydataman.CloudVariable(the_url_you_copied)  # Create the object
Accounts = {}
                  
Accounts = data.read("MyAccounts")  # This will load the dictionary MyAccounts from your database
```

</br></br>

<h3>Example 3 (Save an excel file in online storage):</h3>

```python
import pydataman

#You must change the values of config as your own info, otherwise the code won't work
config = {
    "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
    "authDomain": "variables-2da3.firebaseapp.com",
    "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "variables-2da3.appspot.com",
}
    
file = pydataman.CloudFile(config, serviceAccount)
file.upload("MyExcelFile", "Data.xlsx")  # This will upload the file in your storage
```



</br></br></br></br></br>




# Troubleshooting - Some common problems you might face
&nbsp;&nbsp; <h3> Problem 1 - <code> ModuleNotFoundError: No module named 'Crypto'</code> </h3>
&nbsp;&nbsp; <b><i>If you get any error like this while running your code, try following these steps - </i></b></br>
&nbsp;&nbsp; <i>Step 1:</i> &nbsp; Open your terminal. </br>
&nbsp;&nbsp; <i>Step 2:</i> &nbsp; Enter <code> pip uninstall crypto</code>. </br>
&nbsp;&nbsp; <i>Step 3:</i> &nbsp; Enter <code> pip uninstall pycryptodome</code>. </br>
&nbsp;&nbsp; <i>Step 4:</i> &nbsp; Enter <code> pip install pycryptodome</code>.

&nbsp;&nbsp; <h3> Problem 2 - <code> ... has no attribute ...</code> </h3>
&nbsp;&nbsp; <b><i>If you get this type of error after the module is updated, try upgrading the module - </i></b></br>
&nbsp;&nbsp; <i>Step 1:</i> &nbsp; Open your terminal. </br>
&nbsp;&nbsp; <i>Step 2:</i> &nbsp; Enter <code> pip install pydataman -U</code>. </br>



</br></br></br></br>



# Lisence
This module is completely free and open source. You can freely use and modify the module if you want. Any suggestion will be highly appreciated ;) </br>
Created by <b> Sajedur Rahman Fiad</b> and <b>Jonayed Mohiuddin Shanto</b> </br>
Email : <code> neural.gen.official@gmail.com</code> </br></br>
<i> Let me know your valuable feedback. </i>
