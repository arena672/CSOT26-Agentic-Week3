import os
import sys
import json
import uuid
from dotenv import load_dotenv
from openai import OpenAI

from tools.web import web_search, web_fetch
from tools.files import read_file, write_file, list_files, edit_file
from tools.papers import paper_search, read_paper

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)

MODEL = "deepseek/deepseek-v4-flash"

class Agent:

    def __init__(self):

        with open("AGENTS.md", "r", encoding="utf-8") as f:
            rules = f.read()

        self.messages = [
            {
                "role": "system",
                "content": rules
            }
        ]

        self.session_id = str(uuid.uuid4())

        self.tools = {
            "web_search": web_search,
            "web_fetch": web_fetch,
            "paper_search": paper_search,
            "read_paper": read_paper,
            "read_file": read_file,
            "write_file": write_file,
            "list_files": list_files,
            "edit_file": edit_file
        }

    def save_session(self):

        os.makedirs(".agent/sessions", exist_ok=True)

        filename = f".agent/sessions/{self.session_id}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(
                self.messages,
                f,
                indent=2
            )

    def load_session(self, session_id):

        filename = f".agent/sessions/{session_id}.json"

        if not os.path.exists(filename):
            print("Session not found.")
            return

        with open(filename, "r", encoding="utf-8") as f:
            self.messages = json.load(f)

        self.session_id = session_id

        print("Loaded session:", session_id)
        
    def chat(self, user_message):

      self.messages.append(
          {
              "role": "user",
              "content": user_message
          }
      )

      response = client.chat.completions.create(
          model=MODEL,
          messages=self.messages
      )

      answer = response.choices[0].message.content

      self.messages.append(
          {
              "role": "assistant",
              "content": answer
          }
      )

      self.save_session()
      
      return answer

    def list_sessions(self):

        files = os.listdir(".agent/sessions")

        return [
            file[:-5]
            for file in files
            if file.endswith(".json")
        ]

class REPLAgent(Agent):

    def run(self):

        while True:

            query = input("> ")

            if query.lower() == "exit":
                break

            if query == "/sessions":

                sessions = self.list_sessions()

                print("\nSaved sessions:")

                for s in sessions:
                    print(s)

                continue

            answer = self.chat(query)

            print(answer)

    def run_once(self, question):

        answer = self.chat(question)

        print(answer)


if __name__ == "__main__":

    if "--tui" in sys.argv:

        from tui import TUIAgent

        agent = TUIAgent()

        agent.run()

    else:

        agent = REPLAgent()

        if len(sys.argv) > 1:

            question = " ".join(sys.argv[1:])

            agent.run_once(question)

        else:

            session_id = input(
                "Session ID to load (blank for new): "
            ).strip()

            if session_id:
                agent.load_session(session_id)

            agent.run()