-- 🌾 Création des tables pour AgroConnect sur Supabase (VERSION CORRIGÉE)
-- Exécuter ce script dans le SQL Editor de Supabase

-- =====================================
-- 📋 TABLE DES UTILISATEURS
-- =====================================
CREATE TABLE IF NOT EXISTS users_user (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    email VARCHAR(254) UNIQUE NOT NULL,
    password VARCHAR(128) NOT NULL,
    role VARCHAR(50) DEFAULT 'buyer' CHECK (role IN ('admin', 'farmer', 'buyer', 'seller')),
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    phone VARCHAR(20),
    address TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 📦 TABLE DES PRODUITS
-- =====================================
CREATE TABLE IF NOT EXISTS products_product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    category VARCHAR(50) CHECK (category IN ('cereals', 'vegetables', 'fruits', 'legumes', 'tubers', 'other')),
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER DEFAULT 0,
    image VARCHAR(255),
    farmer_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 🛒 TABLE DES COMMANDES
-- =====================================
CREATE TABLE IF NOT EXISTS products_order (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES products_product(id) ON DELETE CASCADE,
    quantity INTEGER DEFAULT 1,
    buyer_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    status VARCHAR(50) DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled')),
    image VARCHAR(255),
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 🛗 TABLE DU PANIER
-- =====================================
CREATE TABLE IF NOT EXISTS products_cart (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products_product(id) ON DELETE CASCADE,
    quantity INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 💬 TABLE DES MESSAGES
-- =====================================
CREATE TABLE IF NOT EXISTS products_message (
    id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    receiver_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 💡 TABLE DES CONSEILS AGRICOLES
-- =====================================
CREATE TABLE IF NOT EXISTS products_agriculturaladvice (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    advice_type VARCHAR(50) CHECK (advice_type IN ('planting', 'fertilization', 'harvesting', 'protection', 'irrigation')),
    crop_type VARCHAR(50) CHECK (crop_type IN ('cereals', 'vegetables', 'fruits', 'legumes', 'tubers', 'other')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 🌾 TABLE DES CULTURES
-- =====================================
CREATE TABLE IF NOT EXISTS products_culture (
    id SERIAL PRIMARY KEY,
    farmer_id INTEGER REFERENCES users_user(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    crop_type VARCHAR(50) CHECK (crop_type IN ('cereals', 'vegetables', 'fruits', 'legumes', 'tubers', 'other')),
    planting_date DATE NOT NULL,
    expected_harvest DATE,
    area DECIMAL(10, 2) CHECK (area > 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================
-- 📊 INDEX POUR LES PERFORMANCES
-- =====================================

-- Index pour les utilisateurs
CREATE INDEX IF NOT EXISTS idx_users_email ON users_user(email);
CREATE INDEX IF NOT EXISTS idx_users_username ON users_user(username);
CREATE INDEX IF NOT EXISTS idx_users_role ON users_user(role);

-- Index pour les produits
CREATE INDEX IF NOT EXISTS idx_products_farmer ON products_product(farmer_id);
CREATE INDEX IF NOT EXISTS idx_products_category ON products_product(category);
CREATE INDEX IF NOT EXISTS idx_products_created_at ON products_product(created_at);

-- Index pour les commandes
CREATE INDEX IF NOT EXISTS idx_orders_buyer ON products_order(buyer_id);
CREATE INDEX IF NOT EXISTS idx_orders_status ON products_order(status);
CREATE INDEX IF NOT EXISTS idx_orders_date ON products_order(order_date);

-- Index pour les messages
CREATE INDEX IF NOT EXISTS idx_messages_sender ON products_message(sender_id);
CREATE INDEX IF NOT EXISTS idx_messages_receiver ON products_message(receiver_id);
CREATE INDEX IF NOT EXISTS idx_messages_timestamp ON products_message(timestamp);

-- Index pour les conseils
CREATE INDEX IF NOT EXISTS idx_advice_type ON products_agriculturaladvice(advice_type);
CREATE INDEX IF NOT EXISTS idx_advice_crop ON products_agriculturaladvice(crop_type);

-- Index pour les cultures
CREATE INDEX IF NOT EXISTS idx_cultures_farmer ON products_culture(farmer_id);
CREATE INDEX IF NOT EXISTS idx_cultures_crop ON products_culture(crop_type);

-- =====================================
-- 🔐 RLS (ROW LEVEL SECURITY) - SÉCURITÉ
-- =====================================

-- Activer RLS sur toutes les tables
ALTER TABLE users_user ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_product ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_order ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_cart ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_message ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_agriculturaladvice ENABLE ROW LEVEL SECURITY;
ALTER TABLE products_culture ENABLE ROW LEVEL SECURITY;

-- Politiques RLS pour les utilisateurs
CREATE POLICY "Users can view their own profile" ON users_user
    FOR ALL USING (auth.uid()::text = id::text);

-- Politiques RLS pour les produits
CREATE POLICY "Farmers can manage their products" ON products_product
    FOR ALL USING (auth.uid()::text = farmer_id::text);

-- Politiques RLS pour les commandes
CREATE POLICY "Users can view their orders" ON products_order
    FOR ALL USING (auth.uid()::text = buyer_id::text);

-- Politiques RLS pour le panier
CREATE POLICY "Users can manage their cart" ON products_cart
    FOR ALL USING (auth.uid()::text = user_id::text);

-- Politiques RLS pour les messages
CREATE POLICY "Users can view their messages" ON products_message
    FOR ALL USING (
        auth.uid()::text = sender_id::text OR 
        auth.uid()::text = receiver_id::text
    );

-- Politiques RLS pour les conseils (lecture publique pour tous)
CREATE POLICY "Everyone can view advice" ON products_agriculturaladvice
    FOR SELECT USING (true);

CREATE POLICY "Authenticated users can create advice" ON products_agriculturaladvice
    FOR INSERT WITH CHECK (auth.role() = 'authenticated');

-- Politiques RLS pour les cultures
CREATE POLICY "Farmers can manage their cultures" ON products_culture
    FOR ALL USING (auth.uid()::text = farmer_id::text);

-- =====================================
-- 📝 DONNÉES DE TEST (OPTIONNEL)
-- =====================================

-- Créer un admin par défaut
INSERT INTO users_user (username, email, password, role, first_name, last_name)
VALUES (
    'admin',
    'admin@agroconnect.local',
    'pbkdf2_sha256$1200000$N7egLNmAzjTBgRA4RtfdVB$bIYgB0nukqX1ftL2DvVDGAx5fJ1uuZty6anCLSmnw4g=',
    'admin',
    'Admin',
    'AgroConnect'
) ON CONFLICT (username) DO NOTHING;

-- =====================================
-- 🎯 VALIDATION (VERSION SUPABASE COMPATIBLE)
-- =====================================

-- Afficher un résumé simple
SELECT 'AgroConnect Tables Created Successfully' as status;
