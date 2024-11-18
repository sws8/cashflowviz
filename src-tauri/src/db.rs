use std::fs;
use std::path::PathBuf;

use dirs;
use rusqlite::Connection;

/**
 * Return database connection
 */
pub fn get_database_connection() -> Connection {
    let database_path = get_database_path(); 
    let conn = Connection::open(database_path).expect("Could not open database.");
    conn
}

/**
 * Find and return database file path
 */
fn get_database_path() -> PathBuf {
    let db = dirs::config_dir()
        .expect("Could not resolve path to config folder to store database.")
        .join("money");
    
    if !db.exists() {
        fs::create_dir_all(&db).expect("Could not create application config directory.");
    }

    db.join("money.db3")
}