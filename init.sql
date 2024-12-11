CREATE USER medoune WITH PASSWORD 'password123';
CREATE DATABASE userpd;
GRANT ALL PRIVILEGES ON DATABASE userpd TO medoune;

\c userpd;

GRANT ALL PRIVILEGES ON SCHEMA public TO medoune;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO medoune;

-- Création des tables basées sur vos modèles
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE
);

-- Création d'une fonction pour mettre à jour la colonne `updated_at`
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = CURRENT_TIMESTAMP;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Création du trigger pour la table `products`
CREATE TRIGGER set_updated_at
BEFORE UPDATE ON products
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();

-- Insertion de données dans la table categories
INSERT INTO categories (name) 
VALUES 
('Category 1'),
('Category 2');

-- Insertion de données dans la table products
INSERT INTO products (name, description, price, category_id) 
VALUES 
('Product 1', 'Description for Product 1', 10.00, 1),
('Product 2', 'Description for Product 2', 20.00, 1),
('Product 3', 'Description for Product 3', 15.00, 2),
('Product 4', 'Description for Product 4', 25.00, 2);
