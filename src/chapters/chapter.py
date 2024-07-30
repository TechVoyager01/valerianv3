# Storyline
chapter_1_story = """
Chapter 1: The Call to Adventure
In the bustling capital city of Galador, Valerian hears rumors about the ancient city of Thaemus and its legendary artifact that grants eternal youth. 
Driven by curiosity and ambition, he decides to embark on a quest to uncover the secrets of Thaemus. 
Before leaving, he gathers supplies and meets an old sage who gives him a mystical map and some cryptic advice.
You are sent on you way to discover the next clue....
"""

chapter_2_story = """
Chapter 2: The Path of Trials
Valerian ventures into the dense and mystical Enchanted Forest surrounding Thaemus. 
He faces various challenges and encounters that test his strength, intelligence, and courage. 
During his journey, he befriends a magical creature who aids him in overcoming the forest's dangers.
"""

chapter_3_story = """
Chapter 3: The Treacherous Mountains
Valerian continues his journey through the rugged and perilous Treacherous Mountains. 
He navigates through difficult terrain, environmental hazards, and formidable enemies. 
Along the way, he uncovers more about the history of Thaemus and its artifact.
"""

chapter_4_story = """
Chapter 4: The Ruins of Thaemus
Valerian finally reaches the ancient and forgotten city of Thaemus. 
He must navigate through the ruins, solve intricate puzzles, and defeat powerful guardians to reach the inner sanctum where the artifact is kept. 
The final confrontation tests Valerian's resolve and worthiness to obtain the artifact.
"""

class Chapter:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def start(self):
        print(f"Starting chapter: {self.title}")
        print(self.description)
        # Add logic to start the chapter

    def complete(self):
        self.completed = True
        print(f"Chapter {self.title} completed!")

# Example chapters
chapter_1_story = Chapter(
    title="Chapter 1: The Beginning",
    description="You wake up in a mysterious forest with no memory of how you got there..."
)

chapter_2_story = Chapter(
    title="Chapter 2: The Journey",
    description="You decide to venture deeper into the forest, seeking answers..."
)

chapter_3_story = Chapter(
    title="Chapter 3: The Encounter",
    description="You encounter a strange creature that seems to know you..."
)

chapter_4_story = Chapter(
    title="Chapter 4: The Revelation",
    description="The creature reveals a shocking truth about your past..."
)

# List of all chapters
chapters = [chapter_1_story, chapter_2_story, chapter_3_story, chapter_4_story]