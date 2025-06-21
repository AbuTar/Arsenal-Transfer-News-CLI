from fetcher import fetch_latest_news
import time

# This holds the accounts that are trusted sources and I will only webscrape from those accounts
accounts = {
    "Fabrizio Romano": "FabrizioRomano",
    "David Ornstein": "David_Ornstein",
    "Sami Mokbel": "SamiMokbel_BBC",
    "Hand of Arsenal": "HandofArsenal"
}

posts_to_retrieve = 5
history_file = "Arsenal_Transfer_News.txt"

# Menu for selecting what to do
def main_menu():
    while True:
        print("\nArsenal Transfer News CLI")
        print("1. Fetch latest news")
        print("2. View history")
        print("3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            fetcher()
        elif choice == '2':
            view_history()
        elif choice == '3':
            break
        else:
            print("Invalid option. Try again.")

def fetcher():
    # Creating a dictionary to save news that have been fetched
    news = {}

    # Statement to inform user about what is currently happening
    print("\n🔍 Fetching the latest Arsenal transfer tweets...\n")

    # Getting an error about too many requests within a certain time frame so had to add a sleep timer
    for name, username in accounts.items():
        print(f"🧾 {name} (@{username})")
        tweets = fetch_latest_news(username, posts_to_retrieve)

        news[name] = tweets

        if not tweets:
            print("⚠️ No tweets found or an error occurred.\n")
        else:
            for timestamp, text in tweets:
                print(f"   🕒 {timestamp.strftime('%Y-%m-%d %H:%M')} - {text.strip()}\n")
        print("-" * 60)

        # Saving one user's tweets at a time to avoid duplicates in the saved file
        save_news("Arsenal_Transfer_News.txt", {name: tweets})
        time.sleep(3)


def save_news(filename, data):
    with open(filename, 'a', encoding='utf-8') as file:
        for name, tweets in data.items():
            file.write(f"🧾 {name}\n")
            for timestamp, text in tweets:
                file.write(f"   🕒 {timestamp.strftime('%Y-%m-%d %H:%M')} - {text.strip()}\n")
            file.write("-" * 60 + "\n")

def view_history():
    try:
        with open(history_file, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n📜 Transfer News History:\n")
            print(content)
    except FileNotFoundError:
        print("❌ No history found. Run 'Fetch latest news' first.")

if __name__ == "__main__":
    main_menu()





  
