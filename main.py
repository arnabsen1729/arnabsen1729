#
#  Generate a README which will have 5 latest blogs from arnabsen.rocks
#
import feedparser


def getEntries(url, count):
    d = feedparser.parse(url)
    return [
        {
            'title': entry.title,
            'link': entry.link,
            'pubDate': ' '.join(entry.published.split(' ')[1:4])
        }
        for entry in d.entries[:count]
    ]


URL = "https://arnabsen.rocks/index.xml"

DATA = '''
<h1 align="center">Hi, Arnab here 👋</h1>

<p align="center" style="display: inline">
<a href="https://arnabsen.rocks/"><img src="https://img.shields.io/badge/BLOG-arnabsen.rocks-lightgrey/?style=for-the-badge&color=fedcba"></a>
<img src="https://img.shields.io/github/followers/arnabsen1729?style=for-the-badge">
<img src="https://img.shields.io/github/stars/arnabsen1729?style=for-the-badge">
<a href="https://www.linkedin.com/in/arnab-sen-b6950a194/"><img src="https://img.shields.io/badge/-Arnab-blue?style=for-the-badge&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/arnab-sen-b6950a194/)](https://www.linkedin.com/in/arnab-sen-b6950a194/"></a>
</p>


- 👨‍🎓 Sophomore at **Dept. of Computer Science and Technology, IIEST, Shibpur**
- 💻 Prior experience with **ReactJS, NuxtJS, VueJS, JavaScript, Python, Flutter, C** and **C++**
- 📫 My social profiles **https://linktr.ee/arnabsen**

👨‍💻 I am a Software Developer with experience in Web Development, Automation, and Content Writing. For the past 2 years, I have worked around an immense variety of technologies and frameworks such as React, Vue in Frontend and Node, Flask, Rails in the Backend.
You can know more about me [here](https://arnabsen.rocks/about).

Read my CV <a href="https://arnabsen.rocks/resume.pdf">here.</a>

<hr>

'''

STATS = '''
<hr>

|<img src="https://github-readme-stats.vercel.app/api?username=arnabsen1729&show_icons=true&theme=radical&text_color=fff&title_color=F58B02&icon_color=F58B02"/>|<img src="https://github-readme-streak-stats.herokuapp.com/?user=arnabsen1729&theme=dark&hide_border=true"/>|
|---|---|
<img src="https://activity-graph.herokuapp.com/graph?username=arnabsen1729&theme=github" />

<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/arnabsen1729/arnabsen1729/Build%20README?style=for-the-badge" align="right">
'''

if __name__ == "__main__":
    with open("README.md", 'w') as f:
        f.write(DATA)
        f.write(
            "## My Latest Blogs\n\n"
            "This is a list of the latest blogs from [arnabsen.rocks](https://arnabsen.rocks).\n\n"
        )
        f.write("| Blog | Date |\n")
        f.write("| --- | --- |\n")
        for entry in getEntries(URL, 5):
            f.write("| [{title}]({link}) | {pubDate} |\n".format(**entry))

        f.write(STATS)
