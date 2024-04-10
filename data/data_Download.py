from datasets import load_dataset

custom_cache_dir = "/data/zys/.cache/huggingface/datasets"

dataset_bgeM3 = load_dataset("Shitao/bge-m3-data", cache_dir=custom_cache_dir)
dataset_quora = load_dataset("quora", cache_dir=custom_cache_dir)

