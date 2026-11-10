import streamlit as st
from data import PROJECTS


def all_tags(projects):
    tags = set()

    for project in projects:
        for tag in project["tags"]:
            tags.add(tag)

    return sorted(list(tags))


def filter_projects(projects, choosen):
    filtered_projects = []

    if not choosen: 
        return projects
    
    for project in projects:
        has_tag = False
        for tag in choosen:
            if tag in project["tags"]:
                has_tag = True
                break
        if has_tag:
            filtered_projects.append(project)
    return filtered_projects
        
                



tags = all_tags(PROJECTS)
choosen =  st.multiselect("Filtre par tag", options=tags)
filtered_list = filter_projects(PROJECTS, choosen)

sort_order = st.radio(
    "Tri par année", 
    options=["Plus récents", "Plus anciens"]
)


s = "s" if len(filtered_list) > 1 else ""
st.write(f"**{len(filtered_list)}** projet{s} trouvé{s}")

cols = st.columns(2)

for i, project in enumerate(filtered_list):
    with cols[i % 2]:
        with st.container(border=True):
            st.subheader(project["title"])
            st.write(project["description"])
            tags_str = ", ".join(project["tags"])
            st.caption(f"Tags : {tags_str} | Année : {project['year']}")
            if project.get("link"):
                st.link_button("See the code", project["link"])