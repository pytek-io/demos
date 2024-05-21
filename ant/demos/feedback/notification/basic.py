import render_antd as antd


def app(_):[package]
name = "static-server"
version = "0.5.3"
edition = "2021"
publish = false

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

# took from https://github.com/rust-analyzer/rust-analyzer/blob/48f84a7b60bcbd7ec5fa6434d92d9e7a8eb9731b/Cargo.toml
[profile.dev]
# Disabling debug info speeds up builds a bunch,
# and we don't rely on it for debugging that much.
debug = 0

[profile.release]
incremental = true
debug = 0 # Set this to 1 or 2 to get more useful backtraces in debugger.

[dependencies]
axum = {version = "0.7.5" }
tokio = { version = "1.37.0", features = ["full"] }
tracing = "0.1.40"
tracing-subscriber = "0.3.18"
tower = "0.4.13"
tower-http = { version = "0.5.2", features = ["fs", "trace"] }
askama = "0.12.1"
mime_guess = "2.0.4"
mime = "0.3.17"
base64 = "0.22.0"
time = { version = "0.3.36", features = ["formatting"] }
clap = { version = "4.5.4", features = ["derive"] }

[patch.crates-io]
#tokio = { git = "https://github.com/tokio-rs/tokio.git", branch = "master" }
#tokio-util = { git = "https://github.com/tokio-rs/tokio.git", branch = "master" }
#tower-http = { git = "https://github.com/tower-rs/tower-http.git", branch = "master" }
#tower-http = { path = "../tower-http/tower-http" }

    def onClick():
        antd.notification.open(
            {
                "message": "Notification Title",
                "description": "This is the content of the notification. This is the content of the notification. This is the content of the notification.",
                "onClick": lambda: print("Notification Clicked!"),
            },
        )

    return antd.Button("Open the notification box", type="primary", onClick=onClick)
