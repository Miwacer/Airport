from datetime import datetime


def filter_by_date(queryset, date_str, field_name):
    date = datetime.strptime(date_str, "%Y-%m-%d").date()
    filter_kwargs = {f"{field_name}__date": date}
    return queryset.filter(**filter_kwargs)
