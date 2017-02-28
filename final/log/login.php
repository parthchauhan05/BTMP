<?php
if(!empty($_POST['user']) && !empty($_POST['password'])){
	$user=$_POST['user'];
	$pass=$_POST['password'];
	$url = "139.59.29.224:5612/login?user=$user";
$ch = curl_init();
curl_setopt($ch,CURLOPT_URL,$url);
curl_setopt($ch,CURLOPT_RETURNTRANSFER,1);
curl_setopt($ch,CURLOPT_CONNECTTIMEOUT, 4);
// get_file_content(Url);
$json = curl_exec($ch);
if(!$json) {
    echo curl_error($ch);
}
curl_close($ch);
$rps=json_decode($json);
//print_r(json_decode($json));
if(empty($rps)){
	echo 'Wrong usrname or Password';
}
else{
	if($user==$rps->_id && $pass==$rps->Password){
		$name=$rps->Name;
		echo 'Welcome '.$name.'';
	}else{
		echo 'Wrong usrname or Password';	
	}
	}}
	else
		echo 'Please Enter Username or Password';

?>