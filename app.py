import json
from difflib import get_close_matches as get_close_result

def load_database():
    database = {"prompts": []}
    try:
        with open('C:\\Users\\...\\OneDrive\\...\\GitHub\\...\\...\\database.json', 'r', encoding='utf-8') as file:
            database = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading database: {e}")
    return database
    
def write_database(dataset):
    with open('C:\\Users\\...\\OneDrive\\...\\GitHub\\...\\...\\database.json', 'w', encoding='utf-8') as file: 
        json.dump(dataset, file, indent=2, ensure_ascii=False)

def find_close_result(prompt, promptset):
    match_data = get_close_result(prompt, promptset, n=1, cutoff=0.7)
    return match_data[0] if match_data else None

def find_answer(prompt, database):
    for prompt_data in database["prompts"]:
        if prompt_data["Terms"] == prompt or prompt_data["Meanings"] == prompt or prompt_data["Meanings2"] == prompt or prompt_data["Meanings3"] == prompt:
            return prompt_data
    return None

def ai_bot():
    database = load_database()

    while True:
        prompt = input("You: ")
        
        if prompt.lower() == "quit":
            break

        prompts_list = [prompt_data["Terms"] for prompt_data in database["prompts"]] + \
                    [prompt_data["Meanings"] for prompt_data in database["prompts"]] + \
                    [prompt_data["Meanings2"] for prompt_data in database["prompts"]] + \
                    [prompt_data["Meanings3"] for prompt_data in database["prompts"]]

        get_result = find_close_result(prompt, prompts_list)

        if get_result:
            prompt_data = find_answer(get_result, database)
            if prompt_data:
                if prompt_data["Terms"] == prompt:
                    answer = f"{prompt_data['Meanings']}, {prompt_data['Meanings2']}, {prompt_data['Meanings3']}"
                else:
                    answer = prompt_data["Terms"]
                print(f"Bot: {answer}")
        else:
            print("Bot: I don't understand?")
            new_answer = input("Please teach me or type 'quit' to exit: ")

            if new_answer.lower() == 'quit':
                break
            elif new_answer.lower() == 'continue':
                continue
            else:
                terms = input("Please provide the main term (e.g., 'about'): ")
                meanings = input("Please provide the first meaning: ")
                meanings2 = input("Please provide the second meaning: ")
                meanings3 = input("Please provide the third meaning: ")

                database["prompts"].append({
                    "Terms": terms,
                    "Meanings": meanings,
                    "Meanings2": meanings2,
                    "Meanings3": meanings3
                })

                write_database(database)
                print("Bot: Thank you.")

if __name__ == '__main__':
    ai_bot()
