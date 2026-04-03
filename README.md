# LLM Flashcard Generation

Bash script that generates flashcards based on the contents of a text file. 

It also tries to check for logical errors within each note.

It uses ollama to interface with llama3.1:8b to run the llm locally on my pc. 

Used to automate tediously creating flashcards for my obsidian vault.

## Workflow

- Create notes using obsidian
- Tag those notes with #needs-flashcards
- Run a script that looks through each note for that tag, and appends flashcards to the end
- Review for any errors flagged by the llm in the note and fix them.
- Use obsidian to anki converter to scan all flashcards and import them into anki
- Memorise content

## Roadmap

- [x] Append flashcards to a note file
- [ ] Omit markdown frontmatter from the file given in the prompt
- [ ] Scan directory for the #needs-flashcards tag in the markdown frontmatter
- [ ] Loop through each file with the #needs-flashcard tag

