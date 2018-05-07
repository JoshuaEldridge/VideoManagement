<?php

require('/usr/local/lib/php/Smarty/Smarty.class.php');

$smarty = new Smarty();

$smarty->setTemplateDir('smarty/templates');
$smarty->setCompileDir('smarty/templates_c');
$smarty->setCacheDir('smarty/cache');
$smarty->setConfigDir('smarty/configs');

include 'adodb5/adodb.inc.php';

/*
* This is the driver you have selected to use
*/
$driver = 'sqlite3';
 
$db = newAdoConnection($driver);
 
/*
* These are the parameters required to connect to the database see connect()
*/
 
$db->connect('home-video.db','','','');

$sql = "select *
        from source_videos v order by s_filename";
        
$source_videos = $db->getAll($sql);
// print_r($source_videos);

$smarty->assign('source_videos', $source_videos);

$smarty->display('index.tpl');

?>