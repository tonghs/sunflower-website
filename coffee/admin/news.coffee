$('.del').click ->
    self = $(this)
    $.confirm(->
        id = self.data('id')
        $.postJSON '/j/admin/del_news', {id_: id}, (o) ->
            location.reload()
        
    , '确定删除吗？')
