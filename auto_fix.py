import re
import os
from github import Github
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
g = Github(token)

repo = g.get_repo("mosharishahab/Auto-test")
folder_path = "lib"

def process_file(content_file):
    file_content = content_file.decoded_content.decode()
    test_line = "// [AutoFix by GPT] Style added\n"

    new_content = re.sub(
        r'Text\(([^,)]+)\)',
        r'Text(\1, style: TextStyle(fontSize: 16))',
        file_content
    )

    if new_content != file_content:
        new_content = test_line + new_content
        repo.update_file(
            content_file.path,
            "AutoFix: added default style to Text widgets",
            new_content,
            content_file.sha
        )
        print(f"✅ Updated: {content_file.path}")
    else:
        print(f"⏩ No change: {content_file.path}")

try:
    contents = repo.get_contents(folder_path)
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "file" and file_content.name.endswith(".dart"):
            process_file(file_content)
        elif file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
except Exception as e:
    print(f"❌ Error: {e}")