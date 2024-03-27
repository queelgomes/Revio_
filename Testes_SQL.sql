-- Endereço dos CLientes
SELECT name, street FROM customers WHERE city = 'Porto Alegre'

-- Maior e Menor Preço
SELECT MAX(price), MIN(price) FROM products;

-- Pessoas Juridicas
SELECT name FROM customers WHERE id IN (SELECT id_customers FROM legal_person);

-- Filmes em Promoção
SELECT id, name FROM movies WHERE id_prices in (SELECT id FROM prices WHERE value < 2.00)

-- Quantidades Entre 10 e 20
SELECT name FROM product WHERE amount BETWEEN 10 AND 20 AND id_providers in (SELECT id FROM providers WHERE name LIKE "P%")

-- Representantes Executivos
SELECT prod.name, prov.name FROM products as prod, providers as prov WHERE prod.id_providers = prov.id AND prod.id_categories = 6
