# Name Mood Analyzer 🎭

name = input("Enter your name: ")

# Convert to lowercase for easier comparison
n = name.lower()

if n.startswith("a") or n.endswith("a"):
    mood = "Calm & Creative ✨"
elif "z" in n:
    mood = "Cool & Mysterious 😎"
elif len(n) <= 4:
    mood = "Cute & Energetic 😄"
elif len(n) >= 8:
    mood = "Wise & Thoughtful 🧠"
elif "k" in n or "r" in n:
    mood = "Bold & Confident 🔥"
else:
    mood = "Balanced & Friendly 😊"

print(f"\nHey {name}! Your mood vibe today is: {mood}")
