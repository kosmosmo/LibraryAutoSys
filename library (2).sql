SET time_zone = "+00:00";

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;


CREATE TABLE `author` (
  `Author` varchar(100) NOT NULL,
  `ISBN13` varchar(13) NOT NULL
) ;

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

CREATE TABLE `book` (
  `ISBN13` varchar(13) NOT NULL,
  `Title` varchar(100) DEFAULT NULL,
  `Author` varchar(100) DEFAULT NULL,
  `Publisher` varchar(100) DEFAULT NULL,
  `Language` varchar(4) DEFAULT NULL,
  `Year` varchar(4) DEFAULT NULL,
  `Count` int(11) NOT NULL
) ;

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

CREATE TABLE `branch` (
  `branch` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL
) ;

INSERT INTO `branch` (`branch`, `address`) VALUES
('0Flushing', 'Queens,NewYork'),
('Bikini Bottom', 'Underwater pineapple'),
('Gotham City', 'New Jersey'),
('Neverland', 'Your imagination'),
('South Park', 'Rocky Mountains of central Colorado'),
('Wonderful World', 'Land of OZ');

CREATE TABLE `copy` (
  `ISBN13` varchar(13) NOT NULL,
  `Copy` varchar(3) NOT NULL,
  `ReturnDate` varchar(100) DEFAULT NULL,
  `BorrowID` varchar(100) DEFAULT NULL,
  `ReserveID` varchar(100) DEFAULT NULL
) ;

INSERT INTO `copy` (`ISBN13`, `Copy`, `ReturnDate`, `BorrowID`, `ReserveID`) VALUES
('9780140283297', '001', NULL, NULL, NULL),
('9780141181264', '001', NULL, NULL, NULL),
('9780141182131', '001', NULL, NULL, NULL),
('9780156028356', '001', NULL, NULL, NULL),
('9780199536245', '001', NULL, NULL, NULL),
('9780307409607', '001', NULL, NULL, NULL),
('9780345476722', '001', NULL, NULL, NULL),
('9780345476722', '002', NULL, NULL, NULL),
('9780374515362', '001', NULL, NULL, NULL),
('9780374529260', '001', NULL, NULL, NULL),
('9780449213940', '001', NULL, NULL, NULL),
('9780486264646', '001', NULL, NULL, NULL),
('9780486264653', '001', NULL, NULL, NULL),
('9780486298030', '001', NULL, NULL, NULL),
('9780486821955', '001', NULL, NULL, NULL),
('9780618526413', '001', NULL, NULL, NULL),
('9780674018242', '001', NULL, NULL, NULL),
('9780679723165', '001', NULL, NULL, NULL),
('9780684807317', '001', NULL, NULL, NULL),
('9780684843322', '001', NULL, NULL, NULL),
('9781400078776', '001', NULL, NULL, NULL),
('9781417931361', '001', NULL, NULL, NULL),
('9781417931361', '002', NULL, NULL, NULL),
('9781451673319', '001', NULL, NULL, NULL),
('9781594483295', '001', NULL, NULL, NULL),
('9781603090001', '001', NULL, NULL, NULL),
('9781603090100', '001', NULL, NULL, NULL),
('9781603093750', '001', NULL, NULL, NULL),
('9781603094122', '001', NULL, NULL, NULL),
('9781853260087', '001', NULL, NULL, NULL),
('9781881133209', '001', NULL, NULL, NULL),
('9781906230746', '001', NULL, NULL, NULL),
('9783518455944', '001', NULL, NULL, NULL),
('9783518455944', '002', NULL, NULL, NULL),
('9783518455944', '003', NULL, NULL, NULL);

CREATE TABLE `reader` (
  `Id` varchar(7) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone` varchar(10) NOT NULL,
  `Count` int(11) NOT NULL DEFAULT '0',
  `Balance` int(11) NOT NULL DEFAULT '0'
) ;

INSERT INTO `reader` (`Id`, `Name`, `Address`, `Phone`, `Count`, `Balance`) VALUES
('0980485', 'Jun Chen', 'Flushing', '3473999999', 43, 200),
('0980486', 'Pewdiepie', 'Internet', '3473991234', 35, 520),
('0980487', 'Jackie Chen', 'Hollywood', '3473994321', 2, 0),
('0980488', 'Bruce Wayne', 'Gotham City', '8888888888', 2, 0),
('0980489', 'Peter Pan', 'Neverland', '3471234567', 10, 0),
('0980490', 'Gordon Ramsay', 'United Kingdom', '3471230000', 0, 0),
('0980491', 'Darth Vader', 'Death Star', '4444444444', 0, 0),
('0980492', 'Bugs Bunny', 'Rabbit Hole', '8907659876', 0, 0),
('0980494', 'Justin Bieber', 'Canada', '8999999999', 0, 0),
('0980495', 'Harry Potter', 'Hogwarts School', '9874563579', 0, 0),
('0980496', 'James Bond', 'Bond\'s places', '0070070007', 0, 0),
('0980497', 'Jack Sparrow', 'Boat', '9638521547', 0, 0),
('0980498', 'Mickey Mouse', 'Disney World', '8523699658', 11, 0),
('0980499', 'Logan Paul', 'Los Angeles', '8521323659', 0, 0),
('0980500', 'Jake Paul', 'Los Angeles', '8521323658', 5, 0),
('0980501', 'Ed Sheeran', 'Castle on the Hill', '8521329876', 7, 0),
('0980502', 'Winnie Pooh', 'Honey Jar', '8520988888', 0, 0),
('0980503', 'Dora', 'Mexico', '3450988888', 0, 0),
('0980504', 'Diego', 'Mexico Jungle', '3330988888', 0, 0),
('0980505', 'Pikachu', 'Pokemon Center', '0010020005', 0, 0),
('0980506', 'Dwayne Johnson', 'Gym', '8523647410', 0, 0),
('0980507', 'SpongeBob', 'Underwater', '4598710934', 0, 0),
('0980508', 'Billy Herrington', 'Long Island', '0097786666', 0, 0),
('0980509', 'Unicorn', 'Rainbow', '3333333338', 0, 0),
('0980510', 'Koki', 'Magic Forest', '9876667777', 0, 0);

CREATE TABLE `readerborrow` (
  `Id` varchar(7) NOT NULL,
  `ISBN13` varchar(13) NOT NULL,
  `Copy` varchar(3) NOT NULL
) ;

CREATE TABLE `readerreserve` (
  `Id` varchar(7) NOT NULL,
  `ISBN13` varchar(13) NOT NULL,
  `Reid` varchar(100) NOT NULL,
  `Inhold` tinyint(1) NOT NULL DEFAULT '0'
) ;


ALTER TABLE `author`
  ADD PRIMARY KEY (`Author`,`ISBN13`);

ALTER TABLE `book`
  ADD PRIMARY KEY (`ISBN13`);

ALTER TABLE `branch`
  ADD PRIMARY KEY (`branch`);

ALTER TABLE `copy`
  ADD PRIMARY KEY (`ISBN13`,`Copy`);

ALTER TABLE `reader`
  ADD PRIMARY KEY (`Id`);

ALTER TABLE `readerborrow`
  ADD PRIMARY KEY (`Id`,`ISBN13`,`Copy`);

ALTER TABLE `readerreserve`
  ADD PRIMARY KEY (`Id`,`ISBN13`,`Reid`);


ALTER TABLE `copy`
  ADD CONSTRAINT `copy_ibfk_1` FOREIGN KEY (`ISBN13`) REFERENCES `book` (`ISBN13`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
