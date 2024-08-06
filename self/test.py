
def show(sorted_items):
    for item in sorted_items:
        print(f"len {item}: {len(item)}")

def sortzxc(list_to_sort: list, new_list=[], start=0) -> list:
    for index in range(start, len(list_to_sort), 3):
        new_list.append(list_to_sort[index])
    if len(list_to_sort) != len(new_list):
        sortzxc(list_to_sort=list_to_sort, new_list=new_list, start=start+1)
    return new_list

embed_dict = {
    "title": "Embed Title",
    "description": "Embed Description",
    "color": 0xFEE75C,
    "timestamp": "",
    "author": {
        "name": "Embed Author",
        "url": "https://disnake.dev/",
        "icon_url": "https://disnake.dev/assets/disnake-logo.png",
    },
    "thumbnail": {"url": "https://disnake.dev/assets/disnake-logo.png"},
    "fields": [
        {"name": "Regular Title", "value": "Regular Value", "inline": "false"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
        {"name": "Inline Title", "value": "Inline Value", "inline": "true"},
    ],
    "image": {"url": "https://disnake.dev/assets/disnake-banner-thin.png"},
    "footer": {"text": "Embed Footer", "icon_url": "https://disnake.dev/assets/disnake-logo.png"},
}

items = list(embed_dict.keys())
items = ['description', 'author', 'title', 'timestamp', 'fields', 'color', 'thumbnail', "send",
                        'footer', 'image']


sorted_items = sorted(items, key=len, reverse=True)
print(f"\nSorted list: {sorted_items}")
show(sorted_items=sorted_items)

new_sorted = sortzxc(list_to_sort=sorted_items)
print(new_sorted)
show(sorted_items=new_sorted)

def check_3_elem(list_od: list, index=0):
    sum = 0
    for x in range(3):
        sum += len(list_od.pop(0))
    index = index + 1
    print(index, ": ", sum)
    if list_od:
        check_3_elem(list_od=list_od, index=index)
    else:
        return
print()
check_3_elem(new_sorted)