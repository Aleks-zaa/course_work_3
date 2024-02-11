from functions import data_clean, sort_status, sort_data, date_format, card_hidden, account_hidden


def main():
    """ Основная логика программы, которая выводит на экран список из 5 последних выполненных клиентом операций"""
    data = data_clean("operations.json")
    data = sort_status(data)
    sorted_data = sort_data(data)
    for item in sorted_data[:5]:
        from_to = item.get('from', 'not found')
        if from_to == 'not found':
            from_to = from_to
        elif len(str(from_to.split(" ")[-1])) < 20:
            from_to = card_hidden(from_to)
        else:
            from_to = account_hidden(from_to)
        date = date_format(item.get('date'))
        description = item.get("description", 'not found')
        to = item.get("to", 'not found')
        if to == 'not found':
            to = to
        elif len(str(to.split(" ")[-1])) < 20:
            to = card_hidden(to)
        else:
            to = account_hidden(to)
        amount = item.get('operationAmount', 'not found').get('amount', 'not found')
        currency = item.get('operationAmount').get('currency').get('name', 'not found')
        print(f'{date} {description}\n{from_to} -> {to}\n{amount} {currency} \n')


if __name__ == "__main__":
    main()
