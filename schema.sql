/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.17-log : Database - vods
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`vods` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `vods`;

/*Table structure for table `vods` */

DROP TABLE IF EXISTS `vods`;

CREATE TABLE `vods` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(300) DEFAULT '' COMMENT '标题',
  `pic` varchar(500) DEFAULT '' COMMENT '预览图',
  `pageurl` varchar(500) DEFAULT '' COMMENT '详情页',
  `vodurl` varchar(500) DEFAULT '' COMMENT '视频地址',
  `pic_path` varchar(500) DEFAULT '' COMMENT '图片文件路径',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=505 DEFAULT CHARSET=utf8;

/*Table structure for table `vods_bak` */

DROP TABLE IF EXISTS `vods_bak`;

CREATE TABLE `vods_bak` (
  `id` bigint(20) NOT NULL DEFAULT '0' COMMENT 'id',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `title` varchar(300) DEFAULT '' COMMENT '标题',
  `pic` varchar(500) DEFAULT '' COMMENT '预览图',
  `pageurl` varchar(500) DEFAULT '' COMMENT '详情页',
  `vodurl` varchar(500) DEFAULT '' COMMENT '视频地址',
  `pic_path` varchar(500) DEFAULT '' COMMENT '图片文件路径'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
