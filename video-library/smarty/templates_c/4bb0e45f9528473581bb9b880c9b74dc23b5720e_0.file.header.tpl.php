<?php
/* Smarty version 3.1.32, created on 2018-05-07 20:54:49
  from '/Users/161619/Sites/video-library/smarty/templates/header.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.32',
  'unifunc' => 'content_5af0bd19af1618_19702692',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '4bb0e45f9528473581bb9b880c9b74dc23b5720e' => 
    array (
      0 => '/Users/161619/Sites/video-library/smarty/templates/header.tpl',
      1 => 1525726487,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_5af0bd19af1618_19702692 (Smarty_Internal_Template $_smarty_tpl) {
?><!DOCTYPE html>
<html>
<head>
  <title><?php echo (($tmp = @$_smarty_tpl->tpl_vars['title']->value)===null||$tmp==='' ? "My Home Video" : $tmp);?>
</title>
  <link href="video-library.css" rel="stylesheet" type="text/css">
  <link href="video-js/video-js.css" rel="stylesheet" type="text/css">
  <?php echo '<script'; ?>
 src="video-js/video.js"><?php echo '</script'; ?>
>
  <?php echo '<script'; ?>
>
    videojs.options.flash.swf = "video-js/video-js.swf";
  <?php echo '</script'; ?>
>
    <?php echo '<script'; ?>
>
    function scrubVideo(t) {
        var t = t + 0.1
        var myPlayer = videojs('example_video_1');
        if(myPlayer.paused()) {
            myPlayer.currentTime(t)
            myPlayer.play()
        } else {
            myPlayer.currentTime(t)
        }
    }
    <?php echo '</script'; ?>
>
</head><?php }
}
