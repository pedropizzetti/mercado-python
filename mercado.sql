-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 26, 2026 at 05:12 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mercado`
--

-- --------------------------------------------------------

--
-- Table structure for table `itens_venda`
--

CREATE TABLE `itens_venda` (
  `id` int(11) NOT NULL,
  `id_venda` int(11) NOT NULL,
  `id_produto` int(11) NOT NULL,
  `quantidade` int(11) DEFAULT NULL,
  `preco_unitario` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `itens_venda`
--

INSERT INTO `itens_venda` (`id`, `id_venda`, `id_produto`, `quantidade`, `preco_unitario`) VALUES
(1, 1, 1, 2, 4.68),
(2, 2, 5, 3, 1.68),
(3, 3, 3, 2, 21.48),
(4, 4, 2, 3, 14.00),
(5, 5, 4, 2, 1.28),
(6, 6, 1, 4, 4.68),
(7, 7, 3, 4, 21.48),
(8, 8, 2, 4, 14.00),
(9, 9, 2, 6, 14.00),
(10, 10, 11, 2, 10.78),
(11, 11, 3, 5, 21.48),
(12, 12, 30, 6, 4.98),
(13, 13, 4, 2, 1.28),
(14, 14, 2, 6, 14.00);

-- --------------------------------------------------------

--
-- Table structure for table `produtos`
--

CREATE TABLE `produtos` (
  `id_produto` int(11) NOT NULL,
  `nome` varchar(100) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `preco_custo` decimal(10,2) DEFAULT NULL,
  `preco_venda` decimal(10,2) DEFAULT NULL,
  `estoque` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `produtos`
--

INSERT INTO `produtos` (`id_produto`, `nome`, `categoria`, `preco_custo`, `preco_venda`, `estoque`) VALUES
(1, 'Açúcar Refinado Especial (1kg)', 'Alimentos', 2.00, 4.68, 23),
(2, 'Arroz Parboilizado Tipo 1 (5kg)', 'Alimentos', 7.00, 14.00, 33),
(3, 'Detergente Sanitário Gel Adesivo (38g)', 'Limpeza', 12.00, 21.48, 42),
(4, 'Água Mineral Natural sem Gás (510ml)', 'Bebidas', 0.47, 1.28, 29),
(5, 'Hambúrguer de Carne de Frango e Bovina (56g)', 'Congelados', 0.80, 1.68, 68),
(6, 'Azeite de Oliva Extra Virgem (500ml)', 'Óleos e Condimentos', 18.00, 35.00, 35),
(7, 'Uva Mista sem Semente (500g)', 'Hortifruti', 4.00, 10.98, 3),
(8, 'Torta Frango e Requeijão (500g)', 'Congelados', 13.00, 22.98, 7),
(9, 'Água Mineral com Gás (510ml)', 'Bebidas', 0.40, 1.38, 67),
(10, 'Pão de Forma Tradicional (390g)', 'Mercearia', 3.90, 7.98, 32),
(11, 'Morango Orgânico (250g)', 'Hortifruti', 4.00, 10.78, 10),
(12, 'Leite Integral (1L)', 'Laticínios', 3.20, 5.98, 45),
(13, 'Queijo Mussarela (200g)', 'Laticínios', 4.50, 9.90, 28),
(14, 'Iogurte Natural (170g)', 'Laticínios', 1.80, 3.99, 52),
(15, 'Refrigerante Cola (2L)', 'Bebidas', 4.20, 8.49, 36),
(16, 'Suco de Laranja Natural (1L)', 'Bebidas', 5.00, 9.98, 20),
(17, 'Café Torrado e Moído (500g)', 'Mercearia', 8.00, 16.90, 33),
(18, 'Macarrão Espaguete (500g)', 'Mercearia', 2.20, 4.89, 60),
(19, 'Molho de Tomate Tradicional (340g)', 'Mercearia', 1.50, 3.79, 48),
(20, 'Sabonete Neutro (90g)', 'Higiene', 1.10, 2.99, 75),
(21, 'Shampoo Anticaspa (350ml)', 'Higiene', 6.50, 14.90, 22),
(22, 'Papel Higiênico (4 rolos)', 'Higiene', 4.80, 10.98, 40),
(23, 'Desinfetante Lavanda (1L)', 'Limpeza', 2.90, 6.49, 37),
(24, 'Esponja Multiuso (3un)', 'Limpeza', 1.20, 3.49, 64),
(25, 'Amaciante de Roupas (2L)', 'Limpeza', 7.50, 15.98, 18),
(26, 'Batata Congelada (1kg)', 'Congelados', 6.00, 13.98, 26),
(27, 'Pizza Calabresa Congelada', 'Congelados', 9.00, 18.99, 14),
(28, 'Banana Prata (1kg)', 'Hortifruti', 2.80, 5.99, 50),
(29, 'Tomate Italiano (1kg)', 'Hortifruti', 3.50, 7.49, 34),
(30, 'Cenoura (1kg)', 'Hortifruti', 2.10, 4.98, 23),
(31, 'Chocolate ao Leite (90g)', 'Doces', 2.50, 5.99, 55),
(32, 'Ração para Cães Adultos (1kg)', 'Pet Shop', 8.00, 16.90, 20),
(33, 'Ração para Gatos (500g)', 'Pet Shop', 4.50, 9.98, 25),
(34, 'Biscoito para Cachorro (300g)', 'Pet Shop', 3.20, 7.49, 18),
(35, 'Areia Sanitária para Gatos (2kg)', 'Pet Shop', 6.50, 13.90, 15),
(36, 'Sachê para Gatos (85g)', 'Pet Shop', 1.20, 2.99, 40);

-- --------------------------------------------------------

--
-- Table structure for table `vendas`
--

CREATE TABLE `vendas` (
  `id_venda` int(11) NOT NULL,
  `data_venda` datetime DEFAULT NULL,
  `valor_total` decimal(10,2) DEFAULT NULL,
  `metodo_pagamento` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `vendas`
--

INSERT INTO `vendas` (`id_venda`, `data_venda`, `valor_total`, `metodo_pagamento`) VALUES
(1, '2026-03-24 11:22:56', 9.36, 'Dinheiro'),
(2, '2026-03-25 00:01:16', 5.04, 'Dinheiro'),
(3, '2026-03-25 00:20:03', 42.96, 'Dinheiro'),
(4, '2026-03-25 00:20:15', 42.00, 'Dinheiro'),
(5, '2026-03-25 00:20:32', 2.56, 'Dinheiro'),
(6, '2026-03-25 00:20:40', 18.72, 'Dinheiro'),
(7, '2026-03-25 00:35:43', 85.92, 'Crédito'),
(8, '2026-03-25 10:45:06', 56.00, 'Débito'),
(9, '2026-03-25 11:10:28', 84.00, 'Pix'),
(10, '2026-03-25 11:45:06', 21.56, 'Crédito'),
(11, '2026-03-25 14:38:32', 107.40, 'Débito'),
(12, '2026-03-25 15:56:59', 29.88, 'Crédito'),
(13, '2026-03-25 16:38:11', 2.56, 'Crédito'),
(14, '2026-03-25 16:58:14', 84.00, 'Pix');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `itens_venda`
--
ALTER TABLE `itens_venda`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_venda` (`id_venda`),
  ADD KEY `id_produto` (`id_produto`);

--
-- Indexes for table `produtos`
--
ALTER TABLE `produtos`
  ADD PRIMARY KEY (`id_produto`);

--
-- Indexes for table `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`id_venda`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `itens_venda`
--
ALTER TABLE `itens_venda`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `produtos`
--
ALTER TABLE `produtos`
  MODIFY `id_produto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `vendas`
--
ALTER TABLE `vendas`
  MODIFY `id_venda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `itens_venda`
--
ALTER TABLE `itens_venda`
  ADD CONSTRAINT `itens_venda_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `vendas` (`id_venda`),
  ADD CONSTRAINT `itens_venda_ibfk_2` FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id_produto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
