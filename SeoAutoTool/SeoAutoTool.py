# SeoAutoTool to optimize website, create share web for Seo

import sys
import json
import facebook
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
    cfg = {
        'page_id': '1984826991748449',
        'access_token': 'EAACxukgPRjUBAGjzIZCE2OFmfDlJNylScTULmZBQLrc4UuM6294mfxDGXrlcSuqpBRf1uFbhVQWsZA20q8LeZCZBRdI4svGZBfTwXtGBFZCXMnYo2KCGxINiiaMBiwFntbGh16gVxA6K9e2CZBZCodQQsTE2GXD7uE0nGqWEYDGNyCwZDZD'
    }

    api = get_api(cfg)
    msg = "i like 5"
    status = api.put_wall_post(msg)

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
