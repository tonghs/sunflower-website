pathname = location.pathname
$(".nav>li").removeClass('active')
$(".nav>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')

$('.table-expandable>tbody>tr>td>a.open').click ->
    obj = $(this).parent('td').parent('tr').next()
    if obj.attr('class') and obj.attr('class').indexOf('collapse') >= 0
        if obj.css('display') == 'none'
            obj.slideDown()
        else
            obj.slideUp(0)
