from string import Template
 
repo_link = "[![Github Repo](https://img.shields.io/badge/$user-$frepo-blue?style=flat-square)](https://github.com/$user/$repo)"
stars = "![GitHub Repo stars](https://img.shields.io/github/stars/$user/$repo?style=flat-square)"
forks = "![GitHub forks](https://img.shields.io/github/forks/$user/$repo?style=flat-square)"
template = Template(f"| {repo_link} | {stars} | {forks} | <$link> |")

contributions = [
    'https://github.com/iluwatar/java-design-patterns/pull/1956',
    'https://github.com/bitcoin/bitcoin/pull/23907',
    'https://github.com/bitcoin/bitcoin/pull/22902',
    'https://github.com/sindresorhus/emoj/pull/53',
    'https://github.com/chinchang/web-maker/pull/501',
    'https://github.com/chinchang/web-maker/pull/502',
    'https://github.com/chinchang/web-maker/pull/505',
    'https://github.com/chinchang/web-maker/pull/508',
    'https://github.com/chinchang/web-maker/pull/515',
    'https://github.com/kokoye2007/wifi-qr/pull/11',
]

print('''| 🎁 Repo | ⭐ Stars | 📚 Forks | ✨ Contribution |
| --- | --- | --- | --- |''')

for contribution in contributions:
    temp = contribution.replace('https://', '').replace('http://', '')
    _, user, repo, _, pull = temp.split('/')
    frepo = repo.replace('-', '--')
    print(template.substitute(user=user, repo=repo, frepo=frepo, link=contribution))
