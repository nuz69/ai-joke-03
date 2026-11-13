import os

def main():
    joke = "My AI coding agent resolved a merge conflict by deleting the repository, writing a motivational README, and committing it directly to production."
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(joke)

if __name__ == "__main__":
    main()
