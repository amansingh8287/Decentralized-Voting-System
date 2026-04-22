#!/usr/bin/env python3
"""
MySQL Database Setup Script for Decentralized Voting System
Run this script to automatically create the database and seed test data
"""

import mysql.connector
from mysql.connector import errorcode

# MySQL connection config (update with your actual credentials)
config = {
    'user': 'root',
    'password': 'password',  # Change this to your MySQL root password
    'host': '127.0.0.1',
    'raise_on_warnings': True,
}

def create_database():
    """Create the voting_system database and voters table"""
    try:
        # Connect to MySQL server
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()

        # Create database
        print("Creating database 'voting_system'...")
        cursor.execute("CREATE DATABASE IF NOT EXISTS voting_system")
        cnx.database = 'voting_system'
        print("✓ Database created successfully")

        # Create voters table
        print("\nCreating 'voters' table...")
        create_table_query = """
        CREATE TABLE IF NOT EXISTS voters (
            voter_id VARCHAR(36) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            role VARCHAR(50) NOT NULL DEFAULT 'voter',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
        cursor.execute(create_table_query)
        cnx.commit()
        print("✓ Voters table created successfully")

        # Insert test data
        print("\nInserting test voter data...")
        test_voters = [
            ('b3e1a2d0-6a1a-4b1f-8d3a-a1c2e4f5b6c7', 'password123', 'voter'),
            ('c4f2b3e1-7b2b-5c2g-9e4b-b2d3f5g6c7d8', 'password456', 'voter'),
            ('d5g3c4f2-8c3c-6d3h-af5c-c3e4g6h7d8e9', 'adminpass', 'admin'),
            ('e6h4d5g3-9d4d-7e4i-bg6d-d4f5h7i8e9fa', 'password789', 'voter'),
        ]

        insert_query = "INSERT INTO voters (voter_id, password, role) VALUES (%s, %s, %s)"
        
        # Clear existing data first
        cursor.execute("DELETE FROM voters")
        
        for voter in test_voters:
            cursor.execute(insert_query, voter)
        
        cnx.commit()
        print(f"✓ Inserted {len(test_voters)} test voters")

        # Display inserted data
        print("\n" + "="*60)
        print("Inserted Test Voters:")
        print("="*60)
        cursor.execute("SELECT voter_id, password, role FROM voters")
        for voter_id, password, role in cursor.fetchall():
            print(f"  Voter ID: {voter_id}")
            print(f"  Password: {password}")
            print(f"  Role: {role}")
            print("-" * 60)

        cursor.close()
        cnx.close()
        print("\n✓ Database setup completed successfully!")
        print("\nYou can now login with these credentials:")
        print("  - Admin: voter_id=d5g3c4f2-8c3c-6d3h-af5c-c3e4g6h7d8e9, password=adminpass")
        print("  - User: voter_id=b3e1a2d0-6a1a-4b1f-8d3a-a1c2e4f5b6c7, password=password123")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("✗ Error: Invalid MySQL username or password")
            print("  Update the 'config' dictionary with your MySQL credentials")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("✗ Error: Database does not exist")
        else:
            print(f"✗ Error: {err}")
        return False
    
    return True

if __name__ == '__main__':
    print("MySQL Database Setup for Decentralized Voting System")
    print("=" * 60)
    
    # Update these with your MySQL credentials
    config['user'] = input("Enter MySQL username (default: root): ") or 'root'
    config['password'] = input("Enter MySQL password (default: password): ") or 'password'
    config['host'] = input("Enter MySQL host (default: 127.0.0.1): ") or '127.0.0.1'
    
    success = create_database()
    if not success:
        print("\nSetup failed. Please check your MySQL credentials and try again.")
