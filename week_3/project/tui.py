from agent import Agent


class TUIAgent(Agent):

    def run(self):

        print("TUI Agent started")

        while True:

            query = input("TUI> ")

            if query.lower() == "exit":
                break

            answer = self.chat(query)

            print(answer)