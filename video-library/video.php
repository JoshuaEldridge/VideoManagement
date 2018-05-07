<?php

require('/usr/local/lib/php/Smarty/Smarty.class.php');
include 'adodb5/adodb.inc.php';
$ADODB_FETCH_MODE = ADODB_FETCH_ASSOC;

$smarty = new Smarty();

$smarty->setTemplateDir('smarty/templates');
$smarty->setCompileDir('smarty/templates_c');
$smarty->setCacheDir('smarty/cache');
$smarty->setConfigDir('smarty/configs');


$source_id = htmlspecialchars($_GET["source_id"]);

/*
* This is the driver you have selected to use
*/
$driver = 'sqlite3';
 
$db = newAdoConnection($driver);

/*
* These are the parameters required to connect to the database see connect()
*/
 
$db->connect('home-video.db','','','');

$video_filename = $db->getOne("select s_filename from source_videos where source_id = ?", array($source_id));

$video_filename = str_replace('.mov', '.mp4', $video_filename);

$folder = substr($video_filename, 0, -4);

$static_images = $db->getAll("select scene_image, scene_ts from source_scenes where source_id = ? order by scene_ts", array($source_id));

// print_r($static_images);

$smarty->assign('source_id', $source_id);
$smarty->assign('folder', $folder);
$smarty->assign('video_filename', $video_filename);
$smarty->assign('static_images', $static_images);
$smarty->display('video.tpl');

?>