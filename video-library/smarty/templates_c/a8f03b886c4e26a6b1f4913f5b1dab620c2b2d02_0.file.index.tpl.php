<?php
/* Smarty version 3.1.32, created on 2018-05-07 21:08:08
  from '/Users/161619/Sites/video-library/smarty/templates/index.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.32',
  'unifunc' => 'content_5af0c038722e66_35507285',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'a8f03b886c4e26a6b1f4913f5b1dab620c2b2d02' => 
    array (
      0 => '/Users/161619/Sites/video-library/smarty/templates/index.tpl',
      1 => 1525727286,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
    'file:header.tpl' => 1,
  ),
),false)) {
function content_5af0c038722e66_35507285 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_checkPlugins(array(0=>array('file'=>'/usr/local/lib/php/Smarty/plugins/modifier.date_format.php','function'=>'smarty_modifier_date_format',),1=>array('file'=>'/usr/local/lib/php/Smarty/plugins/modifier.filesize.php','function'=>'smarty_modifier_filesize',),));
$_smarty_tpl->_subTemplateRender("file:header.tpl", $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, 0, $_smarty_tpl->cache_lifetime, array('title'=>"Video Index Page"), 0, false);
?>

<body>

<?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['source_videos']->value, 'video');
if ($_from !== null) {
foreach ($_from as $_smarty_tpl->tpl_vars['video']->value) {
?>
<div class="video-info">
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_md5'];?>
<br>
    <a href="video.php?source_id=<?php echo $_smarty_tpl->tpl_vars['video']->value['source_id'];?>
"><?php echo $_smarty_tpl->tpl_vars['video']->value['s_filename'];?>
</a><br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_codec_name'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_codec_long'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_codec_tag'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_codec_tag_string'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_width'];?>
 x <?php echo $_smarty_tpl->tpl_vars['video']->value['s_height'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_format'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_format_long'];?>
<br>
    <?php echo smarty_modifier_date_format($_smarty_tpl->tpl_vars['video']->value['s_duration'],"%H:%M:%S");?>
<br>
    <?php echo smarty_modifier_filesize($_smarty_tpl->tpl_vars['video']->value['s_size']);?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_bit_rate'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_timecode'];?>
<br>
    <?php echo smarty_modifier_date_format($_smarty_tpl->tpl_vars['video']->value['s_creation_time'],"%b %d, %Y");?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_year'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_month'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_day'];?>
<br>
    <?php echo $_smarty_tpl->tpl_vars['video']->value['s_archive'];?>
<br>
</div>
<?php
}
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>

</body>
</html><?php }
}
