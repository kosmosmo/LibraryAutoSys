-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2018 at 04:39 AM
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
-- Database: `library2`
--

-- --------------------------------------------------------

--
-- Table structure for table `author`
--

CREATE TABLE `author` (
  `Author` varchar(100) NOT NULL,
  `ISBN13` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `book`
--

CREATE TABLE `book` (
  `ISBN13` varchar(13) NOT NULL,
  `Title` varchar(100) DEFAULT NULL,
  `Author` varchar(100) DEFAULT NULL,
  `Publisher` varchar(100) DEFAULT NULL,
  `Language` varchar(4) DEFAULT NULL,
  `Year` varchar(4) DEFAULT NULL,
  `Count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `copy`
--

CREATE TABLE `copy` (
  `ISBN13` varchar(13) NOT NULL,
  `Copy` varchar(3) NOT NULL,
  `ReturnDate` varchar(100) DEFAULT NULL,
  `BorrowID` varchar(100) DEFAULT NULL,
  `ReserveID` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `reader`
--

CREATE TABLE `reader` (
  `Id` varchar(7) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Count` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reader`
--

INSERT INTO `reader` (`Id`, `Name`, `Address`, `Phone`, `Count`) VALUES
('0980485', 'Jun Chen', 'Flushing', '3473999999', 0),
('0980486', 'Pewdiepie', 'Internet', '3473991234', 5),
('0980487', 'Jackie Chen', 'Hollywood', '3473994321', 0),
('0980488', 'Bruce Wayne', 'Gotham City', '8888888888', 0),
('0980489', 'Peter Pan', 'Neverland', '3471234567', 0),
('0980490', 'Gordon Ramsay', 'United Kingdom', '3471230000', 0),
('0980491', 'Darth Vader', 'Death Star', '4444444444', 0),
('0980492', 'Bugs Bunny', 'Rabbit Hole', '8907659876', 0),
('0980494', 'Justin Bieber', 'Canada', '8999999999', 0),
('0980495', 'Harry Potter', 'Hogwarts School', '9874563579', 0),
('0980496', 'James Bond', 'Bond\'s places', '0070070007', 0),
('0980497', 'Jack Sparrow', 'Boat', '9638521547', 0),
('0980498', 'Mickey Mouse', 'Disney World', '8523699658', 0),
('0980499', 'Logan Paul', 'Los Angeles', '8521323659', 0),
('0980500', 'Jake Paul', 'Los Angeles', '8521323658', 0),
('0980501', 'Ed Sheeran', 'Castle on the Hill', '8521329876', 0),
('0980502', 'Winnie Pooh', 'Honey Jar', '8520988888', 0),
('0980503', 'Dora', 'Mexico', '3450988888', 0),
('0980504', 'Diego', 'Mexico Jungle', '3330988888', 0),
('0980505', 'Pikachu', 'Pokemon Center', '0010020005', 0),
('0980506', 'Dwayne Johnson', 'Gym', '8523647410', 0),
('0980507', 'SpongeBob', 'Underwater', '4598710934', 0),
('0980508', 'Billy Herrington', 'Long Island', '0097786666', 0),
('0980509', 'Unicorn', 'Rainbow', '3333333338', 0);

-- --------------------------------------------------------

--
-- Table structure for table `readerborrow`
--

CREATE TABLE `readerborrow` (
  `Id` varchar(7) NOT NULL,
  `ISBN13` varchar(13) NOT NULL,
  `Copy` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `readerreserve`
--

CREATE TABLE `readerreserve` (
  `Id` varchar(7) NOT NULL,
  `ISBN13` varchar(13) NOT NULL,
  `Reid` varchar(100) NOT NULL,
  `Inhold` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `author`
--
ALTER TABLE `author`
  ADD PRIMARY KEY (`Author`);

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`ISBN13`);

--
-- Indexes for table `copy`
--
ALTER TABLE `copy`
  ADD PRIMARY KEY (`ISBN13`,`Copy`);

--
-- Indexes for table `reader`
--
ALTER TABLE `reader`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `readerborrow`
--
ALTER TABLE `readerborrow`
  ADD PRIMARY KEY (`Id`,`ISBN13`,`Copy`);

--
-- Indexes for table `readerreserve`
--
ALTER TABLE `readerreserve`
  ADD PRIMARY KEY (`Id`,`ISBN13`,`Reid`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `copy`
--
ALTER TABLE `copy`
  ADD CONSTRAINT `copy_ibfk_1` FOREIGN KEY (`ISBN13`) REFERENCES `book` (`ISBN13`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
