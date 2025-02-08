#![windows_subsystem = "windows"]

#[tokio::main]
async fn main() {
    // Define the directory to serve files from
    let image_dir = warp::fs::dir("avespfade_tiles");

    // Start the warp server
    warp::serve(image_dir)
        .run(([127, 0, 0, 1], 3030))
        .await;
}