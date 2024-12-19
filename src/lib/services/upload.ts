import { invoke } from '@tauri-apps/api/core';
import { open } from '@tauri-apps/plugin-dialog';

/***
 * Open file selection dialog to enable full PC path observation
 */
export async function upload_handler() { 

    const file = await open({
        multiple: false,
        directory: false
    });
    
    if (file)
        invoke('send_csv', { file_path: file });
}