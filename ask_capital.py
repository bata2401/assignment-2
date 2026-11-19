import ollama

def ask_capital(country, model="gemma4"):
    try:
        prompt = f"What is the capital of {country}?"

        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt
                }
            ]
        )

        return response['message']['content']

    except Exception:
        return "Failure."
    