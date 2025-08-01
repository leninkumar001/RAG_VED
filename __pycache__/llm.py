from litellm import completion


def completion_llm(prompt):
    response = completion(
                model="ollama/llama3.2:latest",
                messages = [
                    { "role": "system", "content": "You are a helpful assistant that summarizes text. Given a passage, return a concise summary." },
                    { "role": "user", "content": prompt }
                ],
                api_base="http://localhost:11434",
                api_key="sk_8N_yO2Jg-NLkoQ7MGo9ZCJXeZ-HXd3b22Vvmv8BNnjY",
                stream=True
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            print(chunk.choices[0].delta.content, end="", flush=True)
            # yield chunk.choices[0].delta.content

# def completion_llm(prompt):
#     response = completion(
#                 model="ollama/llama3.2:1b",
#                 messages = [
#                     { "role": "system", "content": "You are a helpful assistant that summarizes text. Given a passage, return a concise summary." },
#                     { "role": "user", "content": prompt }
#                 ],
#                 api_base="http://localhost:11434",
#                 stream=True
#     )
#     for chunk in response:
#         if chunk.choices[0].delta.content is not None:
#             # print(chunk.choices[0].delta.content, end="", flush=True)
#             yield chunk.choices[0].delta.content



# completion_llm("what is the capital of France?")