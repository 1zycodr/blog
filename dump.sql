-- MySQL dump 10.13  Distrib 5.7.33, for Linux (x86_64)
--
-- Host: localhost    Database: blog
-- ------------------------------------------------------
-- Server version	5.7.33-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog_user`
--

DROP TABLE IF EXISTS `blog_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creation_date` datetime DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(25) NOT NULL,
  `password` varchar(50) NOT NULL,
  `profile_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_profile_id` (`profile_id`),
  CONSTRAINT `fk_profile_id` FOREIGN KEY (`profile_id`) REFERENCES `profile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_user`
--

LOCK TABLES `blog_user` WRITE;
/*!40000 ALTER TABLE `blog_user` DISABLE KEYS */;
INSERT INTO `blog_user` VALUES (10,'2021-04-01 20:26:27','username','password',1),(11,'2021-04-07 19:52:42','marvin','12345678',3),(12,'2021-04-07 19:55:31','vanya','12345678',4),(13,'2021-04-14 19:06:44','username_','password',5);
/*!40000 ALTER TABLE `blog_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `creation_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` int(11) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `blog_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile`
--

DROP TABLE IF EXISTS `profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(30) DEFAULT NULL,
  `second_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(30) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile`
--

LOCK TABLES `profile` WRITE;
/*!40000 ALTER TABLE `profile` DISABLE KEYS */;
INSERT INTO `profile` VALUES (1,'Marvin','None','None',NULL),(2,'Marvin','None','None',NULL),(3,'amirlan','None','None',NULL),(4,'Marvin','None','None',NULL),(5,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `profile` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-14 19:49:16
