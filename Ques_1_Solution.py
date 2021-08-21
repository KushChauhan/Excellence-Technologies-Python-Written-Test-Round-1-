import requests
import json

def get_response(posts_api, comments_api):
    posts_response = requests.get(url = posts_api).text
    comments_response = requests.get(url = comments_api).text

    posts_data = json.loads(posts_response)
    comments_data = json.loads(comments_response)
    # print(posts_data)
    # print(comments_data)

    # assigned comment to its respective post
    for post in posts_data:
        post_comment = []
        post['post_comment'] = post_comment
        for comment in comments_data:
            if(post['id'] == comment['postId']):
                post_comment.append(comment['body'])
                post['post_comment']= post_comment

    # print(posts_data)
    # print(comments_data)

    # combined data of both posts/comments
    combined_data = {}

    combined_data["posts"] = posts_data
    combined_data["comments"] = comments_data
    # print(combined_data)

    json_response = json.dumps(combined_data)
    # print(json_response)
    # print()

    return json_response

if __name__=='__main__':

    posts_api = "https://my-json-server.typicode.com/typicode/demo/posts"
    comments_api = "https://my-json-server.typicode.com/typicode/demo/comments"

    response = get_response(posts_api, comments_api)
    print(response)