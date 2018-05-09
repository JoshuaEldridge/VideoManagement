<?php

require('/usr/local/lib/php/Smarty/Smarty.class.php');

include 'adodb5/adodb.inc.php';
$ADODB_FETCH_MODE = ADODB_FETCH_ASSOC;

require_once('classes/video_source.class.php');

$smarty = new Smarty();

$smarty->setTemplateDir('smarty/templates');
$smarty->setCompileDir('smarty/templates_c');
$smarty->setCacheDir('smarty/cache');
$smarty->setConfigDir('smarty/configs');


$source_id = htmlspecialchars($_GET["source_id"]);
$process = htmlspecialchars($_GET["submit"]);

/*
* Set up the database connection
*/
$driver = 'sqlite3';
$db = newAdoConnection($driver);
$db->connect('home-video.db','','','');
$db->debug = True;

if(isset($process) && isset($source_id)) {
    // $video_scenes = $db->getRow("select * from source_scenes where source_id = ? order by scene_ts", array($source_id));
    // $video_fields = $db->getRow("select * from source_videos where source_id = ?", array($source_id));
//     $video_fields = new source_video();
//     $video_fields->update_video_fields($db, $_REQUEST);
//     $video_fields->get_video();
//     $smarty->assign('video_fields', $video_fields->get_video());
//     $smarty->assign('video_scenes', $video_scenes);
//     print_r($video_fields);
// 
//     extract($_REQUEST);
//     echo $source_id;
//     echo $s_filename;
// 
//     foreach($_REQUEST as $k=>$v) {
//         print $k . ":" . $v . "<br>\n";
//     }

// } elseif (isset($source_id)) {
    $video_fields = new source_video();
    $video_fields->load_video_from_db($db, $source_id);
//     $video_fields->get_video();
    print_r(get_object_vars($video_fields));
    $smarty->assign('video_fields', $video_fields->get_video());
}


$video_filename = str_replace('.mov', '.mp4', $video_filename);
$folder_name = substr($video_filename, 0, -4);


// print_r($static_images);

$smarty->assign('source_id', $source_id);
$smarty->assign('folder_name', $folder);
$smarty->display('edit-video.tpl');

?>