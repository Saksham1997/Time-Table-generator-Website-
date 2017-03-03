<?php 
$mysqli=new mysqli('localhost','root','','pro');
$email=$_POST["username"];
//$email=$_POST["emailsignup"];
$password=$_POST["password"];

  
$sql="SELECT *FROM register WHERE emailsignup='$email' AND passwordsignup='$password'";
// WHERE emailsignup='".$email."')";
$result=mysqli_query($mysqli,$sql);
if($result->num_rows>0)
{
	while($row=$result->fetch_assoc()){
	//this displays the mail ids
	//echo "email".$row["emailsignup"];
		echo "success, valid user";
}
}
else
{
	echo "lol";
}
?>