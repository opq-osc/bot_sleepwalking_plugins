from botoy import Action, FriendMsg, GroupMsg, EventMsg,S
from botoy import decorators as deco


@deco.ignore_botself
def receive_friend_msg(ctx: FriendMsg):
    Action(ctx.CurrentQQ)


@deco.ignore_botself
def receive_group_msg(ctx: GroupMsg):
    #Action(ctx.CurrentQQ)
    path = '../plugins/bot_poem/300.json'
    with open(path, encoding='UTF-8') as file:
        data = json.load(file)
    pattern = r',|\.|/|;|\'|`|\[|\]|<|>|\?|:|"|\{|\}|\~|!|@|#|\$|%|\^|&|\(|\)|-|=|\_|\+|，|。|、|；|‘|’|【|】|·|！| |…|（|）'
    for i in data :
        if ctx.Content in i["contents"] :
            res = re.split(pattern, i["contents"])
            res = [x.strip() for x in res]
            S.text(res[res.index(test)+1])


def receive_events(ctx: EventMsg):
    Action(ctx.CurrentQQ)
