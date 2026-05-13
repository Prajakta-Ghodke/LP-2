# Simple Smart Shop Chatbot

print("Welcome to Smart Shop Chatbot")
print("Type 'exit' to stop")

while True:

    # Take user input
    user = input("You: ").lower()

    # Greeting
    if "hello" in user or "hi" in user:
        print("Bot: Hello! Welcome to Smart Shop.")

    # Price information
    elif "price" in user:
        print("Bot: Mobile price starts from 10000 rupees.")

    # Discount information
    elif "discount" in user:
        print("Bot: Today we have 20% discount on electronics.")

    # Delivery information
    elif "delivery" in user:
        print("Bot: Delivery will take 3 to 5 days.")

    # Payment methods
    elif "payment" in user:
        print("Bot: We support UPI, Card and Cash on Delivery.")

    # Contact details
    elif "contact" in user:
        print("Bot: Contact us on 9876543210.")

    # Thank you message
    elif "thank" in user:
        print("Bot: You are welcome!")

    # Exit condition
    elif user == "exit":
        print("Bot: Thank you for visiting Smart Shop.")
        break

    # Default response
    else:
        print("Bot: Sorry! Please ask another question.")