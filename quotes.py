import random

# List of quotes
quotes = [
    "The best way to predict the future is to invent it. - Alan Kay",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Do what you can, with what you have, where you are. - Theodore Roosevelt",
    "You miss 100% of the shots you don't take. - Wayne Gretzky",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt"
]

def display_random_quote():
    # Select a random quote
    quote = random.choice(quotes)
    print("\n🌟 Random Quote 🌟")
    print(f"{quote}\n")

# Run the program
if __name__ == "__main__":
    display_random_quote()
