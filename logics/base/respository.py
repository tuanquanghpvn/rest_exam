SORT_LATEST = 'latest-adddate'


class BaseRespository(object):
    @classmethod
    def filter_limit(cls, queryset, limit):
        return queryset.limit(limit) if limit else queryset

    @classmethod
    def filter_offset(cls, queryset, offset):
        return queryset.offset(offset) if offset else queryset

    @classmethod
    def sort_all(cls, queryset, sort, sort_table):
        """Sort queryset
        """
        if sort == SORT_LATEST:
            return queryset.order_by(sort_table.sa.ins_date.desc())
        if not sort:
            return queryset
        raise ValueError('sort condition is invalid')
