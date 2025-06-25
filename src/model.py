import torch

from transformers import AutoModelForCausalLM, AutoTokenizer


class ChatBot:
    def __init__(self, model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0"):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.chat_history_ids = None

    def ask(self, user_input: str) -> str:
        # Format as instruction-style prompt
        prompt = user_input

        # Encode the prompt
        new_input_ids = self.tokenizer.encode(prompt, return_tensors='pt')

        # Append to chat history if exists
        if self.chat_history_ids is not None:
            bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1)
        else:
            bot_input_ids = new_input_ids

        attention_mask = torch.ones(bot_input_ids.shape, dtype=torch.long)

        # Generate response
        self.chat_history_ids = self.model.generate(
            bot_input_ids,
            attention_mask=attention_mask,
            max_length=bot_input_ids.shape[-1] + 10,
            pad_token_id=self.tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.1,
            top_k=30,
            top_p=0.85,
            repetition_penalty=1.2,
        )

        # Decode only new response
        response = self.tokenizer.decode(
            self.chat_history_ids[0][bot_input_ids.shape[-1]:],
            skip_special_tokens=True
        )

        return response.strip()

    def reset(self):
        self.chat_history_ids = None