# love_cli.py
# The heartbreak-themed CLI tool nobody asked for, but everybody needed.

import time
import random
import sys
from datetime import datetime

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

coping_mechanisms = [
    "Take a walk. Don’t check your phone.",
    "Write but don’t send.",
    "Cry. Hydrate. Repeat.",
    "Block, unblock. Repeat? No. Grow.",
    "You deserve replies. Full stop.",
    "It’s not you. It’s their emotional Wi-Fi."
]

overthink_loops = [
    "Should I have just said hi instead?",
    "Maybe she just forgot... for 72 hours.",
    "I come off too strong. I should delete myself.",
    "Was it the emoji? Did I scare her off with the heart?",
    "I swear she used to care... or did I imagine it?"
]

inspo_fallback = [
    "This too shall pass.",
    "You are not your rejection.",
    "Every chapter of love teaches you something.",
    "You are whole on your own.",
    "Someone out there is craving your type of love.",
    "Let go of who you thought they were.",
    "Healing isn’t linear. Be kind to yourself.",
    "Their silence is a message. Listen."
]

achievements = {
    "i love you": "🏆 Achievement Unlocked: Simped too soon",
    "love u": "🏆 Achievement Unlocked: Simped too soon",
    "luv u": "🏆 Achievement Unlocked: Simped too soon",
    "ily": "🏆 Achievement Unlocked: Simped too soon",
    "wyd": "🏆 Achievement Unlocked: Dry Texter Detected",
    "😭": "🏆 Achievement Unlocked: Certified Sadboi"
}

love_log = "love.log"


def log_attempt(msg, reply):
    with open(love_log, 'a') as f:
        f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent: '{msg}' | Outcome: {reply}\n")


def get_support_quote():
    if HAS_REQUESTS:
        try:
            response = requests.get("https://zenquotes.io/api/random", timeout=3)
            if response.status_code == 200:
                data = response.json()
                return data[0]['q'] + " —" + data[0]['a']
        except Exception:
            pass
    return random.choice(inspo_fallback)


def send_message(msg, debug=False):
    if msg.strip().lower() == "support":
        print("\n🫂 Support Mode Activated... Initializing healing protocol...")
        time.sleep(1.5)
        print("\n✨ Here's something gentle for your soul:")
        time.sleep(1.5)
        print("\n\"" + get_support_quote() + "\" ✨\n")
        time.sleep(1.5)
        print("💡 Tip: It's okay to pause. Your peace > their reply.")
        print("------------------------------------------------------------\n")
        return

    print(f"\n📤 Sending: '{msg}'")
    time.sleep(1.2)

    for keyword in achievements:
        if keyword in msg.lower():
            break
    else:
        if len(msg.strip().split()) == 1:
            print("\n💥 DryTextException: One word? That's all you got?")
            print("🏆 Achievement Unlocked: Elite Level Dry Texter")
            print("Pro TIP: Try more than 1 word!")
            log_attempt(msg, "DryTextException")
            return

    if random.randint(1, 100) == 69:
        reply = "She replied ❤️"
        print("👁️‍🗨️ Seen 2 days ago.")
        time.sleep(1.2)
        print(f"💌 {reply}")
        print("🏆 Achievement Unlocked: Against all odds")
        log_attempt(msg, reply)
        return

    print("👁️‍🗨️ Seen 2 days ago.")
    time.sleep(1.2)
    print("...No reply.")
    time.sleep(1.2)

    print("\n🧠 Overthinking initiated:")
    thoughts = random.sample(overthink_loops, 3)
    for i, thought in enumerate(thoughts):
        print(f"💭 Thought {i+1}: {thought}")
        time.sleep(1.2)

    unlocked = False
    for keyword in achievements:
        if keyword in msg.lower():
            print("\n💥 TooEarlyException: bruh. You said '" + keyword + "'. Bold choice.")
            print(achievements[keyword])
            unlocked = True

    if not unlocked:
        tip = random.choice(coping_mechanisms)
        print(f"\n[ Coping Tip ]: {tip}")
        print("⚠️  Emotional battery: " + str(random.randint(10, 30)) + "%")
        print("💥 Exception: BrokenHeartException")

    print("💬 Log: Still no reply. Still hoping. Still dumb.")
    print("------------------------------------------------------------\n")
    log_attempt(msg, "No reply")

    if debug:
        print("[DEBUG] cringeLevel: {}%".format(random.randint(60, 100)))
        print("[DEBUG] hopeLeft: {}%".format(random.randint(0, 20)))
        print("[DEBUG] ghostRate: {}%".format(random.randint(80, 100)))


def run_cli():
    print("❤️ Welcome to love-cli — where your heart gets rate-limited.")
    print("Type your message below (type 'exit' to quit, 'debug' to enable analytics, or 'support' for healing quotes):\n")

    debug_mode = False

    while True:
        try:
            user_input = input("> ")
            if user_input.lower() == 'exit':
                print("\n👋 Exiting love-cli. Remember: you deserve reciprocation.")
                break
            elif user_input.lower() == 'debug':
                debug_mode = True
                print("🧪 Debug mode activated: Emotional stats will now show up after each send.")
            elif len(user_input.strip()) == 0:
                print("😐 Empty texts don’t get replies either, king.")
            else:
                send_message(user_input, debug=debug_mode)
        except KeyboardInterrupt:
            print("\n\n🚪 Ctrl+C detected. Escaping emotional damage.")
            sys.exit(0)


if __name__ == '__main__':
    run_cli()
