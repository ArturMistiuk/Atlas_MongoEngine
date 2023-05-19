from connect import connection
from models import Author, Quote


def search_quote_from_name(user_args):
    name = user_args.split('name:')[1]
    # get obj Author from name to be sure everything is correct
    # author = Author.objects(fullname=name).first()
    quote = Quote.objects(author__fullname=name)
    print(quote)


def handle_argument(argument):
    if argument.startswith('name:'):
        return search_quote_from_name
    elif argument.startswith('tag:'):
        return search_quote_from_tag
    elif argument.startswith('tags:'):
        return search_quote_from_tags
    else:
        print('Unknown command!')


if __name__ == '__main__':
    while True:
        user_input = input('Write a query: ')
        command = handle_argument(user_input)
        command(user_input)
