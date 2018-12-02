-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2018 at 04:55 AM
-- Server version: 10.1.37-MariaDB
-- PHP Version: 7.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `Author` varchar(100) NOT NULL,
  `ISBN13` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `author`
--

INSERT INTO `author` (`Author`, `ISBN13`) VALUES
('Alan Moore', '9781603090001'),
('Alice Walker', '9780156028356'),
('Campbell Whyte', '9781603094122'),
('Carson McCullers', '9780618526413'),
('Charles Dickens', '9780199536245'),
('Christian Slade', '9781603090100'),
('Edith Wharton', '9780486298030'),
('Edward Morgan Forster', '9780141182131'),
('Emily Dickinson', '9780674018242'),
('Erich Maria Remarque', '9780449213940'),
('Ernest Hemingway', '9780684843322'),
('F. Scott Fitzgerald', '9781906230746'),
('Flannery O\'Connor', '9780374515362'),
('Herman Melville', '9781853260087'),
('Jack Kerouac', '9780140283297'),
('James Joyce', '9780141181264'),
('James Joyce', '9783518455944'),
('Jason E. Zinza', '9781881133209'),
('Joseph Conrad', '9780486264646'),
('Junot Daz', '9781594483295'),
('Kazuo Ishiguro', '9781400078776'),
('Marguerite Yourcenar', '9780374529260'),
('Mario Puzo', '9780345476722'),
('Michael Beschloss', '9780307409607'),
('Miguel de Cervantes', '9780486821955'),
('Moliere', '9781417931361'),
('Ray Bradbury', '9781451673319'),
('Stephen Crane', '9780486264653'),
('Troy Little', '9781603093750'),
('Vladimir Vladimirovich Nabokov', '9780679723165'),
('William Butler Yeats', '9780684807317');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`Author`,`ISBN13`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
