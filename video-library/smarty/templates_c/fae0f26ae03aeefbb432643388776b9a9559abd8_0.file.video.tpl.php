<?php
/* Smarty version 3.1.32, created on 2018-05-07 20:02:16
  from '/Users/161619/Sites/video-library/smarty/templates/video.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.32',
  'unifunc' => 'content_5af0b0c838a199_96500792',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'fae0f26ae03aeefbb432643388776b9a9559abd8' => 
    array (
      0 => '/Users/161619/Sites/video-library/smarty/templates/video.tpl',
      1 => 1525723333,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
  ),
),false)) {
function content_5af0b0c838a199_96500792 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_subTemplateRender("file:header.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('title'=>"Video Detail Page"), 0, false);
?>

<body>

<div class="main-container">
  <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="418" height="320"
      inactivityTimeout=0
      poster="images/<?php echo $_smarty_tpl->tpl_vars['folder']->value;?>
/<?php echo $_smarty_tpl->tpl_vars['folder']->value;?>
-000.png"
      data-setup='{ "inactivityTimeout": 0 }'>
    <source src="videos/<?php echo $_smarty_tpl->tpl_vars['video_filename']->value;?>
" type='video/mp4' />
    <p class="vjs-no-js">To view this video please enable JavaScript, and consider upgrading to a web browser that <a href="http://videojs.com/html5-video-support/" target="_blank">supports HTML5 video</a></p>
  </video>

<?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['static_images']->value, 'image');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['image']->value) {
?>
    <a href="#" onclick="scrubVideo(<?php echo $_smarty_tpl->tpl_vars['image']->value['scene_ts'];?>
)"><img src="images/<?php echo $_smarty_tpl->tpl_vars['folder']->value;?>
/<?php echo $_smarty_tpl->tpl_vars['image']->value['scene_image'];?>
" width="75"></a>
<?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
</div>

<!-- 
879.412746
907.507508
924.991658
936.403070
984.317651
1011.144478
1018.785452
1037.604271
1074.841508
1098.832165
1115.081748
1116.449783
1124.891558
1141.007674
1151.918585
1165.231899
1196.763430
 -->

</body>
</html>
<?php }
}
