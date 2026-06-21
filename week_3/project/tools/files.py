import os


def read_file(path, start_line=1, read_lines=50):

    try:

        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        start = start_line - 1
        end = start + read_lines

        content = []

        for i, line in enumerate(lines[start:end], start=start_line):
            content.append(f"{i}: {line.rstrip()}")

        has_more = end < len(lines)

        return {
            "content": "\n".join(content),
            "start_line": start_line,
            "end_line": min(end, len(lines)),
            "has_more": has_more
        }

    except Exception as e:

        return {
            "error": str(e)
        }

def write_file(path, content):

    try:

        os.makedirs(
            os.path.dirname(path),
            exist_ok=True
        )

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

        return {
            "success": True,
            "path": path
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def list_files(path="."):

    try:

        files = []

        for root, dirs, filenames in os.walk(path):

            for file in filenames:

                files.append(
                    os.path.join(root, file)
                )

        return {
            "files": files
        }

    except Exception as e:

        return {
            "error": str(e)
        }


def edit_file(path, operation, old_text="", new_text=""):

    try:
        with open(path,"r",encoding="utf-8") as f:
            old_content = f.read()

        if operation=="append":
            updated = old_content + "\n" + new_text

        elif operation=="replace":
            updated = old_content.replace(old_text,new_text)

        elif operation=="delete":
            updated = old_content.replace(old_text,"")

        else:
            return {"error":"Unknown operation"}

        with open(path,"w",encoding="utf-8") as f:
            f.write(updated)

        return {
            "success":True,
            "diff_preview":{
                "before":old_content,
                "after":updated
            }
        }

    except Exception as e:
        return {"error":str(e)}