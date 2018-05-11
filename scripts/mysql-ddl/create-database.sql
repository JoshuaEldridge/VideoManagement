DROP DATABASE IF EXISTS video_library;
CREATE DATABASE video_library;
USE  video_library;
DROP TABLE IF EXISTS source_videos;
CREATE TABLE source_videos (
    source_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    s_md5 CHAR(32),
    s_filename VARCHAR(255),
    s_codec_name VARCHAR(35),
    s_codec_long VARCHAR(255),
    s_codec_type VARCHAR(25),
    s_codec_tag CHAR(10),
    s_codec_tag_string VARCHAR(25),
    s_width SMALLINT UNSIGNED,
    s_height SMALLINT UNSIGNED,
    s_format VARCHAR(75),
    s_format_long VARCHAR(255),
    s_duration DECIMAL(11, 6),
    s_size BIGINT UNSIGNED,
    s_bit_rate INT UNSIGNED,
    s_timecode TIME,
    s_creation_time TIMESTAMP,
    s_year SMALLINT UNSIGNED,
    s_month TINYINT UNSIGNED,
    s_day TINYINT UNSIGNED,
    s_archive_flag BOOLEAN,
    s_camera_name VARCHAR(55),
    s_scene_id_poster INTEGER UNSIGNED,
    s_active_flag BOOLEAN,
    PRIMARY KEY (source_id)
);