import random
import yaml


_ignored_if_depth = 0
_defines = {}
_event_defines = {}
_items = []
_items_unshuffled = []
_locations = []


def load_settings(logic_path: str, settings_path: str):
    global _defines
    default_settings = parse_default_settings(logic_path)

    settings_file = open(settings_path)
    settings_yaml = yaml.safe_load(settings_file)
    loaded_settings = settings_yaml["settings"]
    # add the settings to the defines
    # save the settings as strings, so we can easilly replace them in the defines
    for def_setting in default_settings:
        setting_name = def_setting["Name"]

        if setting_name in loaded_settings:
            # setting overwritten: load that
            load_single_setting(yaml_to_setting(def_setting, loaded_settings[setting_name]))
        else:
            # setting not in setting file: load default
            load_single_setting(def_setting)


def load_single_setting(setting):
    setting_name = setting["Name"]
    setting_type = setting["Type"]
    setting_value = setting["Value"]

    match setting_type:
        case "Flag":
            load_flag_setting(setting_name, setting_value)
        case "Dropdown":
            set_define(setting_name, str(setting_value))
        case "Numberbox":
            set_define(setting_name, str(setting_value))
        case "Color":
            load_color_setting(setting_name, setting_value)


def load_flag_setting(name: str, value: bool):
    if value:
        set_define(name)


def load_color_setting(name: str, colors):
    set_define(name)
    for num, color in enumerate(colors):
        set_define(f"{name}_{num}", color)


def yaml_to_setting(default_setting, yaml_value):
    setting_name = default_setting["Name"]
    setting_type = default_setting["Type"]

    new_setting = default_setting

    match setting_type:
        case "Flag":
            new_setting["Value"] = yaml_value
            return new_setting
        case "Dropdown":
            new_setting["Value"] = yaml_value
            return new_setting
        case "Numberbox":
            new_setting["Value"] = yaml_value
            return new_setting
        case "Color":
            # we currently do not support loading color cosmetics
            print("Error: color is not supposed to get loaded")
            return new_setting



# run through the logic file and load the context for the settings and defaults
def parse_default_settings(file_path: str):
    logic_lines = open(file_path, "r").readlines()
    logic_lines = preprocess_lines(logic_lines)

    default_settings = []

    for line in logic_lines:
        if not is_directive(line):
            continue

        new_setting = parse_settings_directive(line)
        if new_setting is None:
            continue
        default_settings.append(new_setting)
    return default_settings


def process_file(file_path: str):
    logic_lines = open(file_path, 'r').readlines()
    logic_lines = preprocess_lines(logic_lines)
    
    for line in logic_lines:

        if should_ignore_lines():
            if is_directive(line):
                parse_conditional(line)
            continue

        line = replace_define(line)

        if is_directive(line):
            if is_logic_directive(line):
                parse_logic_directive(line)
            continue

        # otherwise this is an item or location
        parse_item_or_location(line[0])


def preprocess_lines(logic_lines):
    cleaned_lines = []
    for line in logic_lines:
        # remove whitespace
        clean_line = "".join(line.split())

        # clean out comments
        clean_line = clean_line.split("#")[0]

        # ignore empty lines
        if len(clean_line) == 0:
            continue

        # split all tokens
        new_directive = clean_line.split("-")
        cleaned_lines.append(new_directive)

    return cleaned_lines


def replace_define(directive):
    # check for defined variables
    for i, token in enumerate(directive):
        if "`HEART_OUTLINE_COLOR" in token:
            i = i

        if "`" not in token:
            continue

        # replace builtin `RAND_INT` with random number
        if "RAND_INT" in token:
            rand_int = random.randint(0, 0x7FFFFFFF)  # TODO: implement seeded random number generator
            directive[i] = token.replace("`RAND_INT`", format(rand_int, "x"))
        else:
            find_defines = token.split("`")[1::2]
            for define_token in find_defines:
                if define_token in _defines:
                    dir_i = directive[i]
                    new_dir = dir_i.replace(define_token, _defines[define_token])
                    directive[i] = new_dir
                else:
                    # TODO exception, define does not exist
                    print(f"Error: replace define [{define_token}] in {token}, has not yet been defined")

        directive[i] = directive[i].replace("`", "")
    return directive


