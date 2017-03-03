

<?php
if(isset($_POST['submit']))
{
	$mysqli=new mysqli('localhost','root','','pro');
	$usernamesignup=$_POST["usernamesignup"];
	$passwordsignup=$_POST["passwordsignup"];
	$emailsignup=$_POST["emailsignup"];
	
//	$query="insert into register values('$usernamesignup','$passwordsignup','$emailsignup');";
	
	if(mysqli_query($mysqli,"insert into register values('$usernamesignup','$passwordsignup','$emailsignup')"))
	{
	echo "success";
	header("location:index.html");
	}
	else
	{
	echo "failed";
	header("location:a href:'#index.html'");
	}
	
}
?>
