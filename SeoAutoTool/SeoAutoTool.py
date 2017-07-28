# SeoAutoTool to optimize website, create share web for Seo

import sys
import os
import json
import facebook
import time
# ----------------------function----------------------

#give access token
def give_token():
    with open("settings.json", "r") as data_file:
        data = json.load(data_file)
        token = data['token']
        return token

def facebook_option():
    print("Choose an action: \n"
          "- (G) post message on group \n")

    choice = input("What do you want to do?").lower()

    '''if choice == "p":

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


        status = api.put_wall_post(msg, attachment=attachment)'''

    if choice == "g":

        token = give_token()

        file_check = False

        while file_check == False:
            account = input("insert file name: ").lower()

            if os.path.isfile('./' + account + '.json') == True:

                with open(account + ".json", "r") as data_file:
                    data = json.load(data_file)

                    #make post attachament
                    message = input("insert post message: ")
                    name = input("insert post name: ")
                    link = input("insert sharable post link: ")

                    for key, value in data.items():
                        post_on_group(token,value,message,name,link)
                        time.sleep(30)

                # close
                data_file.close()
            else:
                print("Ops! The file doesn't exist. Retry!")

    else:
        print("wrong action")

#post on facebook group
def post_on_group(token_id,group_id,message,name,link):
    graph = facebook.GraphAPI(token_id)
    groups = graph.get_object("me/groups")

    attachment = {
        'name': name,
        'link': "https://" + link,
    }

    graph.put_wall_post(message,attachment,group_id)


''''#post on facebook page
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
  return graph'''

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
        chose = input("What you want to do?: ").upper()

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
