from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

model_name = "gpt2"
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
 
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
input_text = "Reiz kādā tālā zemē..." 
input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print("Generated Text:")
print(generated_text)
