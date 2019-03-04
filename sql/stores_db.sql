-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 04-03-2019 a las 01:37:57
-- Versión del servidor: 10.1.36-MariaDB
-- Versión de PHP: 7.2.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_sge`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `almacen1`
--

CREATE TABLE `storage1` (
  `code` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `descripcion` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `storage1`
--

INSERT INTO `storage1` (`code`, `quantity`, `descripcion`) VALUES
('A0001', '10', 'INTEL I7'),
('A0002', '15', 'RAM 16GB'),
('A0003', '22', 'SDD 512GB'),
('A0004', '8', 'NVIDIA'),
('A0005', '5', 'INTEL I5'),
('A0006', '10', 'RAM 8GB'),
('A0007', '6', 'SSD 256GB'),
('A0008', '3', 'SSD 1TB'),
('A0009', '12', 'AMD'),
('A0010', '19', 'PANTALLA RETINA'),
('A0011', '3', 'RAM 32');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `storage2`
--

CREATE TABLE `storage2` (
  `code` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `quantity` decimal(10,0) DEFAULT NULL,
  `descripcion` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `storage2`
--

INSERT INTO `storage2` (`code`, `quantity`, `descripcion`) VALUES
('B0001', '0', 'PC GAMER'),
('B0002', '0', 'PC WORKSTATION'),
('B0003', '0', 'MAC PRO'),
('B0004', '0', 'IMAC');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reference_table`
--

CREATE TABLE `reference_table` (
  `C2` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `C1` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `quantity` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `reference_table`
--

INSERT INTO `reference_table` (`C2`, `C1`, `quantity`) VALUES
('B0001', 'A0001', '1'),
('B0001', 'A0002', '2'),
('B0001', 'A0003', '1'),
('B0001', 'A0004', '1'),
('B0002', 'A0005', '1'),
('B0002', 'A0006', '2'),
('B0002', 'A0007', '1'),
('B0003', 'A0005', '1'),
('B0003', 'A0006', '2'),
('B0003', 'A0007', '1'),
('B0003', 'A0010', '1'),
('B0003', 'A0009', '1'),
('B0004', 'A0001', '1'),
('B0004', 'A0011', '2'),
('B0004', 'A0003', '2'),
('B0004', 'A0009', '2');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `movement`
--

CREATE TABLE `movement` (
  `cod_movement` double NOT NULL,
  `date_movement` date DEFAULT NULL,
  `c2` varchar(10) COLLATE latin1_spanish_ci DEFAULT NULL,
  `quantity` decimal(10,0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `storage1`
--
ALTER TABLE `storage1`
  ADD PRIMARY KEY (`code`);

--
-- Indices de la tabla `storage2`
--
ALTER TABLE `storage2`
  ADD PRIMARY KEY (`code`);

--
-- Indices de la tabla `reference_table`
--
ALTER TABLE `reference_table`
  ADD PRIMARY KEY (`C2`,`C1`),
  ADD KEY `C1` (`C1`);

--
-- Indices de la tabla `movement`
--
ALTER TABLE `movement`
  ADD UNIQUE KEY `cod_movement` (`cod_movement`),
  ADD KEY `c2` (`c2`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `movement`
--
ALTER TABLE `movement`
  MODIFY `cod_movement` double NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `reference_table`
--
ALTER TABLE `reference_table`
  ADD CONSTRAINT `reference_table_ibfk_1` FOREIGN KEY (`C1`) REFERENCES `storage1` (`code`),
  ADD CONSTRAINT `reference_table_ibfk_2` FOREIGN KEY (`C2`) REFERENCES `storage2` (`code`);

--
-- Filtros para la tabla `movement`
--
ALTER TABLE `movement`
  ADD CONSTRAINT `movement_ibfk_1` FOREIGN KEY (`c2`) REFERENCES `storage2` (`code`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
