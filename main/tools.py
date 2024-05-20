import re


def extract_phone_numbers(text):
    # Define the regex patterns for different phone number formats
    patterns = [
        r'9\d{2}\s\d{3}\s\d{4}',  # 9xx xxx xxxx
        r'9\d{2}\s\d{4}\s\d{3}',  # 9xx xxxx xxx
        r'9\d{2}-\d{3}-\d{4}',  # 9xx-xxx-xxxx
        r'9\d{2}\s\(\d{3}\)\s\d{4}',  # 9xx (xxx) xxxx
        r'9\s\d\s\d\s\d\s\d\s\d\s\d\s\d\s\d',  # 9 x x x x x x x x x
        r'9\s-\d\s\(\d\s\d{2}\)\)\d\s\d{2}-\d\s\d',  # 9 -x (x xx))x xx-x x
        r'\+98\d{10}',  # +98xxxxxxxxxx
        r'09\d{9}',  # 09xxxxxxxxx
        r'9\d{9}',  # 9xxxxxxxxx
        r'\+\u06F9\d\s\(\d{3}\)\s\d{2}\s\d{2}\s\d{3}'  # +۹x (xxx) xx xx xxx (Persian digits)
        r'۹[\u06F0-\u06F9]{2}\s[\u06F0-\u06F9]{3}\s[\u06F0-\u06F9]{4}',  # ۹xx xxx xxxx
        r'۹[\u06F0-\u06F9]{2}\s[\u06F0-\u06F9]{4}\s[\u06F0-\u06F9]{3}',  # ۹xx xxxx xxx
        r'۹[\u06F0-\u06F9]{2}-[\u06F0-\u06F9]{3}-[\u06F0-\u06F9]{4}',  # ۹xx-xxx-xxxx
        r'۹[\u06F0-\u06F9]{2}\s\([\u06F0-\u06F9]{3}\)\s[\u06F0-\u06F9]{4}',  # ۹xx (xxx) xxxx
        r'۹\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]\s[\u06F0-\u06F9]',
        r'۹\s-[\u06F0-\u06F9]\s\([\u06F0-\u06F9]\s[\u06F0-\u06F9]{2}\)\)[\u06F0-\u06F9]\s[\u06F0-\u06F9]{2}-[\u06F0-\u06F9]\s[\u06F0-\u06F9]',
        r'\+۹۸[\u06F0-\u06F9]{10}',  # +۹۸xxxxxxxxxx
        r'۰۹[\u06F0-\u06F9]{9}',  # ۰۹xxxxxxxxx
        r'۹[\u06F0-\u06F9]{9}',  # ۹xxxxxxxxx
        r'\d{2}[۰۹]\d{2}\s\d{3}\s\d{4}',  #٠٩xx xxx xxxx
    ]

    # Compile the patterns into a single pattern
    combined_pattern = '|'.join(patterns)
    regex = re.compile(combined_pattern)

    # Find all matches in the text
    matches = regex.findall(text)

    return matches


def save_numbers(numbers_list, tags, set_tag=True):

    if set_tag:
        target_tags = '   '
        if tags:
            for tag in tags:
                target_tags = target_tags + str(tag) + ' '
        else:
            target_tags = target_tags + '_'

        with open("numbers_with_tag.txt", "a", encoding="utf-8") as f:
            for number in numbers_list:
                english_number = convert_persian_to_english(number)
                f.write(english_number + target_tags + "\n")

        return True

    with open("numbers.txt", "a", encoding="utf-8") as f:
        for number in numbers_list:
            english_number = convert_persian_to_english(number)
            f.write(english_number + "\n")

    return True


def save_error_numbers(text):
    with open("error_numbers.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n" + "***" + "\n")

    return True


def count_numbers(filename):
    with open(filename, 'r') as file:
        count = 0
        for line in file:
            count += 1
    return count


def convert_persian_to_english(text):
    persian_to_english_map = {
        '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4',
        '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9'
    }

    translated_text = ''

    for char in text:
        if char in persian_to_english_map:
            translated_text += persian_to_english_map[char]
        else:
            translated_text += char

    return translated_text


def extract_tags(text):
    pattern = r'#\w+'
    tags = re.findall(pattern, text)
    # Remove the leading # from each tag
    tags = [tag for tag in tags]
    return tags

