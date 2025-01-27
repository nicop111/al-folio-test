import os


tags: list = []
categories: list = []

# read in the .md files from _posts folder in this directory one by one
for file in os.listdir("_posts"):
    if file.endswith(".md"):
        with open(f"_posts/{file}", "r") as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith("tags:"):
                    tags.extend(line.split(":")[1].strip().split(","))
                if line.startswith("categories:"):
                    categories.extend(line.split(":")[1].strip().split(","))

# remove [ and ] and whitespaces at the beginning or end of a tag from the tags
tags = [tag.strip().strip("[]") for tag in tags]
categories = [category.strip().strip("[]") for category in categories]

# order the tags and categories. The more often a tag or category appears, the higher it is in the list, then remove duplicates
tags = sorted(tags, key=tags.count, reverse=True)
categories = sorted(categories, key=categories.count, reverse=True)

# Print the tags and categories
print("display_tags: " + str(tags))
print("display_categories: " + str(categories))