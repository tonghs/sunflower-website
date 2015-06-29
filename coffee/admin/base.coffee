pathname = location.pathname
$(".nav>li").removeClass('active')
$(".nav>li").each ->
    self = $(this)
    if self.children("a").attr('href') == pathname
        self.addClass('active')
