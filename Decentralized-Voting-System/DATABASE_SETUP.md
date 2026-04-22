# Database Setup Guide

## Overview
Your login endpoint expects a MySQL database with a `voters` table containing:
- `voter_id` (UUID string, primary key)
- `password` (plaintext or hashed)
- `role` (either 'voter' or 'admin')

## Setup Instructions

### Option 1: Using Python Script (Recommended)
Run this from the project root:

```powershell
cd 'C:\Users\Aman singh\OneDrive\Desktop\development\Decentralized-Voting-System'
python setup_database.py
```

The script will prompt you for your MySQL credentials and automatically:
- Create the `voting_system` database
- Create the `voters` table
- Insert test voter data

### Option 2: Manual MySQL Setup
If you prefer to run SQL directly:

1. Open MySQL command line or MySQL Workbench
2. Run the SQL commands from `setup_database.sql`:

```sql
CREATE DATABASE IF NOT EXISTS voting_system;
USE voting_system;

CREATE TABLE IF NOT EXISTS voters (
    voter_id VARCHAR(36) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) NOT NULL DEFAULT 'voter',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO voters (voter_id, password, role) VALUES
('b3e1a2d0-6a1a-4b1f-8d3a-a1c2e4f5b6c7', 'password123', 'voter'),
('c4f2b3e1-7b2b-5c2g-9e4b-b2d3f5g6c7d8', 'password456', 'voter'),
('d5g3c4f2-8c3c-6d3h-af5c-c3e4g6h7d8e9', 'adminpass', 'admin'),
('e6h4d5g3-9d4d-7e4i-bg6d-d4f5h7i8e9fa', 'password789', 'voter');
```

## Update .env Configuration
Make sure your `.env` file in `Database_API/` has correct credentials:

```env
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_HOST=127.0.0.1
MYSQL_DB=voting_system
```

## Test Voter Credentials
After setup, you can login with these credentials:

| Voter ID | Password | Role |
|----------|----------|------|
| b3e1a2d0-6a1a-4b1f-8d3a-a1c2e4f5b6c7 | password123 | voter |
| c4f2b3e1-7b2b-5c2g-9e4b-b2d3f5g6c7d8 | password456 | voter |
| d5g3c4f2-8c3c-6d3h-af5c-c3e4g6h7d8e9 | adminpass | admin |
| e6h4d5g3-9d4d-7e4i-bg6d-d4f5h7i8e9fa | password789 | voter |

## Verify Connection
After setup, you should see successful login requests instead of 401 errors in the uvicorn logs.

## Troubleshooting

**Error: "Something is wrong with your user name or password"**
- Check your MySQL credentials in `.env`
- Verify MySQL is running
- Confirm the database exists

**Error: "Database does not exist"**
- Run the setup script again
- Check that the database creation was successful

**Still getting 401 on login?**
- Make sure you're using the exact voter_id and password from the test data
- Check the browser developer console for the exact request being sent
- Verify the API is receiving the credentials correctly
