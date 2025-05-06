from openai import OpenAI
from sk import my_sk

client = OpenAI(
  api_key = my_sk
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "Listen to your"}
  ],
  max_tokens = 3, 
  n = 5
)

for i in range(len(completion.choices)):
  print(completion.choices[0].message);
