# ==========================================================
# CODSOFT TASK 4
# AI Course Recommendation System
# Developed by Yatharth Singhal
# ==========================================================



from Courses import courses
from datetime import datetime
import time
import random
import sys


tips = [
    "Practice coding every day.",
    "Build projects to improve your skills.",
    "Contribute to open-source projects.",
    "Consistency beats intensity.",
    "Learn by creating real-world applications.",
    "Read documentation regularly.",
    "Debugging makes you a better programmer."
]

print(f"\n💡 Learning Tip: {random.choice(tips)}")

def loading():
    print("\n🤖 AI is analyzing your learning goals", end="")

    for _ in range(6):
        print(".", end="", flush=True)
        time.sleep(0.4)

    print("\n")



print("=" * 70)
print("🤖 AI COURSE RECOMMENDATION SYSTEM")
print("=" * 70)
print("🎓 Discover the Best Programming & Technology Courses")
print("💡 Personalized Recommendations Based on Your Interests")
print("👨‍💻 Developed by Yatharth Singhal")
print("🚀 Powered by Python")
print("=" * 70)


print(f"🕒 {datetime.now().strftime('%d-%m-%Y | %I:%M %p')}")



while True:

    print(f"\n📚 Total Categories Available: {len(courses)}\n")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    for category in courses:
        print(f"✅ {category.title()}")

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

    user_choice = input("\n💡 Enter your interest: ").lower().strip()

    print("\n🤖 AI is searching the best recommendations...")
    time.sleep(1.5)


    if user_choice in courses:

        print("\n" + "=" * 65)
        print(f"🎯 TOP RECOMMENDED {user_choice.upper()} COURSES")
        print("=" * 65)

        for i, course in enumerate(courses[user_choice], start=1):
            print(f"{i}. 📖 {course}")

        print(f"\n📊 Total Recommendations: {len(courses[user_choice])}")



        print("=" * 65)
        print("💡 Happy Learning! Keep Building Amazing Projects.")
        print("=" * 65)
    else:
        print("\n❌ Oops! Invalid category.")

    print("\n📚 Available Categories:")

    for category in courses:
        print(f"👉 {category.title()}")

    print("\n💡 Please try again.")

    again = input("\n🔄 Would you like another recommendation? (yes/no): ").lower().strip()


    if again != "yes":
        break

print("\n📈 SESSION SUMMARY")
print("-" * 40)
print(f"📚 Total Categories : {len(courses)}")
print("🤖 AI Recommendations : Successful")
print("⭐ Status : Completed")




print("\n" + "=" * 65)
print("🙏 Thank You for Using the AI Course Recommendation System!")
print("=" * 65)
print("    👨‍💻 Developed by : Yatharth Singhal   ")
print("🏫 Galgotias University")
print("💻 GitHub : https://github.com/YathartAI")
print("💼 LinkedIn : https://www.linkedin.com/in/yatharth-singhal-ai/")
print()
print("🌟 Keep Learning")
print("💡 Keep Building")
print("🚀 Keep Growing")
print()
print("     Thank you for trying my project! I hope you found it helpful and enjoyable. If you have any feedback or suggestions, feel free to reach out to me on GitHub or LinkedIn. Happy coding!  🚀")
print("=" * 65)