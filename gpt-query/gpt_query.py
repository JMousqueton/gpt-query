import openai
import os
from dotenv import load_dotenv

class GPTQuery:
    """
    A class to query OpenAI's GPT-4 model for information about company activity sectors.

    Methods
    -------
    __init__():
        Initializes the class by loading the API key.

    query(prompt, max_tokens=150):
        Sends a prompt to the GPT-4 model and returns the response.
    """

    def __init__(self):
        """Initializes the GPTQuery class by loading the API key from the .env file."""
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.gptmodel = os.getenv('OPENAI_MODEL', 'gpt-4')  # Default to 'gpt-4' if not specified
        openai.api_key = self.api_key

    def query(self, prompt, max_tokens=150):
        """
        Sends a prompt to the GPT-4 model and returns the main activity sector of the company.

        Parameters
        ----------
        prompt : str
            The prompt to send to the GPT-4 model.
        max_tokens : int, optional
            The maximum number of tokens to generate in the response (default is 150).

        Returns
        -------
        str
            The main activity sector of the company.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.gptmodel,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                n=1,
                stop=None,
                temperature=0.7,
            )
            sector = response.choices[0].message['content'].strip()
            return sector
        except Exception as e:
            return f"An error occurred: {e}"
