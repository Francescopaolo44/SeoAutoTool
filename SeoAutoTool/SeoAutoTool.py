# SeoAutoTool to optimize website, create share web for Seo

import sys
import json
import facebook
import requests
# ----------------------function----------------------









#define settings to add account detail
def settings():
    print("Choose an action: \n"
          "- (R) read config file"
          "- (W) write new account \n")

    choice = input("What do you want to do?").lower()

    if choice == "r":
        # open config.json file (read)
        account = input("Insert account name").lower()
        with open("config.json", "r") as data_file:
            data = json.load(data_file)
            print(data[account + '_' + 'id'])
            print(data[account + '_' + 'access_token'])

            # close
            data_file.close()

    if choice == "w":
        # open config.json file (write)
        account = input("insert account name").lower()
        id = input("insert page id").lower()
        access_token = input("insert access token").lower()
        data = {}
        data['account'] = account
        data[account + '_' + 'id'] = id
        data[account + '_' + 'access_token'] = access_token
        with open("config.json", "w") as data_file:
            data_file.write(json.dumps(data))

        # close
        data_file.close()

def facebook_option():
    print("Choose an action: \n"
          "- (P) post a message on page"
          "- (G) post message on group \n")

    choice = input("What do you want to do?").lower()

    if choice == "p":

        account = input("insert account").lower()

        with open("config.json", "r") as data_file:
            data = json.load(data_file)

            id = data[account + '_' + 'id']
            token = data[account + '_' + 'access_token']

        # close
        data_file.close()

        cfg = {
            'page_id': id,
            'access_token': token,
        }

        api = get_api(cfg)
        msg = input("insert post message")

        attachment = {
            'name': 'Oltremare',
            'link': 'https://www.facebook.com/permalink.php?story_fbid=805209756301573&id=771403016348914',
            'caption': 'Scopri oltremare',
            'description': 'bla bla bla bla',
        }


        status = api.put_wall_post(msg, attachment=attachment)

    if choice == "g":
        account = input("insert account").lower()
        with open("config.json", "r") as data_file:
            data = json.load(data_file)

            id = data[account + '_' + 'id']
            token = data[account + '_' + 'access_token']

        # close
        data_file.close()

        post_on_group(token)

    if choice == "r":
        account = input("insert account").lower()
        with open("config.json", "r") as data_file:
            data = json.load(data_file)

            id = data[account + '_' + 'id']
            token = data[account + '_' + 'access_token']

        retrieve_post(token);

def some_action(post):
        """ Here you might want to do something with each post. E.g. grab the
        post's message (post['message']) or the post's picture (post['picture']).
        In this implementation we just print the post's created time.
        """
        print(post['message'])

#retrive post
def retrieve_post(token_id):

    graph = facebook.GraphAPI(token_id)
    profile = graph.get_object('BillGates')
    posts = graph.get_connections(profile['id'], 'posts')

    while True:
        try:
            # Perform some action on each post in the collection we receive from
            # Facebook.
            [some_action(post=post) for post in posts['data']]
            # Attempt to make a request to the next page of data, if it exists.
            posts = requests.get(posts['paging']['next']).json()
        except KeyError:
            # When there are no more pages (['paging']['next']), break from the
            # loop and end the script.
            break

#post on facebook group
def post_on_group(token_id):
    graph = facebook.GraphAPI(token_id)
    groups = graph.get_object("me/groups")
    group_id = '1803611843284044'

    message = input("insert message")

    attachment = {
        'name': 'Oltremare',
        'link': 'https://www.facebook.com/permalink.php?story_fbid=805209756301573&id=771403016348914',
        'caption': 'Scopri oltremare',
        'description': 'bla bla bla bla',
    }

    graph.put_object(group_id, "post", message = message, attachment = attachment)


#post on facebook page
def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip
  # the following if you want to post as yourself.
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph

# read and print specific progress
def help():
    print (
        "\n     SeoAutoTool.py:                          open the complete interface of the tool\n" +
        "\n     SeoAutoTool.py C:                        open tool setting to add api key of various account\n" +
        "\n     SeoAutoTool.py F:                        open facebook option\n" +
        "\n     SeoAutoTool.py I:                        open instagram option\n" +
        "\n     SeoAutoTool.py T:                        open twitter option\n" +
        "\n     SeoAutoTool.py J:                        open joomla option\n" +
        "\n     SeoAutoTool.py L:                        open linkedin option\n")


# menu function
def menu(topic):
    if topic == "C":
        settings()
    if topic == "F":
        facebook_option()
# ----------------------main----------------------
if len(sys.argv) == 1:

    print("\nWelcome to SeoAutoTool: SeoOptimizer\n")

    print("Choose an action: \n"
          "- (C) open SeoAutoTool settings\n"
          "- (F) open Facebook option\n"
          "- (I) open Instagram option\n"
          "- (T) open Twitter option \n"
          "- (J) open Joomla option \n"
          "- (L) open Linkedin option \n"
          "- (H) show possible command\n\n")

    check_topic = False

    while check_topic == False:
        chose = input("What you want to do?").upper()

        if chose == "C" or chose == "F" or chose == "I" \
                or chose == "T" or chose == "J" or chose == "L" or chose == "H":

            check_topic = True

        else:
            print("wrong action\n\n")

        # call menu
        menu(chose)

else:
    if sys.argv[1].upper() == "C" or sys.argv[1].upper() == "F" or sys.argv[1].upper() == "I" \
            or sys.argv[1].upper() == "T" or sys.argv[1].upper() == "J" or sys.argv[1].upper() == "L" \
            or sys.argv[1].upper() == "H":
        # call menu
        menu(sys.argv[1].upper())
    else:
        print("\ncommand not found")
