from django import template


register = template.Library()


@register.filter(name='plural_comments')
def plural_comments(numberComments):

    try:
        numberComments = int(numberComments)
        if numberComments == 0:
            return f'Nenhum comentário'
        elif numberComments == 1:
            return f'{numberComments} comentário'
        else:
            return f'{numberComments} comentários'
    except:
        return f'{numberComments} comentários'