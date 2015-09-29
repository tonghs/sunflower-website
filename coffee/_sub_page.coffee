pathname = location.pathname
$("#left>ul>li").removeClass('active')
$("#left>ul>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')
