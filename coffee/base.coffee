$.fn.extend(
    parallax: ->
        scroll_top = $(window).scrollTop()
        self = $(this)
        ratio = parseFloat(self.data('parallax-background-ratio'))
        self.css('background-position', "0 #{scroll_top * ratio}px")
)

$('#to-top').click ->
    $("html,body").animate({scrollTop: $("#top").offset().top}, 500)

$(window).scroll ->
    $('#home').parallax()
    scroll_top = $(window).scrollTop()
    console.log scroll_top

    if scroll_top > 0
        $('#to-top').css('opacity', 1)
    else
        $('#to-top').css('opacity', '0')
