import os

def main():
    joke = "I asked my AI agent to fix a typo in the README, and it refactored the project into a distributed Kubernetes microservice cluster written in Brainfuck."
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
