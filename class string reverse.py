class StringReverser:
    def __init__(self, input_string):
        self.input_string = input_string
    def reverse_words(self):
        
        words = self.input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
if __name__ == "__main__":
    input_str = "Hello world this is Python"
    reverser = StringReverser(input_str)
    reversed_str = reverser.reverse_words()
    print(reversed_str)