import streamlit as st
from data import DATA, TEXTS

texts = TEXTS[st.session_state.get("language", "en")]
projects = DATA[st.session_state.get("language", "en")]["projects"]

st.title(texts["nav"]["projects"])


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
        
                



tags = all_tags(projects)
choosen = st.multiselect(texts["projects"]["tag_filter"], options=tags)
filtered_list = filter_projects(projects, choosen)

sort_order = st.radio(
    texts["projects"]["sort_year"],
    options=[texts["projects"]["newest"], texts["projects"]["oldest"]]
)

filtered_list.sort(
    key=lambda p: int(p["year"]),
    reverse=(sort_order == texts["projects"]["newest"]),
)

result_text = texts["projects"]["found_many"] if len(filtered_list) > 1 else texts["projects"]["found_one"]
st.write(f"**{len(filtered_list)}** {result_text}")

cols = st.columns(2)

for i, project in enumerate(filtered_list):
    with cols[i % 2]:
        with st.container(border=True):
            if project.get("image"):
                st.image(
                    project["image"], use_container_width=True
            ) 
            st.subheader(project["title"])
            st.write(project["description"])
            tags_str = ", ".join(project["tags"])
            st.caption(
                f"{texts['projects']['tags']} : {tags_str} | "
                f"{texts['projects']['year']} : {project['year']}"
            )
            if project.get("link"):
                st.link_button(texts["projects"]["see_code"], project["link"])