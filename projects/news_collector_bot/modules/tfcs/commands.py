def modify(data, pizza):
    """
    Изменяет данные согласно запросу

    :param data: поле, содержащее данные, которые необходимо изменить
    :param pizza: экземпляр класса бота
    """
    fields = data.keys()
    for field in fields:
        setattr(pizza, field, data[field].value)

