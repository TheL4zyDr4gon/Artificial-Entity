# Artificial Entity — Desktop Starter

A local desktop AI companion powered by Ollama. The first launch guides users through choosing a name, personality, and model.

## Start on Windows

1. Install Python 3.10+ from https://python.org and Ollama from https://ollama.com/download.
2. Open PowerShell in this folder.
3. Run `py -m pip install -r requirements.txt`.
4. Run `py desktop.py`.

If Ollama is not running, start it from the Start menu (or run `ollama serve`). The app can download `llama3.2:3b` after confirmation. Downloads can be several GB and require an internet connection.

## Privacy

All settings and optional chat history are stored in the local `data/` directory. Do not commit this directory to a public repository. The app sends prompts to the local Ollama endpoint at `127.0.0.1:11434`; it does not expose Ollama to the network. Do not store secrets in prompts or settings.

## Next steps

Package with PyInstaller and optionally bundle a guided Ollama installation. The current starter still requires Python and Ollama to be installed separately.
