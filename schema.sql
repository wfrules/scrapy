/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.17-log : Database - res
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`res` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `res`;

/*Table structure for table `admin_menu` */

DROP TABLE IF EXISTS `admin_menu`;

CREATE TABLE `admin_menu` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) NOT NULL DEFAULT '0',
  `order` int(11) NOT NULL DEFAULT '0',
  `title` varchar(50) NOT NULL,
  `icon` varchar(50) NOT NULL,
  `uri` varchar(50) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Table structure for table `admin_operation_log` */

DROP TABLE IF EXISTS `admin_operation_log`;

CREATE TABLE `admin_operation_log` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `method` varchar(10) NOT NULL,
  `ip` varchar(15) NOT NULL,
  `input` text NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_operation_log_user_id_index` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8;

/*Table structure for table `admin_permissions` */

DROP TABLE IF EXISTS `admin_permissions`;

CREATE TABLE `admin_permissions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `http_method` varchar(255) DEFAULT NULL,
  `http_path` text,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_permissions_name_unique` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

/*Table structure for table `admin_role_menu` */

DROP TABLE IF EXISTS `admin_role_menu`;

CREATE TABLE `admin_role_menu` (
  `role_id` int(11) NOT NULL,
  `menu_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  KEY `admin_role_menu_role_id_menu_id_index` (`role_id`,`menu_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `admin_role_permissions` */

DROP TABLE IF EXISTS `admin_role_permissions`;

CREATE TABLE `admin_role_permissions` (
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  KEY `admin_role_permissions_role_id_permission_id_index` (`role_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `admin_role_users` */

DROP TABLE IF EXISTS `admin_role_users`;

CREATE TABLE `admin_role_users` (
  `role_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  KEY `admin_role_users_role_id_user_id_index` (`role_id`,`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `admin_roles` */

DROP TABLE IF EXISTS `admin_roles`;

CREATE TABLE `admin_roles` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_roles_name_unique` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `admin_user_permissions` */

DROP TABLE IF EXISTS `admin_user_permissions`;

CREATE TABLE `admin_user_permissions` (
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  KEY `admin_user_permissions_user_id_permission_id_index` (`user_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `admin_users` */

DROP TABLE IF EXISTS `admin_users`;

CREATE TABLE `admin_users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(190) NOT NULL,
  `password` varchar(60) NOT NULL,
  `name` varchar(255) NOT NULL,
  `avatar` varchar(255) DEFAULT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_users_username_unique` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `author` */

DROP TABLE IF EXISTS `author`;

CREATE TABLE `author` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `aname` varchar(100) DEFAULT '' COMMENT '姓名',
  PRIMARY KEY (`id`),
  UNIQUE KEY `aname` (`aname`)
) ENGINE=InnoDB AUTO_INCREMENT=3679 DEFAULT CHARSET=utf8;

/*Table structure for table `author_link` */

DROP TABLE IF EXISTS `author_link`;

CREATE TABLE `author_link` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `author_id` bigint(20) DEFAULT NULL COMMENT 'author.id',
  `site_id` int(4) DEFAULT NULL COMMENT '网站id',
  `url` varchar(500) DEFAULT '' COMMENT '网址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3689 DEFAULT CHARSET=utf8;

/*Table structure for table `migrations` */

DROP TABLE IF EXISTS `migrations`;

CREATE TABLE `migrations` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

/*Table structure for table `password_resets` */

DROP TABLE IF EXISTS `password_resets`;

CREATE TABLE `password_resets` (
  `email` varchar(255) NOT NULL,
  `token` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  KEY `password_resets_email_index` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `users_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `speed` int(10) DEFAULT '0' COMMENT '速度',
  `quest_at` timestamp NULL DEFAULT NULL COMMENT '提问时间',
  `submit_at` timestamp NULL DEFAULT NULL COMMENT '提交时间',
  `played` int(11) DEFAULT '0' COMMENT '播放次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=200 DEFAULT CHARSET=utf8;

/*Table structure for table `questions_detail` */

DROP TABLE IF EXISTS `questions_detail`;

CREATE TABLE `questions_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `questions_id` int(10) DEFAULT '0',
  `content` int(10) NOT NULL DEFAULT '0',
  `answer` int(10) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1195 DEFAULT CHARSET=utf8;

/*Table structure for table `site` */

DROP TABLE IF EXISTS `site`;

CREATE TABLE `site` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `sname` varchar(100) DEFAULT '' COMMENT '站点名',
  `url` varchar(1000) DEFAULT '' COMMENT '站点网址',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `song` */

DROP TABLE IF EXISTS `song`;

CREATE TABLE `song` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `sname` varchar(100) DEFAULT '' COMMENT '姓名',
  `author_id` bigint(20) DEFAULT '0' COMMENT '作者author.id',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3345 DEFAULT CHARSET=utf8;

/*Table structure for table `tab` */

DROP TABLE IF EXISTS `tab`;

CREATE TABLE `tab` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '修改时间',
  `song_id` bigint(20) DEFAULT NULL COMMENT 'song.id',
  `url` varchar(1000) DEFAULT '' COMMENT '来源网址',
  `site_id` bigint(20) DEFAULT '0' COMMENT 'site.id',
  `ttype` tinyint(1) DEFAULT '0' COMMENT '0 未知 1文本 2 图片 3 gtp 4 html',
  `content` mediumtext COMMENT '内容',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1248 DEFAULT CHARSET=utf8;

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `remember_token` varchar(100) DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT NULL,
  `updated_at` timestamp NULL DEFAULT NULL,
  `api_token` varchar(100) NOT NULL,
  `speed` int(11) NOT NULL DEFAULT '80',
  `quest_len` int(10) DEFAULT '6' COMMENT '问题长度',
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_email_unique` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Table structure for table `vods` */

DROP TABLE IF EXISTS `vods`;

CREATE TABLE `vods` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(300) DEFAULT '' COMMENT '标题',
  `pic` varchar(500) DEFAULT '' COMMENT '预览图',
  `pageurl` varchar(500) DEFAULT '' COMMENT '详情页',
  `vodurl` varchar(500) DEFAULT '' COMMENT '视频地址',
  `pic_path` varchar(500) DEFAULT '' COMMENT '文件位置',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=122 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
