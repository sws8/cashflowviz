mod db;
mod commands;

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {

  let connection = db::get_database_connection();

  tauri::Builder::default()
    .invoke_handler(tauri::generate_handler![commands::send_csv])
    .setup(|app| {
      if cfg!(debug_assertions) {
        app.handle().plugin(
          tauri_plugin_log::Builder::default()
            .level(log::LevelFilter::Info)
            .build(),
        )?;
      }
      Ok(())
    })
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
