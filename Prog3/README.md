# README for Psychotherapist Chat Bot

## Algorithm Outline:
1. **Initialization:** The program initializes an empty dictionary to store keywords and their corresponding responses.
2. **Adding Keywords and Responses:** Keywords along with their responses are added to the dialog system using the `add_keyword_response` method.
3. **User Input Processing:** When the user inputs a message, the program checks for exact matches first. If an exact match is found, a response is generated. Otherwise, it checks for partial matches with any part of the keyword and input text to generate a response.
4. **Descriptor Extraction:** A separate method, `extract_descriptor`, is used to extract descriptors from the user's input based on the triggering keyword. Stopwords are excluded from the descriptor.
5. **Handling No Match:** If no match is found, a response is chosen from the "no match" choices to provide a meaningful interaction.
6. **Efficiency Considerations:** The algorithm optimizes keyword matching by first checking for exact matches and then partial matches, reducing the computational complexity. The `extract_descriptor` method efficiently extracts descriptors by considering stopwords and ensuring the inclusion of articles like "a" or "an" before descriptors if present.

## Dialog Class Description:
The `Dialog` class is the core component of the psychotherapist chat bot. It encapsulates functionalities for adding keywords and responses, processing user input to generate appropriate responses, and extracting descriptors from user input. Key methods include:
- `__init__`: Initializes the dialog system with an empty keywords-responses dictionary.
- `add_keyword_response`: Adds keywords and their corresponding responses to the dialog system.
- `get_response`: Processes user input and returns a response based on keyword matching and descriptor extraction.
- `extract_descriptor`: Extracts descriptors from the user's input based on the triggering keyword.

## Efficiency and Optimization:
Efficiency considerations are integrated into the algorithm and class design:
- Exact match checking is prioritized to quickly identify responses for input messages that match keywords exactly.
- Partial match handling optimizes keyword matching by checking for any part of the keyword in the input text.
- Descriptor extraction efficiently identifies descriptors by considering stopwords and including articles like "a" or "an" before descriptors if present.

## File Structure:
- `chat.py`: Contains the source code for the psychotherapist chat bot.
- `README.md`: This README file describing the algorithm, dialog class, and efficiency considerations.

## Running the Program:
To run the chat bot, execute the `chat.py` file using your `python3` compiler. The program will interactively prompt the user for input and generate responses based on the implemented algorithm.