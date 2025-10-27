# AIVA – AI Virtual Assistant

A lightweight offline conversational AI running purely on CPU.  
built with ctransformers and a local `.gguf` model.(the model size could be 1GB)

---

## 🧠 Features
- Runs **offline** — no API keys, no cloud.
- Uses **TinyLlama 1.1B** (GGUF format) [https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tree/main](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/tree/main)
- Text-only, minimalistic CLI interface.
- “Boots consciousness” and talks back.

---

## 🧩 Setup
1. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
2. Place your model file inside the models folder.

3. Run it
    ```cmd
    python ai.py
    ```

## Additional
If the `pip install -r requirements.txt` doesnt't work then try this `pip install ctransformers==0.2.27`
