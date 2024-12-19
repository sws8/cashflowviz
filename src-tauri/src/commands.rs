// use tauri::ipc::Response;

// #[tauri::command]
// pub fn send_csv(file_path: String) -> Response {
//     let data = std::fs::read().unwrap();
//     println!("I was invoked from Svelte!");
//     tauri::ipc::Response::new(data)
// }

#[tauri::command(rename_all = "snake_case")]
pub fn send_csv(file_path: String) {
    println!("Uploaded: {}", file_path);
}
