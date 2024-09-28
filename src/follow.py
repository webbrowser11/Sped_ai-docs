import scratchattach as attach
import time


print("Creating session")
session = attach.login("sped_AI", "weluvai")
print("Connecting studio")
studio = session.connect_studio("35292763")
off = 41000
index = 0
while True:
    print(f"Fetching projects with offset of {off}")
    projects = studio.projects(limit=20, offset=off)
    for project_info in projects:
        index += 1
        project = session.connect_project(project_info['id'])
        project.get_author().follow()
        print(f"{index}: Followed author {project.get_author().username} from project {project.title}")
    off += 20
    time.sleep(60)
