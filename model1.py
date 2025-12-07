from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Thinking:novita",
    messages=[
        {
            "role": "user",
            "content": "Сколько весит жираф?"
        }
    ],
)

print(completion.choices[0].message)