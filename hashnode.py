import requests
import os
from github import Github, GithubException, InputGitAuthor

base_url="https://apoorvtyagi.tech/"
START_COMMENT = '<!--START_SECTION:blog-->'
END_COMMENT = '<!--END_SECTION:blog-->'
listReg = f"{START_COMMENT}[\\s\\S]+{END_COMMENT}"
ghtoken = os.getenv('INPUT_GH_TOKEN')

def decode_readme(data: str):
    '''Decode the contents of old readme'''
    decoded_bytes = base64.b64decode(data)
    return str(decoded_bytes, 'utf-8')


def generate_new_readme(stats: str, readme: str):
    '''Generate a new Readme.md'''
    stats_in_readme = f"{START_COMMENT}\n{stats}\n{END_COMMENT}"
    return re.sub(listReg, stats_in_readme, readme)

def run_query(query): # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post('https://api.hashnode.com/', json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

        
def get_stats():
    stats=''
    query = """
    {
      user(username: "apoorvtyagi") {
        publication {
          posts(page: 0) {
            slug
            title
          }
        }
      }
    }
    """

    result = run_query(query)
    out=result['data']['user']['publication']['posts']

    for i in range (0,3):
        stats+='[{}]({})\n\n'.format(base_url+out[i]['slug'],out[i]['title'])

    return stats

if __name__ == '__main__':
    try:
        """
        if ghtoken is None:
            raise Exception('Token not available')
        g = Github(ghtoken)
        """
        waka_stats=get_stats
        repo = "ApoorvTyagi/blog"
        contents = repo.get_readme()
        rdmd = decode_readme(contents.content)
        new_readme = generate_new_readme(stats=waka_stats, readme=rdmd)
        committer = InputGitAuthor('blog-bot', 'blog-bot@example.com')
        if new_readme != rdmd:
            repo.update_file(path=contents.path, message='Updated with blogs',
                             content=new_readme, sha=contents.sha, branch='master',
                             committer=committer)
            print("blogs updated")
        except Exception as e:
            traceback.print_exc()
            print("Exception Occurred " + str(e))
