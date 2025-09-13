class llms:

    token_size = 100

    def __init__(self,query):
        self.query = query

    def openai(self):
        print(f"I am Openai. You are {self.query}")

    def claude(self):
        print("I am Claude")

    def llama(self):
        print("I am llama")

if __name__ == "__main__":

    obj = llms("Hey, I am Anabel")
    obj.openai()