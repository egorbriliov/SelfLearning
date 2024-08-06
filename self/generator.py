import disnake
embed_dict_with_nested_dicts = {
    0: {
        "embed": disnake.Embed().add_field(name="First steps",
                                           value="To get started, you need to use /embed").set_image(
            url="https://media.discordapp.net/attachments/1262719342500384861/1263953249317158925"
                "/chrome_kLpriNSOYs.gif?ex=669cc471&is=669b72f1&hm=1ee7a00ba18ec13806ba67345c2641a614297018c603282b"
                "0d758b0dc0d08c19&=&width=718&height=344"),
        "url": ""
    },
    1: {
        "embed": disnake.Embed().add_field(name="Add something",
                                           value="To add something, you need to click a button and out the "
                                                 "modal window").set_image(
            url="https://media.discordapp.net/attachments/1262719342500384861/1263953248507658240/chrome_c3lv00QRtE.gif"
                "?ex=669cc471&is=669b72f1&hm=8e1c5511664041c4305e154478edac16514df527a4e3e1342998a19536caad5b&=&width=718"
                "&height=344"),
        "url": ""
    },
    2: {
        "embed": disnake.Embed().add_field(name="Delete something",
                                           value="To delete something, you need to click a button").set_image(
            url="https://media.discordapp.net/attachments/1262719342500384861/1263953248927092869/chrome_dD06gFqCWc"
                ".gif?ex=669cc471&is=669b72f1&hm=1edf969222a076794162a38d5ca7f92824a6940b3f6ae23ebb054172fc251dc6&="
                "&width=718&height=344"),
        "url": ""
    }
}

print("\nДобро пожаловать!")

embed_dict = {}
bool_value = True
while bool_value:
    print("\nНачало заполнения нового шага: ")
    name = input("Введите name: ")
    value = input("Введите value: ")
    image_url = input("Введите image_url: ")
    original_message_sourse = input("Введите original_message_sourse: ")
    if embed_dict.keys(): new_item_index = max(embed_dict.keys()) + 1
    else: new_item_index = 0
    embed_dict[new_item_index] = {
        "embed": {
            "fields": [
                {"name": name,
                "value": value,
                "inline": False}
            ],
            "image": {
                "url": image_url
            }
        },
        "url": original_message_sourse
        }
    bool_value = True if input("Хотите продолжить (y/n): ") == "y" else False

print("\n", embed_dict)