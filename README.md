![Android or Windows](https://img.shields.io/badge/OS-Android%20%20%7C%20%20Windows-orange) &nbsp; &nbsp;
![Made with Python](https://img.shields.io/badge/Made%20with-Python-orange)

</br>

# What is PyVariable?
<b>Basically this module is for saving variables outside your code so that you don't lose their value.</b> </br>
Let's say you've created a game with pygame. There is a high score system and you want to save the highest score in an online database so that users all over the world can see the highest score. Here comes the usage of <b>PyVariable</b>. Yes you can also do it without <b>PyVariable</b>, but you've to write more to do so. </br>
Again, let's say you don't want a variable to be reset everytime you run your code, here you must use <b>PyVariable</b>. Using <b>PyVariable</b>, you can save a variable in your drive (offline) or in an online database. It's really simple enough.</br></br>
One more feature, you can save any of your files in an online databse and download from any device whenever and wherever you need them.</br>

</br></br></br>

# Installation
Installing the module is quite easy ;) </br>
Simple open your terminal and enter <code> pip install pyvariable</code>.</br></br>
<b><i>Note: If you face any error like <code> ModuleNotFoundError: No module named 'Crypto'</code>, then follow these steps - </i></b></br>
<i>Step 1:</i> &nbsp; Open your terminal. </br>
<i>Step 2:</i> &nbsp; Enter <code> pip uninstall crypto</code>. </br>
<i>Step 3:</i> &nbsp; Enter <code> pip uninstall pycryptodome</code>. </br>
<i>Step 4:</i> &nbsp; Enter <code> pip install pycryptodome</code>.

</br></br></br></br>

# Variable in Folder
Import the module and create an object of the class <code> LocalVariable</code>. Call the <code> save()</code> method with the name and the value of a variable as argument to store your data locally and call any of the methods from the list below to read the value. </br>
<ul>
      <li><code> read_int (var_name) </code></li>
      <li><code> read_float (var_name) </code></li>
      <li><code> read_str (var_name) </code></li>
      <li><code> read_bool (var_name) </code></li>
      <li><code> read_list (var_name) </code></li>
      <li><code> read_tuple (var_name) </code></li>
      <li><code> read_set (var_name) </code></li>
      <li><code> read_dict (var_name) </code></li>
</ul>
Also, call <code> exists()</code> method with name of a variable as argument to check if the variable exists. </br> <b><i>Note: It will return True or False.</i></b></br>
</br></br>
Here is a sample code -
<pre>
import pyvariable
data = pyvariable.LocalVariable()
data.save("Name", "John")  # This will store the variable Name with the value John
LocalName = data.read_str("Name")  # This will read the value of Name from files and store in LocalName
print(LocalName)  # This will print John
</pre>
Another example of checking if a variable exists -</br>
<pre>
import pyvariable
data = pyvariable.LocalVariable()
if data.exists("X"):  # The method returns true if the variable exists in your folder
      print("The variable X exists")
else:
      print("The variable X doesn't exist")
</pre>




</br></br></br></br>




# Variable in online database
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
<i>Step 12</i>: &nbsp; Now go to your code and import the module <code> pyvariable</code>.</br>
<i>Step 13</i>: &nbsp; After that create an object of the class <code> CloudVariable</code> with the url you copied as argument. </br></br>

Everything is now ready. Simply call the <code> save()</code> method with the name and the value of a variable as argument to store your data online and call the <code> read()</code> method with the name of your variable as argument to read the value of it. </br> <b><i>Note: The returned value will automatically be in your desired data type.</i></b>
Also, call <code> exists()</code> method with name of a variable as argument to check if the variable exists.<i> Note: It will return True or False.</i></br>
</br></br></br>


Here is a sample code -
```python
import pyvariable

data = pyvariable.CloudVariable(The_Url_You_Copied)
data.save("Name", "John")  # This will store the variable Name with the value John
LocalName = data.read("Name")  # This will read the value of Name from your database and store in LocalName
print(LocalName)  # This will print John
```


Another example of checking if a variable exists -
```python
import pyvariable

data = pyvariable.CloudVariable(The_Url_You_Copied)
if data.exists("X"):  # The method returns true if the variable exists in your database
      print("The variable X exists")
else:
      print("The variable X doesn't exist")
```
<b><i>Note: You have to use multiple firebase database (Not account) for multiple projects.</i></b>




</br></br></br></br>




# Store files online
<h3>Setting up your online storage:</h3>
<i>Step 1</i>: &nbsp; Go to https://console.firebase.google.com/ </br>
<i>Step 2</i>: &nbsp; Login with your google account. </br>
<i>Step 3</i>: &nbsp; Click on <b>Add Project</b></br>
<i>Step 4</i>: &nbsp; Enter any name (The name doesn't matter at all). </br>
<i>Step 5</i>: &nbsp; Disable <b>Google Analytics</b> and click on continue. </br>
<i>Step 6</i>: &nbsp; The database creation is now finished. </br>
<i>Step 7</i>: &nbsp; Click on <b>Storage</b> on the left. </br>
<i>Step 8</i>: &nbsp; Click on <b>Get Started</b> and click next. </br>
<i>Step 9</i>: &nbsp; Select your nearest location and click done. </br>
<i>Step 10</i>: &nbsp; Now go to <b> Rules</b> tab and replace the line <code> allow read, write: if request.auth != null;</code> by <code> allow read, write</code> </br>
<i>Step 11</i>: &nbsp; Then click the settings icon beside <b>Project Overview</b> on the left and select <b>Project settings</b>.</br>
<i>Step 12</i>: &nbsp; Click on the <code> &lt;/&gt;</code> icon under <b>Your apps</b>.</br>
<i>Step 13</i>: &nbsp; Enter any name and press register.</br>
<i>Step 14</i>: &nbsp; Note the items of the dictionary <code> firebaseConfig</code>, it's important.</br>
<i>Step 15</i>: &nbsp; Click <b>Continue to console</b>.</br>
<i>Step 16</i>: &nbsp; Now go to <b>Service accounts</b> tab and select <b>Python</b>.</br>
<i>Step 17</i>: &nbsp; Click on <b>Generate new private key</b> and save the key in any easy-to-remember name.</br>
<i>Step 18</i>: &nbsp; Finally click on <b>Storage</b> on the left and you are ready for the code.</br>
<i>Step 19</i>: &nbsp; Now go to your code and import the module <code> pyvariable</code>.</br>
<i>Step 20</i>: &nbsp; After that create an object of the class <code> CloudFile</code> with these 2 arguments -</br>
<ul>
      <li>The dictionary you recently copied.</li>
      <li>The directory of you private key file</li>
</ul>
<b><i>Note 1: You can find the dictionary whenever you need in the general tab in project settings.</i></b></br>
<b><i>Note 2: You have to modify the dictionary a little bit in Python format because it is written in JavaScript.</i></b></br>

Everything is now ready. Simply call the <code> upload()</code> method with the name and the value of a variable as argument to upload your file online and call the <code> download()</code> method with the name of your variable as argument to download the file. </br> <b><i>Note: By default, the file will save in the same directory your code is in. To change it, modify the argument <code> path</code> in the download method.</i></b>
Some othe methods available in this class:</br>
<ul>
      <li><code> exists (file_name) </code> - This will search for a file, returns True if the file exists and False if it doesn't.</li>
      <li><code> download_all (path) </code> - This will download all the files available in your database</li>
      <li><code> get_all_file_names () </code> - Ths will return a list of all file names available in your database.</li>
</ul>
</br></br></br>
Here is a sample code - <br>
<pre>
import pyvariable

#You must change the values of config as your own info, otherwise the code won't work
config = {
    "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
    "authDomain": "variables-2da3.firebaseapp.com",
    "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "variables-2da3.appspot.com",
}
file = pyvariable.CloudFile(config, serviceAccount)
file.upload("MyFile.png")  #This will upload the file in your storage
file.download("MyFile.png")  #This will download the file in the same directory the code is in
#To download in custom directory, the statement would be - file.download("MyFile.png", path=myPath)
</pre>
Another example of checking if a file exists -
<pre>
import pyvariable

#You must change the values of config as your own info, otherwise the code won't work
config = {
    "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
    "authDomain": "variables-2da3.firebaseapp.com",
    "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "storageBucket": "variables-2da3.appspot.com",
}
file = pyvariable.CloudFile(config, serviceAccount)
if file.exists("NeuralgenLogo.jpg"):  #The method returns true if the variable exists in your database
      print("The logo exists in your database")
else:
      print("The logo doesn't exist in your database")
</pre>
</br></br>
<h3><i>A twist: </i> You can save the dictionary items as variables and use in <code> CloudFile</code> whenever you want so that you don't have any chance to lose them. </h3>






</br></br></br></br>





# Some example usage
Example 1.1 (Count how many times a code is run) - Saving in your drive:

```python
    import pyvariable  # Importing the module

    count = 0
    data = pyvariable.LocalVariable()  # Create the object
    if not data.exists("count"):  # Create a variable if it doesn't exist
        data.save("count", 0)
    count = data.read_int("count")  # This will read the value of count and store in count variable
    count = count + 1
    data.save("count", count)  # This will store the variable count with the value John
    print("This program ran " + str(count) + " times")
```

</br>

Example 1.2 (Count how many times a code is run) - Saving in online database:
```python
    import pyvariable  # Importing the module

    count = 0
    data = pyvariable.CloudVariable(the_url_you_copied)  # Create the object
    if not data.exists("count"):  # Create a variable if it doesn't exist
        data.save("count", 0)
    count = data.read("count")  # This will read the value of count and store in count variable
    count = count + 1
    data.save("count", count)  # This will store the variable count with the value John
    print("This program ran " + str(count) + " times")
```

</br>

Example 2 (Save an excel file in online storage):
```python
    import pyvariable

    #You must change the values of config as your own info, otherwise the code won't work
    config = {
        "apiKey": "AIzaSyBy37khExSIw-XZK2kT17_P1jPSxDt2rj",
        "authDomain": "variables-2da3.firebaseapp.com",
        "databaseURL": "https://variables-2da3-default-rtdb.asia-southeast1.firebasedatabase.app",
        "storageBucket": "variables-2da3.appspot.com",
    }
    file = pyvariable.CloudFile(config, serviceAccount)
    file.upload("Data.xlsx")  # This will upload the file in your storage
```

</br></br></br></br>

# Lisence
This module is completely free and open source. You can freely use and modify the module if you want. Any suggestion will be highly appreciated ;) </br>
Created by <b> Sajedur Rahman Fiad </b> </br>
Email : <code> neural.gen.official@gmail.com</code> </br></br>
<i> Let me know your valuable feedback. </i>
