# LLM-Learning Chat Application

This project is a command-line chat application that utilizes OpenAI's API to provide conversational capabilities. The application maintains a persistent chat history and allows users to interact with the AI in a simple and intuitive manner.

## Project Structure

- `cli_chat.py`: Contains the main logic for the chat application, including functions to load and save chat history, build a chat chain with a specified model, and handle user input.
- `requirements.txt`: Lists the dependencies required for the project.
- `.env`: Stores environment variables such as API keys and model configurations.
- `chat_history.json`: Persists chat history in JSON format for maintaining context across sessions.
- `README.md`: Documentation for the project.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/LLM-Learning.git
   cd LLM-Learning
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   OPENAI_MODEL=gpt-4o-mini
   ```

## Usage

To run the chat application, execute the following command in your terminal:

```
python cli_chat.py
```

You can specify a different model by using the `--model` argument:

```
python cli_chat.py --model gpt-4o-mini
```

Type your messages in the terminal, and the AI will respond. Type 'exit' or 'quit' to end the session.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.