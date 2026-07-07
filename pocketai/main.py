from ai import ask_ai
print("=" * 45)
print("                   POCKET AI")
print("=" * 45)
print("Type /help for commands.")
print()
while True:
    prompt = input("You > ")
    if not prompt.strip():
        continue
    if prompt.lower() == "/bye":
        print("AI  > Goodbye! 👋")
        break
    if prompt.lower() == "/help":
        print("\nCommands:")
        print("  /help  - Show this help")
        print("  /bye   - Exit PocketAI")
        continue
    result = ask_ai(prompt)
    
    print("AI  >", result)
    print()