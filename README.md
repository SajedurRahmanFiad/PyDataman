# CloudVariable
</br>
<i>Step1</i>: &nbsp; Go to https://console.firebase.google.com/ </br>
<i>Step2</i>: &nbsp; Login with your google account. </br>
<i>Step3</i>: &nbsp; Click on <b>Add Project</b></br>
<i>Step4</i>: &nbsp; Enter any name (The name doesn't matter at all). </br>
<i>Step5</i>: &nbsp; Disable <b>Google Analytics</b> and click on continue. </br>
<i>Step6</i>: &nbsp; After the the database creation is finished, click on continue and you'll see a window like this. </br>
<i>Step7</i>: &nbsp; Click on <b>Realtime Database</b> on the left. </br>
<i>Step8</i>: &nbsp; Click on <b>Create Database</b> and select your nearest location. </br>
<i>Step9</i>: &nbsp; After clicking <b>Next</b>, Select <b>Start in test mode</b> and click on <b>Enable</b> </br>
<i>Step10</i>: &nbsp; Finally, just copy this url as shown in the image.</br></br>
<p align="CENTER" style="margin:5px;"><img src="step10.jpg" alt="Step 10" width = 800></p>
<i>Step11</i>: &nbsp; Now go to your code and import the module <b>Variables</b>.</br>
<i>Step12</i>: &nbsp; After that create an object of the class <b>CloudVariable</b> with the url you copied as argument. </br></br>

Everything is now ready. Simply call the <b>save</b> method with the name and the value of a variable as argument to store your data online and call the <b>read</b> method with the name of your variable as argument to read the value. </br>
</br></br>
Here is a sample code -
<pre>
      import Variables
      data = Variables.CloudVariable(The_Url_You_Copied)
      data.save("Name", "John")  # This will store the variable Name with the value John
      LocalName = data.read("Name")  # This will read the value of Name from cloud and store in LocalName
      print(LocalName)  # This will print John
</pre>
