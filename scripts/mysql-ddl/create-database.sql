DROP DATABASE IF EXISTS video_library;
CREATE DATABASE video_library;
USE  video_library;
DROP TABLE IF EXISTS videos;
CREATE TABLE videos (
    video_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    md5 CHAR(32),
    filename VARCHAR(255),
    codec_name VARCHAR(35),
    codec_long VARCHAR(255),
    codec_type VARCHAR(25),
    codec_tag CHAR(10),
    codec_tag_string VARCHAR(25),
    width SMALLINT UNSIGNED,
    height SMALLINT UNSIGNED,
    format VARCHAR(75),
    format_long VARCHAR(255),
    duration DECIMAL(11, 6),
    size BIGINT UNSIGNED,
    bit_rate INT UNSIGNED,
    timecode CHAR(11),
    creation_time TIMESTAMP,
    year SMALLINT UNSIGNED,
    month TINYINT UNSIGNED,
    day TINYINT UNSIGNED,
    archive_flag BOOLEAN,
    camera_name VARCHAR(55),
    scene_id_poster INTEGER UNSIGNED,
    active_flag BOOLEAN,
    original_source_flag BOOLEAN,
    long_description TEXT,
    PRIMARY KEY (video_id)
);
drop table scenes;
CREATE TABLE scenes (
    scene_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    video_id INTEGER UNSIGNED NOT NULL,
    active_flag BOOLEAN,
    image_name VARCHAR(125),
    ts DECIMAL(11, 6),
    description TINYTEXT,
    PRIMARY KEY (scene_id)
);