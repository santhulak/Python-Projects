# Mood-Based Response Bot

print("🤖 MoodBot: Hi! I want to understand how you're feeling today.")
mood = input("How are you feeling right now? ").lower()

print("\n🤖 MoodBot Response:")

if "happy" in mood or "good" in mood or "great" in mood:
    print("That's awesome! Keep spreading the positivity ✨🔥")

elif "sad" in mood or "down" in mood or "upset" in mood:
    print("I'm sorry you're feeling this way 💛")
    print("Try taking a deep breath and remember — this moment will pass.")

elif "angry" in mood or "mad" in mood or "frustrated" in mood:
    print("It’s okay to feel angry sometimes 😤")
    print("Maybe step away for a moment and reset.")

elif "tired" in mood or "sleepy" in mood or "exhausted" in mood:
    print("You sound exhausted 😴 Make sure to rest and hydrate.")

elif "anxious" in mood or "stressed" in mood or "nervous" in mood:
    print("You’re not alone 🤍")
    print("Try this: inhale 4 sec → hold 4 sec → exhale 4 sec.")

else:
    print("I may not fully understand that mood yet… but I’m here for you 💙")

print("\n🤖 MoodBot: Want to talk more? I'm always here.")
