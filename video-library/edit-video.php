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
$process = htmlspecialchars($_GET["submit"]);
$edit = htmlspecialchars($_GET["edit"]);

/*
* Set up the database connection
*/
$driver = 'sqlite3';
$db = newAdoConnection($driver);
$db->connect('home-video.db','','','');
$db->debug = True;

if(isset($process)) {
// Insert updated data
}

if(isset($edit) && isset($source_id)) {
    $video_scenes = $db->getRow("select * from source_scenes where source_id = ? order by scene_ts", array($source_id));
    $video_fields = $db->getRow("select * from source_videos where source_id = ?", array($source_id));
    $smarty->assign('video_fields', $video_fields);
    $smarty->assign('video_scenes', $video_scenes);
    print_r($video_fields);
}


$video_filename = str_replace('.mov', '.mp4', $video_filename);
$folder_name = substr($video_filename, 0, -4);


// print_r($static_images);

$smarty->assign('source_id', $source_id);
$smarty->assign('folder_name', $folder);
$smarty->display('edit-video.tpl');

?>