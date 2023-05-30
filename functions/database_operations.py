import sqlite3
import os
from utils.tcolors import tcolors


DATABASE_PATH = os.path.join(os.getcwd(), 'Database', 'password_manager.db')


class Database:
    def __init__(self):
        os.makedirs(os.path.dirname(DATABASE_PATH), exist_ok=True)
        self.conn = sqlite3.connect(DATABASE_PATH)
        self.cursor = self.conn.cursor()
        self.conn.execute('PRAGMA foreign_keys = ON')


    def close_connection(self):
        self.conn.close()


    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            master_password_hash BLOB NOT NULL,
            salt BLOB NOT NULL
            );
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS stored_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            item_name TEXT NOT NULL,
            encrypted_username BLOB NOT NULL,
            encrypted_password BLOB NOT NULL,
            url TEXT,
            notes TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            );
        ''')
        self.conn.commit()


    def insert_user(self, username, hashed_password, salt):
        self.cursor.execute('INSERT INTO users (username, master_password_hash, salt) VALUES (?,?,?)', (username, hashed_password, salt))
        return self.conn.commit()


    def login_user(self, username):
        self.cursor.execute('SELECT id, master_password_hash, salt FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()
    

    def get_username(self, username):
        self.cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
        return self.cursor.fetchone()


    def get_user_id(self, user_id):
        self.cursor.execute('SELECT id FROM users where id = ?', (user_id,))
        return self.cursor.fetchone()

    
    def get_user_salt_and_hash(self, user_id):
        self.cursor.execute('SELECT master_password_hash, salt FROM users WHERE id = ?', (user_id,))
        return self.cursor.fetchone()


    def add_item(self, user_id, item_name, stored_username, stored_password, url, notes):
        encrypted_username = stored_username
        encrypted_password = stored_password
        self.cursor.execute('INSERT INTO stored_items (user_id, item_name, encrypted_username, encrypted_password, url, notes) VALUES (?,?,?,?,?,?)', (user_id, item_name, encrypted_username, encrypted_password, url, notes))        
        self.conn.commit()
        print(tcolors.GREEN('Item successfully added!'))


    def retrieve_item(self, user_id):
        self.cursor.execute('''
            SELECT id, item_name, encrypted_username, encrypted_password, url, notes 
            FROM stored_items 
            WHERE user_id = ?
        ''', (user_id,))
        return self.cursor.fetchall()
    

    def update_item(self, item_id, user_id, item_name, stored_username, stored_password, url, notes):
        self.cursor.execute('''
        UPDATE stored_items 
        SET item_name = ?, encrypted_username = ?, encrypted_password = ?, url = ?, notes = ?
        WHERE id = ? AND user_id = ?
    ''', (item_name, stored_username, stored_password, url, notes, item_id, user_id))
        self.conn.commit()
    print(tcolors.GREEN('Item successfully updated!'))


    def delete_item(self, item_id, user_id):
        self.cursor.execute('''
            DELETE FROM stored_items 
            WHERE id = ? AND user_id = ?
        ''', (item_id, user_id))
        self.conn.commit()
        print(tcolors.GREEN('Item successfully deleted!'))