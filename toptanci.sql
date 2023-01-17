-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 21 Haz 2020, 15:41:13
-- Sunucu sürümü: 10.1.38-MariaDB
-- PHP Sürümü: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `toptanci`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `admin_adi` varchar(25) COLLATE utf8mb4_turkish_ci NOT NULL,
  `sifre` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `admin`
--

INSERT INTO `admin` (`id`, `admin_adi`, `sifre`) VALUES
(1, 'dilan', 123456);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `kullaniciler`
--

CREATE TABLE `kullaniciler` (
  `id` int(11) NOT NULL,
  `kullanici_adi` varchar(50) COLLATE utf8mb4_turkish_ci NOT NULL,
  `adi` varchar(50) COLLATE utf8mb4_turkish_ci NOT NULL,
  `soyadi` varchar(50) COLLATE utf8mb4_turkish_ci NOT NULL,
  `e_posta` varchar(100) COLLATE utf8mb4_turkish_ci NOT NULL,
  `adres` text COLLATE utf8mb4_turkish_ci NOT NULL,
  `ülke` varchar(50) COLLATE utf8mb4_turkish_ci NOT NULL,
  `sehir` varchar(50) COLLATE utf8mb4_turkish_ci NOT NULL,
  `posta_kodu` int(11) NOT NULL,
  `sifre` int(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `kullaniciler`
--

INSERT INTO `kullaniciler` (`id`, `kullanici_adi`, `adi`, `soyadi`, `e_posta`, `adres`, `ülke`, `sehir`, `posta_kodu`, `sifre`) VALUES
(1, 'bulakdilann', 'dilan', 'bulak', 'dilan.bulak1999@gmail.com', 'fatih mahallesi', 'Türkiye', 'İstanbul', 1075, 123456),
(2, 'EMREB', 'emre', 'bulak', 'emre_bulak@gmail.com', 'esenyurt', 'Türkiye', 'İstanbul', 341510, 7845),
(3, 'DURUU', 'Duru', 'Karakaya', 'duru@gmail.com', 'talatpaşa mahallesi 810 sokak no 63', 'Türkiye', 'Ankara', 385222, 1234);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `sikayet`
--

CREATE TABLE `sikayet` (
  `id` int(11) NOT NULL,
  `kullanici_id` int(11) DEFAULT NULL,
  `sikayeti` text COLLATE utf8mb4_turkish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `sikayet`
--

INSERT INTO `sikayet` (`id`, `kullanici_id`, `sikayeti`) VALUES
(1, 1, 'Aldığım ürün bozuk çıktı'),
(2, 3, 'Ürün teslim edilmedi');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `siparisler`
--

CREATE TABLE `siparisler` (
  `id` int(11) NOT NULL,
  `kullanici_id` int(11) NOT NULL,
  `urunler_id` int(11) NOT NULL,
  `siparis_tarihi` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `adet` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `siparisler`
--

INSERT INTO `siparisler` (`id`, `kullanici_id`, `urunler_id`, `siparis_tarihi`, `adet`) VALUES
(1, 1, 1, '2020-06-19 18:32:24', 5);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `urunler`
--

CREATE TABLE `urunler` (
  `id` int(11) NOT NULL,
  `urun_kodu` varchar(25) COLLATE utf8mb4_turkish_ci NOT NULL,
  `urun_adi` varchar(100) COLLATE utf8mb4_turkish_ci NOT NULL,
  `urun_fiyati` float NOT NULL,
  `stok_sayisi` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_turkish_ci;

--
-- Tablo döküm verisi `urunler`
--

INSERT INTO `urunler` (`id`, `urun_kodu`, `urun_adi`, `urun_fiyati`, `stok_sayisi`) VALUES
(1, 'M1', 'Makarna', 2, 250),
(2, 'S1', 'Soda', 3, 300),
(3, 'K1', 'Kola', 5, 500),
(4, 'KM1', 'Konserve Mısır', 3, 200),
(5, 'PN1', 'PEYNİR', 12, 500),
(6, 'SB1', 'Sabun', 2, 600);

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `kullaniciler`
--
ALTER TABLE `kullaniciler`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `sikayet`
--
ALTER TABLE `sikayet`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `siparisler`
--
ALTER TABLE `siparisler`
  ADD PRIMARY KEY (`id`);

--
-- Tablo için indeksler `urunler`
--
ALTER TABLE `urunler`
  ADD PRIMARY KEY (`id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `kullaniciler`
--
ALTER TABLE `kullaniciler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Tablo için AUTO_INCREMENT değeri `sikayet`
--
ALTER TABLE `sikayet`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Tablo için AUTO_INCREMENT değeri `siparisler`
--
ALTER TABLE `siparisler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Tablo için AUTO_INCREMENT değeri `urunler`
--
ALTER TABLE `urunler`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
