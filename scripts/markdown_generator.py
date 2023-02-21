from pathlib import Path
import json
import tags

with open("./judges.json", "r") as json_file:
    judges = json.load(json_file)

tags_list = tags.tags_dict()

def markdown_href(title, url, open_in_new_tab = True):
    url = str(url)
    result = "[" + title + "](" + url + ")"
    if open_in_new_tab:
        result = result + "{:target=\"_blank\"}"

        return result

def judge_div(judge):
    if not judge in judges:
        return judge

    result = ""
    if "icon" in judges[judge].keys():
        result = ":" + judges[judge]["icon"] + ": "
    
    result = result + markdown_href(judges[judge]["name"], judges[judge]["url"]) 
    return result

def tag_link(tag):
    if not tag in tags_list.keys():
        return tag
    return markdown_href(tags_list[tag]["blog_title"], Path("/Shaazzz-Guide/" + tags_list[tag]["site_path"]).with_suffix(""))

def tag_spoiler(tags):
    return "<details> <summary>Spoiler</summary> <ul>" + \
        ' '.join(list(map(lambda tag : "<li>" + tag_link(tag) + "</li>", tags))) + \
             "</ul> </details>"

def create_blur_spoiler(obj):
    return "<div class=\"blur-spoiler\">" + obj + "</div>"

def create_problem_row(problem):
    problem_name = markdown_href(problem["name"], problem["url"])
    if problem["judge"] == "المپیادی":
        problem_name = create_blur_spoiler(problem_name)
    
    return "|" + problem_name + "|" + problem["difficulty"] + \
        "|" + tag_spoiler(problem["tags"]) + "|" + judge_div(problem["judge"]) + "|"

def admonition_markdown(admonition):
    return "??? " + admonition["type"] + " \"" + admonition["title"] + "\"\n" + \
        ('    '.join(('\n' + admonition["content"].lstrip()).splitlines(True)))  + "\n"


def create_admonitions(problems):
    admonitions = set()
    for problem in problems:
        if problem["judge"] in judges.keys():
            if "admonition" in judges[problem["judge"]].keys():
                admonitions.add(admonition_markdown(judges[problem["judge"]]["admonition"]))

    return "\n".join(admonitions)

def generate_markdown(blog_path, blog_name, description, problems):
    if problems:
        problems = sorted(problems, key=lambda x : int(x["difficulty"]))
    file_name = blog_name + ".md"
    with open(blog_path, "w") as markdown_file:
        markdown_file.write("--- \n")
        markdown_file.write("hide:\n")
        markdown_file.write("  - footer\n")
        markdown_file.write("comments: true\n")
        markdown_file.write("---\n")

        markdown_file.write("# " + blog_name + "\n\n")
        
        if description:
            if problems:
                markdown_file.write("## توضیحات \n")
            markdown_file.write(description)
            markdown_file.write("\n")

        if problems:
            if description:
                markdown_file.write("## سوال ها \n")
            markdown_file.write(create_admonitions(problems))
            markdown_file.write("| سوال | سختی | تگ ها | جاج | \n")
            markdown_file.write("| :-----: | :----: | :----: | :----: | \n")
            for problem in problems:
                markdown_file.write(create_problem_row(problem) + "\n")
