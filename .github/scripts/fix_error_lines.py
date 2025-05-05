import os
import re
from github import Github
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
repo_name = "mosharishahab/Auto-test"
folder_path = "lib"

g = Github(token)
repo = g.get_repo(repo_name)

# تعریف الگوهای اصلاحی
fixes = [
    {
        "pattern": r"e\.message\.toString\(\s*,\s*style: TextStyle\([^)]+\)\)",
        "replacement": "e.message.toString(), style: TextStyle(fontSize: 16)"
    },
    {
        "pattern": r"\bText\(([^,)]+)\)",
        "replacement": r'Text(\1, style: TextStyle(fontSize: 16))'
    }
]

def process_file(content_file):
    file_path = content_file.path
    print(f"🧪 Processing: {file_path}")

    try:
        file_content = content_file.decoded_content.decode()
        original_content = file_content

        for fix in fixes:
            file_content = re.sub(fix["pattern"], fix["replacement"], file_content)

        if file_content != original_content:
            if not file_content.startswith("// [AutoFix by GPT]"):
                file_content = "// [AutoFix by GPT]\n" + file_content

            repo.update_file(
                content_file.path,
                "AutoFix: applied common Dart fixes",
                file_content,
                content_file.sha
            )
            print(f"✅ Fixed: {file_path}")
        else:
            print(f"⏩ No changes: {file_path}")
    except Exception as e:
        print(f"❌ Error updating {file_path}: {e}")

def walk_and_fix():
    contents = repo.get_contents(folder_path)
    while contents:
        file = contents.pop(0)
        if file.type == "file" and file.name.endswith(".dart"):
            process_file(file)
        elif file.type == "dir":
            contents.extend(repo.get_contents(file.path))

if __name__ == "__main__":
    walk_and_fix()
