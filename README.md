# Bemo-ChatBot





## Introduction

This project is a simple chatbot implementation using Python, TensorFlow, and Tkinter for the graphical user interface. The chatbot is designed to understand user inputs and provide responses based on predefined patterns and responses.

## Project Structure

The project is divided into three main parts: training ,Chat with the Chatbot and the user interface.

### Training Phase

The training phase is responsible for teaching the chatbot how to understand and respond to user inputs. Here's how it works:

- The training data is defined in a JSON file (`intents.json`), which contains intents, patterns, and responses.
- The NLTK library is used for natural language processing, including tokenization and lemmatization.
- The training data is preprocessed to create a bag of words representation for each pattern.
- A neural network model is created using TensorFlow/Keras to learn from the training data.
- The model is trained using the processed training data for a specified number of epochs.



### Chat with the Chatbot::

- This script is used to chat with the trained chatbot.
- It loads the trained model and vocabulary information.
- Users can type messages, and the chatbot responds based on its training.
### User Interface (Tkinter GUI)

The user interface provides a graphical interface for users to interact with the chatbot. Here's what the interface offers:

- The interface is built using Tkinter, a Python library for creating graphical user interfaces.
- Users can type messages in an input box at the bottom and press "Enter" or click the "Send" button to send messages.
- The chat history is displayed in a text widget, allowing users to see both their messages and the chatbot's responses.
- The interface is designed with a dark color scheme, custom fonts, and a distinct "Send" button.

## Setup and Usage

To run the chatbot, follow these steps:

1. Ensure you have the required libraries installed, including TensorFlow, NLTK, and Keras.
2. Prepare your training data in the `intents.json` file. Define intents, patterns, and responses.
3. Run the training phase code to train the chatbot model. This will generate `words.pkl`, `classes.pkl`, and `chatbot_model.h5` files.
4. Execute the user interface code to launch the chatbot GUI.
5. Type messages in the input box, press "Enter" or click "Send," and the chatbot will respond based on the training data.

## Customization

You can customize the chatbot's behavior by modifying the training data in the `intents.json` file. Define new intents, patterns, and responses to make the chatbot respond to specific user inputs.

Feel free to customize the GUI's appearance by changing colors, fonts, and styles to match your preferences.

## Contributions

Contributions to this project are welcome. You can enhance the chatbot's capabilities, improve its training data, or make UI/UX enhancements.

## Acknowledgments

This project was created as a learning exercise and is inspired by various chatbot tutorials and resources available online. It serves as a foundation for building more advanced chatbots with additional features and integrations.
