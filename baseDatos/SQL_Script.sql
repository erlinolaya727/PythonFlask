--
-- File generated with SQLiteStudio v3.3.3 on mié. jul. 20 01:05:23 2022
--
-- Text encoding used: UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: Calificacion_Habitacion
DROP TABLE IF EXISTS Calificacion_Habitacion;
CREATE TABLE `Calificacion_Habitacion` (
  `idCalificacion_Habitacion` INT NOT NULL,
  `calificacion` INT NULL,
  `comentario` VARCHAR(45) NULL,
  `Habitaciones_idHabitaciones` INT NOT NULL,
  PRIMARY KEY (`idCalificacion_Habitacion`, `Habitaciones_idHabitaciones`));

-- Table: Estado_Disponibilidad
DROP TABLE IF EXISTS Estado_Disponibilidad;
CREATE TABLE `Estado_Disponibilidad` (
  `idEstado_Habitacion` INT NOT NULL,
  `estado` VARCHAR(45) NULL,
  PRIMARY KEY (`idEstado_Habitacion`));

-- Table: Estado_Usuario
DROP TABLE IF EXISTS Estado_Usuario;
CREATE TABLE `Estado_Usuario` (
  `idEstado_Usuario` INT NOT NULL,
  `nombre_estado` VARCHAR(45) NULL,
  PRIMARY KEY (`idEstado_Usuario`));

-- Table: Habitaciones
DROP TABLE IF EXISTS Habitaciones;
CREATE TABLE `Habitaciones` (
  `idHabitaciones` INT NOT NULL,
  `Usuarios_cedula` VARCHAR(45) NOT NULL,
  `tamano` VARCHAR(45) NULL,
  `costo` VARCHAR(45) NULL,
  `Estado_Disponibilidad` INT NOT NULL,
  PRIMARY KEY (`idHabitaciones`, `Usuarios_cedula`, `Estado_Disponibilidad`));

-- Table: Reservas
DROP TABLE IF EXISTS Reservas;
CREATE TABLE `Reservas` (
  `idReservas` INT NOT NULL,
  `Usuarios_cedula` VARCHAR(45) NOT NULL,
  `Habitaciones_idHabitaciones` INT NOT NULL,
  `fecha_inicio` VARCHAR(45) NULL,
  `fecha_fin` VARCHAR(45) NULL,
  `costo_total` VARCHAR(45) NULL,
  PRIMARY KEY (`idReservas`, `Usuarios_cedula`, `Habitaciones_idHabitaciones`));

-- Table: roles
DROP TABLE IF EXISTS roles;
CREATE TABLE `roles` (
  `idroles` INT NOT NULL,
  `nombre_rol` VARCHAR(45) NULL,
  PRIMARY KEY (`idroles`));

-- Table: Usuarios
DROP TABLE IF EXISTS Usuarios;
CREATE TABLE `Usuarios` (
  `idUsuarios` INT NOT NULL,
  `cedula` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NULL,
  `ciudad` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `roles_idrol` INT NOT NULL,
  `Estado_idEstadoUsuario` INT NOT NULL,
  PRIMARY KEY (`cedula`, `roles_idrol`, `Estado_idEstadoUsuario`));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