def is_directive(directive):
    return directive[0][0] == "!"


def is_logic_directive(directive):
    settings_directives = [
        "!flag",
        "!color",
        "!name",
        "!version",
        "!crc",
        "!dropdown",
        "!numberbox"
    ]
    logic_directives = [
        "!define",
        "!addition",
        "!undefine",
        "!eventdefine",
        "!ifdef",
        "!ifndef",
        "!else",
        "!elseifdef",
        "!elseifndef",
        "!endif",
        "!replace",
        "!replaceamount",
        "!replaceincrement",
        "!settype",
        "!import"
    ]
    if any(x in directive[0] for x in settings_directives):
        return False
    if any(x in directive[0] for x in logic_directives):
        return True
    #TODO throw error 
    return False


def parse_settings_directive(directive):
    if is_logic_directive(directive):
        return None

    match directive[0]:
        case "!flag":
            return parse_flag(directive)
        case "!color":
            return parse_color(directive)
        case "!dropdown":
            return parse_dropdown(directive)
        case "!numberbox":
            return parse_numberbox(directive)
        case _:
            print(f"Error: unsupported directive [{directive[0]}]")
    return None


def parse_logic_directive(directive):



    if not is_logic_directive(directive):
        return

    if is_conditional_directive(directive):
        parse_conditional(directive)
        return

    match directive[0]:
        case "!define":
            parse_define(directive)
        case "!undefine":
            parse_undefine(directive)
        case "!eventdefine":
            parse_event_define(directive)
        case "!replace":
            parse_replace(directive)
        case "!replaceamount":
            parse_replace_amount(directive)
        case "!replaceincrement":
            parse_replace_increment(directive)
        case "!addition":
            parse_addition(directive)
        case "!settype":
            parse_settype(directive)
        case "!import":
            parse_import(directive)
        case _:
            print(f"Error: unsupported directive [{directive[0]}]")


def is_conditional_directive(directive):
    conditionals = [
        "!ifdef",
        "!ifndef",
        "!else",
        "!endif",
    ]
    return any(x in directive[0] for x in conditionals)


def parse_conditional(directive):
    global _ignored_if_depth
    
    match directive[0]:
        case "!ifdef":
            if should_ignore_lines() or not define_exists(directive[1]):
                _ignored_if_depth += 1
        case "!ifndef":
            if should_ignore_lines() or define_exists(directive[1]):
                _ignored_if_depth += 1
        case "!else":
            if should_ignore_lines():
                if _ignored_if_depth <= 1:
                    _ignored_if_depth -= 1
                    #if _ignored_if_depth < 0:
                    #    print("What? I didn't know we could have the depth go below zero ordinarily")
                    #    exit(0)
            else:
                _ignored_if_depth += 1
        case "!endif":
            if _ignored_if_depth > 0:
                _ignored_if_depth -= 1

def define_exists(define_string):
    return define_string in _defines


def parse_define(directive):
    define_tokens = parse_define_directive(directive)
    set_define(define_tokens[0], define_tokens[1])

def set_define(define_name: str, define_value: str = ""):
    _defines.update({define_name: define_value})


def parse_undefine(directive):
    define_tokens = parse_define_directive(directive)
    clear_define(define_tokens[0])


def clear_define(define_name: str):
    global _defines
    if define_name in _defines:  # only remove if the define exists, in the default logic file this bug exists
        _defines.pop(define_name)
    else:
        print(f'cannot undef key: {define_name}, it was never defined')

def parse_define_directive(directive):
    if any("RAND_INT" in token for token in directive):
        # TODO exception
        print("Error: cannot change RAND_INT definition")
        return

#    directive[1] = directive[1].replace("`", "")
    num_params = len(directive)
    if num_params == 2:
        return [directive[1], ""]
    if num_params == 3:
        return [directive[1], directive[2]]
    
    # TODO exception
    print("Error incorrect number of parameters!")
    return


def parse_event_define(directive):
    define_tokens = parse_define_directive(directive)
    _event_defines.update({define_tokens[0]: define_tokens[1]})


def parse_import(directive):
    pass


