import random
import string

CHAR = {
    'letter': [x for x in string.ascii_letters],
    'digit': [x for x in string.digits],
    'symbol': [x for x in string.punctuation]
}


def input_num(prompt, unspecified=None):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == unspecified:
                return
            num = int(user_input)
            return num if num >= 0 else 0   # prevent negative number
        except ValueError:
            print('Invalid input')


# Get all the parameter values from the user.
def input_args():
    args = {}
    args_count = 0
    length = input_num('Enter the length of the password: ')

    def args_sum():
        return sum(x for x in args.values() if x is not None)

    for i in CHAR:
        if args_count == 2 or args_sum() == length:
            break
        while True:
            num = input_num(
                f'Enter the number of {i}s (x: unspecified): ', 'x')
            if num is not None:
                if args_sum() + num > length:
                    print('Your characters exceed the password length')
                    continue
                args_count += 1
                args[i] = num
            break
    return length, args


def get_password(length, letter=None, digit=None, symbol=None):
    char_num = {
        'letter': letter,
        'digit': digit,
        'symbol': symbol
    }
    user_char_type = [x for x in char_num if char_num[x] is not None]
    password = []

    # Add random characters with number specified by the user.
    for i in user_char_type:
        password += [random.choice(CHAR[i]) for _ in range(char_num[i])]
        char_num.pop(i)
    # Fill up the password with random characters.
    if len(password) < length and len(char_num) > 0:
        keys = tuple(char_num.keys())
        password += [random.choice(CHAR[random.choice(keys)])
                     for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)


def main():
    print('+---------Password Generator---------+\n')
    length, args = input_args()
    print(f'Your password: {get_password(length, **args)}')


if __name__ == "__main__":
    main()
