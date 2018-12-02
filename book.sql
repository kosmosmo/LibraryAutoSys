-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2018 at 04:50 AM
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

--
-- Dumping data for table `book`
--

INSERT INTO `book` (`ISBN13`, `Title`, `Author`, `Publisher`, `Language`, `Year`, `Count`) VALUES
('9780140283297', 'On The Road', 'Jack Kerouac', 'Penguin Group USA', 'en', '1955', 0),
('9780141181264', 'Finnegans Wake', 'James Joyce', 'Penguin', 'en', '1999', 0),
('9780141182131', 'Howards End', 'Edward Morgan Forster', 'Penguin', 'en', '2000', 0),
('9780156028356', 'The Color Purple', 'Alice Walker', 'Houghton Mifflin Harcourt', 'en', '1982', 0),
('9780199536245', 'The Pickwick Papers', 'Charles Dickens', 'Oxford Paperbacks', 'en', '2008', 0),
('9780307409607', 'Presidents Of War', 'Michael Beschloss', 'Crown', 'en', '2018', 19),
('9780345476722', 'The Fortunate Pilgrim', 'Mario Puzo', 'Ballantine Books', 'en', '2004', 28),
('9780374515362', 'The Complete Stories', 'Flannery O\'Connor', 'Macmillan', 'en', '1971', 0),
('9780374529260', 'Memoirs Of Hadrian', 'Marguerite Yourcenar', 'Macmillan', 'en', '2005', 0),
('9780449213940', 'All Quiet On The Western Front', 'Erich Maria Remarque', 'All Quiet On The Western Front', 'en', '1982', 0),
('9780486264646', 'Heart Of Darkness', 'Joseph Conrad', 'Courier Corporation', 'en', '1902', 6),
('9780486264653', 'The Red Badge Of Courage', 'Stephen Crane', 'Courier Corporation', 'en', '1990', 0),
('9780486298030', 'The Age Of Innocence', 'Edith Wharton', 'Courier Corporation', 'en', '1997', 0),
('9780486821955', 'Don Quixote', 'Miguel de Cervantes', 'Courier Dover Publications', 'en', '2018', 3),
('9780618526413', 'The Heart Is A Lonely Hunter', 'Carson McCullers', 'Houghton Mifflin Harcourt', 'en', '2004', 7),
('9780674018242', 'The Poems Of Emily Dickinson', 'Emily Dickinson', 'Belknap Press', 'en', '2005', 0),
('9780679723165', 'Lolita', 'Vladimir Vladimirovich Nabokov', 'Vintage Books', 'en', '1997', 8),
('9780684807317', 'The Collected Works Of W.B. Yeats Volume I: The Poems', 'William Butler Yeats', 'Scribner', 'en', '1996', 0),
('9780684843322', 'The Complete Short Stories Of Ernest Hemingway', 'Ernest Hemingway', 'Scribner', 'en', '1998', 0),
('9781400078776', 'Never Let Me Go', 'Kazuo Ishiguro', 'Vintage', 'en', '2006', 7),
('9781417931361', 'The Would Be Gentleman', 'Moliere', 'Kessinger Publishing', 'en', '2005', 0),
('9781451673319', 'Fahrenheit 451', 'Ray Bradbury', 'Simon and Schuster', 'en', '2012', 0),
('9781594483295', 'The Brief Wondrous Life Of Oscar Wao', 'Junot Daz', 'Penguin', 'en', '2008', 0),
('9781603090001', 'League Of Extraordinary Gentlemen', 'Alan Moore', 'League Of Extraordinary Gentlemen', 'en', '2009', 1),
('9781603090100', 'Korgi', 'Christian Slade', 'Top Shelf Productions', 'en', '2008', 6),
('9781603093750', 'Hunter S. Thompson\'s Fear And Loathing In Las Vegas', 'Troy Little', 'Idw - Top Shelf', 'en', '2015', 2),
('9781603094122', 'Home Time (Book One)', 'Campbell Whyte', 'Home Time', 'en', '2017', 18),
('9781853260087', 'Moby Dick', 'Herman Melville', 'Wordsworth Editions', 'en', '1992', 8),
('9781881133209', 'Master American Sign Language!', 'Jason E. Zinza', 'Sign Media Incorporated', 'en', '2006', 10),
('9781906230746', 'The Great Gatsby', 'F. Scott Fitzgerald', 'Real Reads Limited', 'en', '2014', 6),
('9783518455944', 'Ulysses. Sonderausgabe', 'James Joyce', 'Ulysses. Sonderausgabe', 'en', '2004', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `book`
--
ALTER TABLE `book`
  ADD PRIMARY KEY (`ISBN13`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
