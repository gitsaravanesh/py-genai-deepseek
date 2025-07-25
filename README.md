# DeepSeek Chat UI

A lightweight web-based chat interface that connects to an Ollama instance serving the DeepSeek model. Built with Streamlit and a tiny Python backend, this project lets you spin up a friendly UI on your EC2 instance and start chatting with DeepSeek in just a few minutes.

## Features

* **Streamlit frontend**: Minimal dependencies, real-time UI updates, and easy customization.
* **Ollama integration**: Talk to the `deepseek-coder:1.3b-instruct` model (or swap in any Ollama-supported model).
* **Simple deployment**: One-click setup on an Ubuntu EC2 instance (t3.medium recommended).
* **Configurable**: Tweak model name, API endpoint, and streaming options in `app.py`.
* **Optional Nginx UI**: Serve a static HTML chat page via Nginx for zero-Python deployments.

## Prerequisites

* An EC2 instance (Ubuntu 22.04) with:

  * At least **4 GiB RAM** (t3.medium)
  * **50 GB** root volume
  * Python 3.12
  * `ollama` installed and running on `127.0.0.1:11434`
* Access to the instance’s security group to open ports:

  * **8501** (Streamlit UI)
  * **11434** (Ollama API, if you plan to access it externally)
  * **80** (for Nginx UI, if using Nginx frontend)

## Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. **Create & activate a Python venv** (for Streamlit)

   ```bash
   sudo apt-get install -y python3-venv python3-full
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install ollama and dependencies**

   ```bash
   export OLLAMA_NO_CUDA=1
   curl -fsSL https://ollama.com/install.sh | sh
   sudo systemctl enable --now ollama

   ollama --version
   sudo ss -tunlp | grep 11434 

   pip install --upgrade pip
   pip install streamlit requests
   ```

4. **Ensure Ollama is running** on `127.0.0.1:11434`:

   ```bash
   ollama status
   ```

5. **Pull the DeepSeek model** (if you haven’t already):

   ```bash
   ollama pull deepseek-coder:1.3b-instruct
   ```

## Running the App with Streamlit

With your venv activated:

```bash
streamlit run app.py \
  --server.port 8501 \
  --server.address 0.0.0.0
```

Browse to `http://<ec2-public-ip>:8501` and start chatting!

## Configuration

* **Model**: Change the `model` field in the `payload` dict inside `app.py` or `index.html` to any Ollama model name.
* **Streaming**: Toggle `"stream": false` in the POST payload to switch between streaming and one-shot responses.
* **Security**: For public deployments, sit Streamlit or Nginx behind API Gateway or enable HTTPS and lock down your security group to trusted IPs.

## Cleanup & Maintenance

* Remove unused models:

  ```bash
  ollama rm <model-name>
  ```
* Clear Ollama cache:

  ```bash
  rm -rf ~/.cache/ollama
  ```
* Manage swap and disk space with `df -h` and `free -h`.
