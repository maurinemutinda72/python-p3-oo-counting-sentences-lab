class MyString:
    def __init__(self, value=''):
        """Initialize MyString with a value, defaulting to empty string."""
        self.value = value  # Use the setter for validation

    def get_value(self):
        """Getter for value."""
        return self._value

    def set_value(self, value):
        """Setter for value with string validation."""
        if not isinstance(value, str):
            print("The value must be a string.")
            return  # Exit early without setting the value
        self._value = value

    value = property(get_value, set_value)

    def is_sentence(self):
        """Return True if value ends with a period, False otherwise."""
        return self.value.endswith('.')

    def is_question(self):
        """Return True if value ends with a question mark, False otherwise."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Return True if value ends with an exclamation mark, False otherwise."""
        return self.value.endswith('!')

    def count_sentences(self):
        """Return the number of sentences in value."""
        if not self.value:  # Handle empty string case
            return 0
        
        # Replace ! and ? with . to standardize sentence endings
        text = self.value.replace('!', '.').replace('?', '.')
        # Split on . and filter out empty strings or whitespace-only strings
        sentences = [s.strip() for s in text.split('.') if s.strip()]
        return len(sentences)