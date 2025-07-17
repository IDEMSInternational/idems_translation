import json
import os
from pathlib import Path

def compose_files(config_path):
    with open(config_path) as config_file:
        data = json.load(config_file)

        in_dir = Path(data['CoreFiles'])
        out_dir = Path(data['ComposeResult'])
        out_dir.mkdir(parents=True, exist_ok=True)

        core_groups = data['CoreGroups']
        split_groups_full = data['SplitGroups']
        split_groups = [row[0] for row in split_groups_full]

    compose(in_dir, out_dir, core_groups, split_groups)

def compose(in_dir, out_dir, core_groups, split_groups):
    # Initialize all split group buckets and 'main'
    contents = {group: [] for group in split_groups}
    contents["main"] = []

    # Loop through all core groups
    for group_name, subfolders in core_groups:
        print(f"\nProcessing group: {group_name}")
        contents = create_list(in_dir, group_name, subfolders, split_groups, contents)

    # Write all output groups, including 'main'
    for group_name, items in contents.items():
        print(f"Writing '{group_name}' with {len(items)} items.")
        write_json(out_dir, group_name, items)

def create_list(in_dir, group_name, subfolders, split_groups, contents):
    base_group_path = in_dir / group_name

    # Optional: accumulate files at the top level of group folder (e.g., global/)
    if base_group_path.exists() and base_group_path.is_dir():
        for file in base_group_path.iterdir():
            if file.is_file():
                print(f"Adding file to 'main' from {file}")
                contents["main"].append(read_json(file))

    for folder in subfolders:
        if not folder:  # skip empty strings (e.g., [""])
            continue

        folder_path = base_group_path / folder
        print(f"Looking into: {folder_path} | Split group? {'Yes' if folder in split_groups else 'No'}")

        if not folder_path.exists():
            print(f"⚠️  Warning: Folder not found - {folder_path}")
            continue

        files = accumulate_json_files(folder_path)

        if folder in split_groups:
            contents[folder] += files
        else:
            contents["main"] += files

    return contents

def accumulate_json_files(dir_path):
    acc = []
    if not dir_path.exists():
        return acc

    for file_name in os.listdir(dir_path):
        file_path = dir_path / file_name
        if file_path.is_file():
            acc.append(read_json(file_path))

    return acc

def read_json(file_path):
    with open(file_path, encoding='utf-8') as json_file:
        return json.load(json_file)

def write_json(out_dir, group_name, contents):
    file_path = out_dir / f'{group_name}.json'
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(contents, json_file, ensure_ascii=False, indent=2)
