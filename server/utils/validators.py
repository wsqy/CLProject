from django.core.validators import MinValueValidator, MaxValueValidator


def int_validators(_min=1, _max=100):
    validators_list = []
    if isinstance(_min, int):
        validators_list.append(MinValueValidator(_min, message=('不能小于%(limit_value)s.')))
    if isinstance(_max, int):
        validators_list.append(MaxValueValidator(_max, message=('不能大于%(limit_value)s.')))
    return validators_list
