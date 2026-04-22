-- MySQL Database Setup Script for Decentralized Voting System
-- Run this script to create the database and tables

-- Create the database
CREATE DATABASE IF NOT EXISTS voting_system;
USE voting_system;

-- Create the voters table
CREATE TABLE IF NOT EXISTS voters (
    voter_id VARCHAR(36) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'voter',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert test voter data
INSERT INTO voters (voter_id, password, role) VALUES
('b3e1a2d0-6a1a-4b1f-8d3a-a1c2e4f5b6c7', 'password123', 'voter'),
('c4f2b3e1-7b2b-5c2g-9e4b-b2d3f5g6c7d8', 'password456', 'voter'),
('d5g3c4f2-8c3c-6d3h-af5c-c3e4g6h7d8e9', 'adminpass', 'admin'),
('e6h4d5g3-9d4d-7e4i-bg6d-d4f5h7i8e9fa', 'password789', 'voter');

-- Verify the data was inserted
SELECT * FROM voters;
