-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 17, 2023 at 07:22 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `librarydata`
--

-- --------------------------------------------------------

--
-- Table structure for table `library`
--

CREATE TABLE `library` (
  `Member` varchar(48) DEFAULT NULL,
  `PRN_No` varchar(48) DEFAULT NULL,
  `ID` int(12) NOT NULL,
  `FirstName` varchar(48) DEFAULT NULL,
  `LAstName` varchar(48) DEFAULT NULL,
  `Adress1` text NOT NULL,
  `Adress2` text NOT NULL,
  `PostCode` int(12) NOT NULL,
  `Mobile` int(10) DEFAULT NULL,
  `Book_Id` int(10) NOT NULL,
  `Book_Tittle` varchar(48) NOT NULL,
  `Author` varchar(48) NOT NULL,
  `Date_Borrowed` date NOT NULL,
  `Date_Due` date NOT NULL,
  `Days_On_Book` int(11) DEFAULT NULL,
  `Late_Return_fee` float NOT NULL,
  `DateOverDue` date NOT NULL,
  `Final_Price` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `library`
--

INSERT INTO `library` (`Member`, `PRN_No`, `ID`, `FirstName`, `LAstName`, `Adress1`, `Adress2`, `PostCode`, `Mobile`, `Book_Id`, `Book_Tittle`, `Author`, `Date_Borrowed`, `Date_Due`, `Days_On_Book`, `Late_Return_fee`, `DateOverDue`, `Final_Price`) VALUES
('Student', '3467348', 1234, 'Mohd', 'Sajid', 'UP', 'Bly', 243205, 2147483647, 0, 'Make Web', 'James', '2023-02-22', '2023-03-09', 15, 50, '0000-00-00', 890),
('Student', '5234', 2345, 'Mohd ', 'Asif', 'UP', 'Bly', 243205, 2147483647, 0, 'Make Web', 'James', '2023-02-22', '2023-03-09', 15, 0, '0000-00-00', 0),
('Teacher', '9485878', 23343, 'Sam', 'Jarry', 'Bly', 'Bly', 243201, 897447747, 1124, 'To build an AI', 'Andy Smith', '2023-05-17', '2023-06-01', 15, 50, '0000-00-00', 670),
('Teacher', '47835789', 53436, 'abc', 'def', 'delhi', 'new delhi', 110025, 2147483647, 1126, 'To build an AI', 'Kris Starlet', '2023-02-22', '2023-03-09', 15, 50, '0000-00-00', 400),
('Student', '9767876', 56767, 'uguhg', 'hjjl', 'iupo', 'kjkj', 8767, 2147483647, 11249, 'Basic Computer Language', 'MK Jordan', '2023-02-26', '2023-03-13', 15, 50, '0000-00-00', 1050),
('Student', '76347', 95784, 'Ahmaz', 'Ahmad', 'UP', 'Bly', 36546, 2147483647, 364087, 'The Ghost', 'Richa Misra', '2023-02-22', '2023-03-09', 15, 50, '0000-00-00', 780),
('Teacher', '4365787', 475647, 'JJ', 'Steve', 'USA', 'USA', 657439, 2147483647, 1125, 'Human and Machine', 'JJ Thomson', '2023-02-23', '2023-03-10', 15, 50, '0000-00-00', 550);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `library`
--
ALTER TABLE `library`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `ID` (`ID`,`PRN_No`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `library`
--
ALTER TABLE `library`
  MODIFY `ID` int(12) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=475648;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
