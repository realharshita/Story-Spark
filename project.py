from llmware.models import ModelCatalog
from llmware.prompts import Prompt

def generate_story_ideas(model_name):
    model = Prompt().load_model(model_name)
    current_story = ""

    def get_story_details():
        genre = input("Enter story genre (e.g., fantasy, sci-fi): ")
        character = input("Describe the main character (briefly): ")
        setting = input("Describe the story setting (briefly): ")
        conflict = input("Describe the initial conflict the character faces: ")
        return genre, character, setting, conflict

    genre, character, setting, conflict = get_story_details()

    while True:
        user_input = f"Write a suspenseful and character-driven continuation of the story:\n{current_story}" \
                     f"\nGenre: {genre}\nCharacter: {character}\nSetting: {setting}\nConflict: {conflict}"
        
        output = model.prompt_main(user_input, prompt_name="generate_story", temperature=0.7)
        story = output["llm_response"].strip("\n")

        current_story += story + "\n\n"
        
        print("*** Generated Story ***")
        print(current_story)
        print("*** End of Generated Story ***")
        
        user_feedback = input("Do you want to continue the story (y/n) or are you happy with this length? ").lower()

        if user_feedback == 'n':
            break

if __name__ == "__main__":
    generate_story_ideas("phi-3-gguf")
