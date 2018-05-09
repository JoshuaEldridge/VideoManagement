<?php
// video_source.class.php

class source_video {

    function __construct() {
    
    }
    
    function update_video_fields($db, $fields) {
        $this->load($fields);
        $table = 'source_videos';
        $db->autoExecute($table, $this, 'UPDATE', 'source_id = ' . $this->source_id);
    }

    function load_video_from_db($db, $source_id) {
        $fields = $db->getRow("select * from source_videos where source_id = ?", array($source_id));
        $this->load($fields);
    }

    function load($fields) {
    // Fields can come from the database or from a request object
        foreach ($fields as $k=>$v) {
            $this->$k = $v;
        }
    }

    function get_video() {
        return $this;
    }

}

?>