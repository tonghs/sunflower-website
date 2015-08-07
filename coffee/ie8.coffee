pathname = location.pathname
$("#header #menu ul li").removeClass('active')
$("#header #menu ul li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')
