-- MySQL Administrator dump 1.4
--
-- ------------------------------------------------------
-- Server version	5.1.73-community


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


--
-- Create schema awaaz
--

-- CREATE DATABASE IF NOT EXISTS awaaz;
USE aawaz;

--
-- Definition of table `analytics_app_open`
--

CREATE TABLE `analytics_app_open` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `even_tid` varchar(45) DEFAULT NULL,
  `user_id` varchar(45) NOT NULL,
  `app_open` varchar(45) NOT NULL,
  `app_platform` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_app_open`
--

/*!40000 ALTER TABLE `analytics_app_open` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_app_open` ENABLE KEYS */;


--
-- Definition of table `analytics_device_detail`
--

CREATE TABLE `analytics_device_detail` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) DEFAULT NULL,
  `app_id` varchar(45) NOT NULL,
  `version_code` varchar(45) NOT NULL,
  `version_name` varchar(45) NOT NULL,
  `device_name` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `board` varchar(45) NOT NULL DEFAULT '',
  `brand` varchar(45) NOT NULL DEFAULT '',
  `device` varchar(45) NOT NULL DEFAULT '',
  `hardware` varchar(45) NOT NULL DEFAULT '',
  `manufacturer` varchar(45) NOT NULL DEFAULT '',
  `model` varchar(45) NOT NULL DEFAULT '',
  `time` varchar(45) NOT NULL DEFAULT '0',
  `sdk_int` varchar(45) NOT NULL DEFAULT '0',
  `os_built_release_version` varchar(45) NOT NULL DEFAULT '',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_device_detail`
--

/*!40000 ALTER TABLE `analytics_device_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_device_detail` ENABLE KEYS */;


--
-- Definition of table `analytics_fast_fwd`
--

CREATE TABLE `analytics_fast_fwd` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) DEFAULT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL DEFAULT '',
  `show_id` varchar(45) NOT NULL DEFAULT '0',
  `episode_id` varchar(45) NOT NULL DEFAULT '0',
  `start_time` varchar(45) NOT NULL DEFAULT '00:00:00',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_fast_fwd`
--

/*!40000 ALTER TABLE `analytics_fast_fwd` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_fast_fwd` ENABLE KEYS */;


--
-- Definition of table `analytics_next`
--

CREATE TABLE `analytics_next` (
  `datetime` varchar(45) NOT NULL,
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL,
  `show_id` varchar(45) NOT NULL,
  `episode_id` varchar(45) NOT NULL,
  `start_time` varchar(45) NOT NULL,
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_next`
--

/*!40000 ALTER TABLE `analytics_next` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_next` ENABLE KEYS */;


--
-- Definition of table `analytics_pause`
--

CREATE TABLE `analytics_pause` (
  `datet_ime` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL DEFAULT '',
  `show_id` varchar(45) NOT NULL DEFAULT '0',
  `episode_id` varchar(45) NOT NULL DEFAULT '0',
  `pause_time` varchar(45) NOT NULL DEFAULT '00:00:00',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_pause`
--

/*!40000 ALTER TABLE `analytics_pause` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_pause` ENABLE KEYS */;


--
-- Definition of table `analytics_play`
--

CREATE TABLE `analytics_play` (
  `datetime` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `eventid` varchar(45) NOT NULL DEFAULT '0',
  `userid` varchar(45) NOT NULL DEFAULT '',
  `platform` varchar(45) NOT NULL DEFAULT '',
  `showid` varchar(45) NOT NULL DEFAULT '0',
  `episodeid` varchar(45) NOT NULL DEFAULT '0',
  `starttime` varchar(45) NOT NULL DEFAULT '00:00:00',
  `appplatform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_play`
--

/*!40000 ALTER TABLE `analytics_play` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_play` ENABLE KEYS */;


--
-- Definition of table `analytics_previous`
--

CREATE TABLE `analytics_previous` (
  `datet_ime` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL DEFAULT '',
  `show_id` varchar(45) NOT NULL DEFAULT '0',
  `episode_id` varchar(45) NOT NULL DEFAULT '0',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_previous`
--

/*!40000 ALTER TABLE `analytics_previous` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_previous` ENABLE KEYS */;


--
-- Definition of table `analytics_rewind`
--

CREATE TABLE `analytics_rewind` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL DEFAULT '',
  `show_id` varchar(45) NOT NULL DEFAULT '0',
  `episode_id` varchar(45) NOT NULL DEFAULT '0',
  `start_time` varchar(45) NOT NULL DEFAULT '00:00:00',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_rewind`
--

/*!40000 ALTER TABLE `analytics_rewind` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_rewind` ENABLE KEYS */;


--
-- Definition of table `analytics_search`
--

CREATE TABLE `analytics_search` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `query` varchar(145) NOT NULL DEFAULT '',
  `no_of_show_count` varchar(45) NOT NULL DEFAULT '0',
  `show_ids` varchar(45) NOT NULL DEFAULT '',
  `no_of_article_count` varchar(45) NOT NULL DEFAULT '0',
  `article_ids` varchar(45) NOT NULL DEFAULT '',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_search`
--

/*!40000 ALTER TABLE `analytics_search` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_search` ENABLE KEYS */;


--
-- Definition of table `analytics_stop`
--

CREATE TABLE `analytics_stop` (
  `date_time` varchar(45) NOT NULL DEFAULT '0000-00-00 00:00:00',
  `event_id` varchar(45) NOT NULL,
  `user_id` varchar(45) NOT NULL,
  `platform` varchar(45) NOT NULL DEFAULT '',
  `show_id` varchar(45) NOT NULL DEFAULT '0',
  `episode_id` varchar(45) NOT NULL DEFAULT '0',
  `time` varchar(45) NOT NULL DEFAULT '00:00:00',
  `app_platform` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `analytics_stop`
--

/*!40000 ALTER TABLE `analytics_stop` DISABLE KEYS */;
/*!40000 ALTER TABLE `analytics_stop` ENABLE KEYS */;


--
-- Definition of table `logging_insert_stats`
--

CREATE TABLE `logging_insert_stats` (
  `date_time` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `file_path` varchar(200) NOT NULL,
  `event_total_data` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `logging_insert_stats`
--

/*!40000 ALTER TABLE `logging_insert_stats` DISABLE KEYS */;
/*!40000 ALTER TABLE `logging_insert_stats` ENABLE KEYS */;




/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
