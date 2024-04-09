import random

class Dialog:
    def __init__(self):
        # Initialize an empty dictionary to store keywords and their corresponding responses
        self.keywords_responses = {}

    def add_keyword_response(self, keywords, responses):
        # Split the keywords by comma, strip leading/trailing spaces, convert to lowercase,
        # and add each keyword along with its responses to the dictionary
        keywords_list = [keyword.strip().lower() for keyword in keywords.split(",")]
        for keyword in keywords_list:
            self.keywords_responses[keyword] = responses

    def get_response(self, input_text):
        input_text_lower = input_text.lower()

        # Check for exact matches first
        if input_text_lower in self.keywords_responses:
            responses = self.keywords_responses[input_text_lower]
            return random.choice(responses)

        # Check for partial matches with any part of the keyword and input text
        for keyword in self.keywords_responses:
            if keyword.lower() in input_text_lower:
                responses = self.keywords_responses[keyword]
                descriptor = self.extract_descriptor(input_text_lower, keyword)
                if descriptor:
                    response = random.choice(responses).replace('*', descriptor)
                    return response

        # If no match is found, choose a response from "no match" choices
        if "no match" in self.keywords_responses:
            return random.choice(self.keywords_responses["no match"])

        return "I'm not sure I understand you fully."

    def extract_descriptor(self, input_text, keyword):
        input_words = input_text.split()
        keyword_words = keyword.split()
        stopwords = ["am", "is", "are", "was", "were", "to", "be", "the", "i", "me", "my", "you", "your"]

        for i in range(len(input_words) - len(keyword_words) + 1):
            match = True
            for j in range(len(keyword_words)):
                input_word = input_words[i + j].lower()
                keyword_word = keyword_words[j].lower()
                # Check if the input word is in the keyword word or if it's a stopword
                if input_word not in keyword_word and input_word not in stopwords:
                    match = False
                    break
            if match:
                # Extract descriptor words after the keyword
                descriptor_words = input_words[i + len(keyword_words):]
                # Include "a" or "an" before the descriptor if they appear in the input
                if descriptor_words and descriptor_words[0].lower() in ["a", "an"]:
                    descriptor = " ".join(descriptor_words)
                else:
                    descriptor = " ".join(word for word in descriptor_words if word.lower() not in stopwords)
                return descriptor.strip()

        return None




def main():
    dialog = Dialog()
    keywords_responses_dict = {
        "always": ["Can you think of a specific example?"],
        "because": ["Is that the real reason?"],
        "sorry": ["Please don't apologize."],
        "maybe": ["You don't seem very certain."],
        "i think": ["Do you really think so?"],
        "i am, i'm": ["I am sorry to hear you are *.", "How long have you been *?",
                      "Do you believe it is normal to be *?", "Do you enjoy being *?"],
        "i feel": ["Tell me more about such feelings.", "Do you often feel *?",
                   "Do you enjoy feeling *?", "Why do you feel that way?"],
        "you": ["We were discussing you, not me.", "You seem quite positive."],
        "yes": ["Why do you think so?", "You seem quite positive."],
        "no": ["Why not?", "Are you sure?"],
        "family, mother, mom, dad, father, sister, brother, husband, wife": [
            "Tell me more about your family.",
            "How do you get along with your family?",
            "Is your family important to you?"
        ],
        "dream": ["What does that dream suggest to you?", "Do you dream often?",
                  "What persons appear in your dreams?", "Are you disturbed by your dreams?"],
        "stress, overwhelmed, pressure": [ 
            #added some extra options about stress and inadequacy because I sometimes suffer from those. 
        "It sounds like you're dealing with a lot of stress. Would you like to talk more about it?",
        "Managing stress is important for your well-being. How do you usually cope with stress?",
        "Feeling overwhelmed can be tough. Let's explore ways to reduce your stress levels."
        ],
        "inadequate, not good enough, worthless": [
            "You are not alone in feeling this way. Many people struggle with feelings of inadequacy.",
            "Remember, everyone has strengths and weaknesses. You are valuable just as you are.",
            "It's common to doubt yourself at times, but try to focus on your accomplishments and strengths."
        ],
        "no match": ["What does that suggest to you?", "I see.", "I'm not sure I understand you fully.",
                     "Can you elaborate?", "That is quite interesting."]
    }

    # Add keywords and responses to the dialog object
    for keywords, responses in keywords_responses_dict.items():
        dialog.add_keyword_response(keywords, responses)

    # Gave the AI a more human name and dialogue intialization message.
    print("================================================================")
    print("My name is Dr. Allie Isenberg --")
    print("\nWhat would you like to talk about in today's session?")
    print("================================================================\n")

    while True:
        user_input = input("\t- ")
        print("\n")
        if "bye" in user_input.lower():
            print("Goodbye!")
            break
        else:
            response = dialog.get_response(user_input)
            print(response + "\n")

if __name__ == "__main__":
    main()