def parse_addition(directive):
    print("Error: !addition unimplemented")


def parse_settype(directive):
    print("Error: !settype unimplemented")


def parse_replace(directive):
    pass


def parse_replace_amount(directive):
    pass


def parse_replace_increment(directive):
    pass


def parse_setting_define_name(directive):
    return directive[4]


def parse_flag(directive):
    define_name = parse_setting_define_name(directive)
    default_value = False

    if len(directive) == 8:
        default_value = directive[7] == "true"

    return {"Type": "Flag",
            "Name": define_name,
            "Value": str(default_value)}


def parse_color(directive):
    define_name = parse_setting_define_name(directive)
    color_vals = []

    i = 8
    while len(directive) >= i:
        col_r = directive[i - 1].replace("0x", "")
        col_g = directive[i].replace("0x", "")
        col_b = directive[i + 1].replace("0x", "")
        color_vals.append(f"{col_r}{col_g}{col_b}")
        i += 3

    return {"Type": "Color",
            "Name": define_name,
            "Value": color_vals}

def parse_dropdown(directive):
    define_name = parse_setting_define_name(directive)
    default_value = directive[7]

    return {"Type": "Dropdown",
            "Name": define_name,
            "Value": default_value}

def parse_numberbox(directive):
    define_name = parse_setting_define_name(directive)
    default_value = directive[7]

    return {"Type": "Numberbox",
            "Name": define_name,
            "Value": default_value}


def should_ignore_lines():
    return _ignored_if_depth != 0


def parse_item_or_location(line):
    # is this an item or location
    if token_is_item(line):
        parse_item(line)
    else:
        parse_location(line)


def token_is_item(token):
    return token.startswith("Items")


def parse_item(line):
    def get_item(item_line):
        split_tokens = item_line.split(":")
        item_amount = 1
        if len(split_tokens) > 1:
            item_amount = int(split_tokens[1])

        item_tokens = split_tokens[0].split(".")

        item_type = item_tokens[1]
        item_subtype = None
        if len(item_tokens) > 2:
            item_subtype = item_tokens[2]

        item = {"Type": item_type, "SubType": item_subtype}
        return item, item_amount

    # Items are built up in two different ways:
    #   In the item pool, they are - Items.(type).[subtype]:[amount]; (item pool type); [dungeon_id]
    #    On unshuffled locations, they are - Items.(type).[subtype]

    # split line into tokens
    tokens_1 = line.split(";")
    new_item, amount = get_item(tokens_1[0])

    if len(tokens_1) == 1:  # unshuffled item
        global _items_unshuffled
        for _ in range(0, amount):
            _items_unshuffled.append(new_item)
    else:
        new_item["Pool"] = tokens_1[1]
        new_item["Dungeon"] = None
        if len(tokens_1) >= 2:
            new_item["Dungeon"] = tokens_1[2]

        global _items
        for _ in range(0, amount):
            _items.append(new_item)


def parse_location(line):
    # A location is built up as
    # (name):[dungeon id1]:[dungeon_id2]:...:[dungeon_idN]; (location type); (address); [logic]; [item] (Only applies to Unshuffled locations)
    #
    tokens_1 = line.split(";")
    name_and_dungeon_tokens = tokens_1[0].split(":")
    location_name = name_and_dungeon_tokens[0]
    location_dungeon_ids = name_and_dungeon_tokens[1:]
    location_type = tokens_1[1]
    location_address = tokens_1[2]
    location_logic = ""
    location_item = ""
    if len(tokens_1) > 3:
        location_logic = tokens_1[3]
    if len(tokens_1) > 4:
        location_item = tokens_1[4]

    global _locations
    _locations.append({"Name": location_name, "Dungeon_ids": location_dungeon_ids,
                       "Type": location_type, "Address": location_address,
                       "Logic": location_logic, "Item": location_item})


if __name__ == "__main__":
    logic_path = "C:/source/Archipelago/worlds/loz_tmc/default.logic"
    settings_path = "C:/source/Archipelago/worlds/loz_tmc/Preset.yaml"

    load_settings(logic_path, settings_path)
    process_file(logic_path)

    for _loc in _locations:
        print(_loc)

