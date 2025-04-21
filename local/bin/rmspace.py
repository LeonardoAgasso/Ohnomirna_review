import os

def remove_spaces_in_files(folder_path, file_extension=".tsv"):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(file_extension):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                content = content.replace('\t ', '\t')  # Remove space following tabs
                content = content.replace(' \t', '\t')  # Remove space preceding tabs
                with open(file_path, 'w') as f:
                    f.write(content)

if __name__ == "__main__":
    folder_path = "../../dataset/6_MotifsEnrichment/test_bifan_pval/output/"
    remove_spaces_in_files(folder_path)