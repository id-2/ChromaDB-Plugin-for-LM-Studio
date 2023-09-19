import tkinter as tk

def create_table(parent_frame):
    models = [
        "BAAI/bge-large-en", "BAAI/bge-base-en", "BAAI/bge-small-en",
        "thenlper/gte-large", "thenlper/gte-base", "thenlper/gte-small",
        "intfloat/e5-large-v2", "intfloat/e5-base-v2", "intfloat/e5-small-v2",
        "hkunlp/instructor-xl", "hkunlp/instructor-large", "hkunlp/instructor-base",
        "sentence-transformers/all-mpnet-base-v2", "sentence-transformers/all-MiniLM-L12-v2", "sentence-transformers/all-MiniLM-L6-v2"
    ]
    vram_values = [
        "5.3GB", "3.7GB", "2.9GB", "5.3GB", "3.7GB", "3GB", "5.2GB", "3.7GB", "2.9GB",
        "18.1GB", "6.8GB", "4.6GB", "2.7GB", "1.6GB", "1.6GB"
    ]

    table_frame = tk.Frame(parent_frame, bg="#202123")
    table_frame.pack(pady=5, fill=tk.BOTH, expand=1)

    tk.Label(table_frame, text="Embedding Model", borderwidth=1, relief="solid", font=("Segoe UI Historic", 13), bg="#202123", fg="light gray").grid(row=0, column=0, sticky="nsew")
    tk.Label(table_frame, text="Estimated VRAM", borderwidth=1, relief="solid", font=("Segoe UI Historic", 13), bg="#202123", fg="light gray").grid(row=0, column=1, sticky="nsew")

    for i, (model, vram) in enumerate(zip(models, vram_values), start=1):
        tk.Label(table_frame, text=model, borderwidth=1, relief="solid", font=("Segoe UI Historic", 10), bg="#202123", fg="light gray").grid(row=i, column=0, sticky="nsew")
        tk.Label(table_frame, text=vram, borderwidth=1, relief="solid", font=("Segoe UI Historic", 10), bg="#202123", fg="light gray").grid(row=i, column=1, sticky="nsew")

    table_frame.grid_columnconfigure(0, weight=1)
    table_frame.grid_columnconfigure(1, weight=1)

def create_pro_tip(parent_frame):
    pro_tip_label = tk.Label(parent_frame, text="Pro tip:", font=("Segoe UI Historic", 12, "bold"), bg="#202123", fg="light gray")
    pro_tip_label.pack(pady=(10, 0), anchor="w", padx=5, side=tk.TOP)

    pro_tip_text = (
        "DO NOT have LM Studio running when creating the vector database. The VRAM numbers above refer to when creating "
        "the database, hence more VRAM used. After it's created, run LM Studio and "
        "load your LLM . To query the database, "
        "the embedding model uses much less VRAM. Use the LARGEST embedding model you can possibly fit into VRAM while the "
        "LLM is loaded into LM Studio. The quality of the embedding model is ACTUALLY MORE important than the size of the LLM. "
        "Experiment with low-quality LLMs and high-quality embedding models. For example, q3_k_3 model + instructor-xl worked "
        "just fine together. If your text has a lot of technical jargon, a larger LLM might be better, but for everyday usage, "
        "strive to use as large of an embedding model as possible with as large of an LLM with the remaining VRAM."
    )

    pro_tip_description = tk.Label(parent_frame, text=pro_tip_text, wraplength=400, justify="left", font=("Segoe UI Historic", 10), bg="#202123", fg="light gray")
    pro_tip_description.pack(anchor="w", padx=5, side=tk.TOP)
