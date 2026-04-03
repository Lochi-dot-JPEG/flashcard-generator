NOTE_FILE=$1

CONTENT=$(cat $NOTE_FILE)

MODEL=llama3.1:8b

if [[ $(ollama ls | grep "$MODEL") == "" ]]; then
		echo "LLM model not found in ollama. Installing now..."
		ollama pull "$MODEL"
fi

PROMPT="Generate flashcards in the format:

Q: Front of flashcard
A: Back of flashcard

If factual inaccuracies are found in the content, add an error section before flashcards. It must be in the format
Error: Description of error

Content start
$CONTENT
End of content

Do not include any other text or formatting in the response other than the flashcard text and errors in the flashcard content to be appended. Cover all vital content in the note."

OUTPUT="
AI OUTPUT:

$(ollama run "$MODEL" "$PROMPT")"

echo $OUTPUT >> $1


