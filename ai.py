from ctransformers import AutoModelForCausalLM
import os, sys, time

# Model path setup
model_path = os.path.join("models", "tinyllama-1.1b-chat-v1.0.Q2_K.gguf")

print("AIVA: Booting synthetic consciousness...")

# Optional performance tweak
os.environ["CTRANSFORMERS_CONTEXT_LENGTH"] = "512"

try:
    llm = AutoModelForCausalLM.from_pretrained(
        model_path,
        model_type="llama",         # llama for TinyLLaMA models
        local_files_only=True,      # never tries downloading
        gpu_layers=0                # change if you have GPU
    )
except Exception as e:
    print(f"AIVA: Failed to load model: {e}")
    sys.exit(1)

print("AIVA: Online. Ready to chat.\n")

while True:
    user = input("You: ").strip()
    if user.lower() in ["bye", "exit", "quit"]:
        print("AIVA: Shutting down gracefully. Goodbye.")
        break

    print("AIVA: ", end="", flush=True)

    # Stream output token by token
    try:
        for token in llm(user, max_new_tokens=60, temperature=0.7, stream=True):
            print(token, end="", flush=True)
        print("\n")
    except Exception as e:
        print(f"\n[Error during generation: {e}]\n")
